pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-docker"
        IMAGE_TAG = "v1"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'master', url: 'https://github.com/santoshkumar711/Python-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Stop Existing Container') {
            steps {
                // Agar container exist nahi karta to ignore karo
                bat "docker stop %IMAGE_NAME% || exit 0"
                bat "docker rm %IMAGE_NAME% || exit 0"
            }
        }

        stage('Run Docker Container') {
            steps {
                bat "docker run -d --name %IMAGE_NAME% -p 5000:5000 %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Docker Login & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds', // ya tumhara credentials ID
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    bat "docker login -u %USERNAME% -p %PASSWORD%"
                    bat "docker tag %IMAGE_NAME%:%IMAGE_TAG% %USERNAME%/%IMAGE_NAME%:%IMAGE_TAG%"
                    bat "docker push %USERNAME%/%IMAGE_NAME%:%IMAGE_TAG%"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
