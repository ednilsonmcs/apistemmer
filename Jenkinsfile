pipeline {
    agent any
    stages {
        stage('verify') {
            steps {
                sh '''
                    docker version
                '''
            }
        }
    }
}
