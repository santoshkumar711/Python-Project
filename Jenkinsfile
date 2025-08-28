pipeline {
    agent any

    environment {
        IMAGE_NAME = 'hello-docker'
        IMAGE_TAG  = 'v1'
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
                bat "docker stop %IMAGE_NAME% || exit 0"
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat "docker tag %IMAGE_NAME%:%IMAGE_TAG% %DOCKER_USER%/%IMAGE_NAME%:%IMAGE_TAG%"
                bat "docker push %DOCKER_USER%/%IMAGE_NAME%:%IMAGE_TAG%"
            }
        }
    }
}
