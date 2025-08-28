pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/santoshkumar711/Python-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hello-docker:v1 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                docker stop hello-docker || exit 0
                docker rm hello-docker || exit 0
                docker run -d -p 5000:5000 --name hello-docker hello-docker:v1
                '''
            }
        }

        stage('Docker Login') {
            steps {
                // Replace <DOCKER_PASSWORD> with your Docker Hub password or access token
                bat 'docker login -u santoshkumar711 -p <DOCKER_PASSWORD>'
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat 'docker tag hello-docker:v1 santoshkumar711/hello-docker:v1'
                bat 'docker push santoshkumar711/hello-docker:v1'
            }
        }
    }
}
