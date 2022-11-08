pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps {
                script {
                    dockerapp = docker.build("${env.IMAGE_NAME}:${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }
        
        stage ('Push Image') {
            steps {
                script {
                    docker.withRegistry("${env.URL_REGISTRY}", 'registry.idados') {
                        dockerapp.push('latest')
                        dockerapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }

        stage ('Deploy Container in Windows Server') {
            steps {
                sh 'apidocker-deploy.py'
            }
        }
    }
}





