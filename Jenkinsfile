pipeline {
    agent any

    stages {
        stage ('Variables wp-config.php') {
            steps {
                sh 'sed -i s/"DATABASE_NAME"/"mysql"/g wp-config.php'
                sh 'sed -i s/"DATABASE_USER"/"root"/g wp-config.php'
                sh 'sed -i s/"DATABASE_PASSWORD"/"JAVA>PHPin2012IN!2018"/g wp-config.php'
                sh 'sed -i s/"DATABASE_HOST"/"10.10.10.6:3306"/g wp-config.php'
            }
        }

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





