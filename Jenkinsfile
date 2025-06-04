pipeline {
    agent any

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t task-tracker:latest .'
            }
        }

        stage('Test') {
            steps {
                bat '''
                    docker run --rm task-tracker:latest /bin/sh -c "pip install pytest && export PYTHONPATH=/app && pytest tests --maxfail=1 -q"
                '''.stripIndent()
            }
        }

        stage('Code Quality') {
            steps {
                bat '''
                    docker run --rm task-tracker:latest /bin/sh -c "pip install flake8 && flake8 ."
                '''.stripIndent()
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f task-tracker || echo Container not found>nul'
                bat 'docker run -d --name task-tracker -p 5000:5000 task-tracker:latest'
            }
        }

        stage('Demo') {
            steps {
                // pause for 3 seconds on Windows
                bat 'timeout /t 3 /nobreak >nul'

                // verify the app is running (adjust URL/port if needed)
                bat 'curl http://localhost:5000 || echo "Unable to reach app on port 5000"'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
