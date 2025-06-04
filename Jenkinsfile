pipeline {
    agent any

    environment {
        // (any environment variables if you had them; remove if none)
    }

    stages {
        stage('Build') {
            steps {
                // Build the Docker image
                bat 'docker build -t task-tracker:latest .'
            }
        }

        stage('Test') {
            steps {
                // Run pytest inside a temporary container
                bat '''docker run --rm task-tracker:latest ^
    /bin/sh -c "pip install pytest && export PYTHONPATH=/app && pytest tests --maxfail=1 -q"'''
            }
        }

        stage('Code Quality') {
            steps {
                // Run flake8 inside a temporary container
                bat '''docker run --rm task-tracker:latest ^
    /bin/sh -c "pip install flake8 && flake8 ."'''
            }
        }

        stage('Deploy') {
            steps {
                // Remove any existing container named task-tracker (ignore errors)
                bat 'docker rm -f task-tracker || echo Container not found>nul'
                // Start a new detached container on port 5000
                bat 'docker run -d --name task-tracker -p 5000:5000 task-tracker:latest'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
