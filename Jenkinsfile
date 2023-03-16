pipeline {
    agent any
    stages {
        stage('verify') {
            agent {
                docker { image 'maven' }
            }
        }
    }
}
