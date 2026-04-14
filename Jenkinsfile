pipeline {
    agent any

    environment {
        REGISTRY = "192.168.88.50"
        PROJECT = "projet_cicd"
        IMAGE_NAME = "wine_fraud_image"
        TAG = "latest"
    }

    stages {
        stage("Clone") {
            steps {
                git 'https://github.com/rasolonjanahary/Projet_CICD_avec_jenkins.git'
            }
        }

        stage ("Verifier python"){
            steps {
                bat 'C:\\Users\\rasolonjanahary\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
            }
        }

        stage("Environnement python"){
            steps {
                bat 'C:\\Users\\rasolonjanahary\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv'
                sh 'source venv/Scripts/activate && pip install -r require.txt'
            }
        }

        stage("Run training") {
            steps {
                sh 'source venv/Scripts/activate && python notebook/train.py'
            }
        }

        stage("Run testing") {
            steps {
                sh 'source venv/Scripts/activate && python notebook/test.py'
            }
        }

        stage("Build") {
            steps {
                sh 'docker compose up -d --build && docker images && docker ps'
            }
        }

        stage('Login to Harbor') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'harbor-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh "docker login -u $USERNAME -p $PASSWORD ${REGISTRY}"
                }
            }
        }

        stage('Push Image to Harbor') {
            steps {
                sh "docker push ${REGISTRY}/${PROJECT}/${IMAGE_NAME}:${TAG}"
            }
        }
    } 
}