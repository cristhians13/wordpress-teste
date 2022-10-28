pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps {
                script {
                    dockerapp = docker.build("cristhians/wordpress-teste", '-f ./Dockerfile')
                }
            }
        }
    }
}