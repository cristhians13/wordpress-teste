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
        
        // stage ('Push Image') {
        //     steps {
        //         script {
        //             docker.withRegistry('https://registry.idados.local', 'registry.idados')
        //                 dockerapp.push('latest')
        //                 dockerapp.push('${env.BUILD_ID}')
        //         }
        //     }
        // }

        stage('Push Docker Images to Nexus Registry'){
            sh 'docker login -u appservice -p Au#apS3jz4.q1vyz@1uFV registry.idados.local'
            sh 'docker push registry.idados.local/wp-teste:${env.BUILD_ID}'
            sh 'docker rmi $(docker images --filter=reference="registry.idados.local/wp-teste:${env.BUILD_ID}" -q)'
            sh 'docker logout registry.idados.local'
        }
    }
}