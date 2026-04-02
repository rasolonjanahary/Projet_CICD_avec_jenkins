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
                sh '''
                    sudo apt update
                    sudo apt install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage("Environnement python"){
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r require.txt
                '''
            }
        }

        stage("Run training") {
            steps {
                sh '''
                . venv/bin/activate
                python notebook/train.py
                '''
            }
        }

        stage("Run testing") {
            steps {
                sh '''
                . venv/bin/activate
                python notebook/test.py
                '''
            }
        }

        stage("Build") {
            steps {
                sh 'docker buid -t wine_fraud_image .'
            }
        }
    } 
}