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
     
        stage ('Criando .env') {
            steps {
                script {
                sh 'touch .env'
                sh 'echo "DOCKER_TYPE=${env.DOCKER_TYPE}" >> .env'
                sh 'echo "DOCKER_API_SERVER=${env.DOCKER_API_SERVER}" >> .env'
                sh 'echo "DOCKER_API_PORT=${env.DOCKER_API_PORT}" >> .env'
                sh 'echo "REGISTRY=${env.REGISTRY}" >> .env'
                sh 'echo "USERNAME=${env.USERNAME}" >> .env'
                sh 'echo "PASSWORD=${env.PASSWORD}" >> .env'
                sh 'echo "REPOSITORY=${env.REPOSITORY}" >> .env'
                sh 'echo "TAG=${env.TAG}" >> .env'
                sh 'echo "PORTS=${env.PORTS}" >> .env'
                }
            }
        }  

        stage ('Deploy Container in Windows Server') {
            steps {
                sh 'python3 teste.py'
                // sh 'apidocker-deploy.py'
            }
        }
    }
}





