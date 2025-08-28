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
                script {
                    // Docker image build
                    sh 'docker build -t hello-docker:v1 .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop & remove old container if exists
                    sh '''
                        docker stop hello-docker || true
                        docker rm hello-docker || true
                        docker run --rm -d -p 5000:5000 --name hello-docker hello-docker:v1
                    '''
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Push image to DockerHub
                    sh 'docker tag hello-docker:v1 santoshkumar711/hello-docker:v1'
                    sh 'docker push santoshkumar711/hello-docker:v1'
                }
            }
        }
    }
}
