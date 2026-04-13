pipeline {
    agent any

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
                sh 'docker build -t wine_fraud_image . && docker run -d wine_fraud_image && docker images && docker ps'
            }
        }
    } 
}