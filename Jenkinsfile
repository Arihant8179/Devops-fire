pipeline {
    agent any
    environment {
        REMOTE = "ec2-user@${env.DEPLOY_HOST}"
        SSH_KEY = credentials('ec2-ssh-key') // configure in Jenkins credentials
    }


    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Build Docker Image') {
            steps {
                sh 'docker build -t forestfire:latest .'
            }
        }


        stage('Push/Deploy') {
            steps {
                script {
                    def remote = "${env.DEPLOY_HOST}"
                    sh "ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ec2-user@${remote} 'docker pull || true'"
                    sh "ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ec2-user@${remote} 'cd ~/ForestFire || git clone https://github.com/Arihant8179/Devops-fire.git ~/ForestFire; cd ~/ForestFire; git pull; docker build -t forestfire:latest .; docker rm -f forestfire_app || true; docker run -d --name forestfire_app -p 5000:5000 --restart unless-stopped forestfire:latest'"
                }
            }
        }
    }
}   