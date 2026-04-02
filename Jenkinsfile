pipeline {
    agent any

    stages {
        stage("Clone") {
            steps {
                git 'https://github.com/rasolonjanahary/Projet_CICD_avec_jenkins.git'
            }
        }

        stage ("Install python"){
            steps {
                sh 'winget install --id Python.Python.3.12 -e --source winget && python --version'
            }
        }

        stage("Environnement python"){
            steps {
                sh 'python -m venv venv'
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
                sh 'docker buid -t wine_fraud_image .'
            }
        }
    } 
}