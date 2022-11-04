pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps {
                script {
                    dockerapp = docker.build("registry.idados.local/wp-teste:${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }
        
        stage ('Push Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.idados.local', 'registry.idados')
                        dockerapp.push('latest')
                        dockerapp.push('${env.BUILD_ID}')
                }
            }
        }
    }
}