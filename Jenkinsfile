pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                sh "docker build -t task-tracker:latest ."
            }
        }
        stage("Test") {
            steps {
                sh '''
                  docker run --rm task-tracker:latest \
                    /bin/sh -c "pip install pytest && pytest --maxfail=1 -q"
                '''
            }
        }
        stage("Code Quality") {
            steps {
                sh '''
                  docker run --rm task-tracker:latest \
                    /bin/sh -c "pip install flake8 && flake8 ."
                '''
            }
        }
        stage("Deploy") {
            steps {
                sh '''
                  docker rm -f task-tracker || true
                  docker run -d --name task-tracker -p 5000:5000 task-tracker:latest
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
