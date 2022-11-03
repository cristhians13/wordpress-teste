pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps {
                script {
                    dockerapp = docker.build("cristhians/wordpress-teste:${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }
    }
}