pipeline {
    agent none

    stages {

        stage ('Build Docker Image') {
            agent any

            steps {
                
		sh 'docker build --tag hello:$BUILD_NUMBER .'
		sh 'echo "Hello Jenkins..!!"'
            }
        }
        stage ('Run Docker Container') {
            agent any

            steps {
                
		sh 'docker ps | grep hello && docker stop hello && docker rm hello'
		sh 'docker run -d --name hello -p 8000:5000 hello:$BUILD_NUMBER'
            }
        }
    }
}

