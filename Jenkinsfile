pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                bat "docker build -t task-tracker:latest ."
            }
        }
        stage("Test") {
            steps {
                bat """
                  docker run --rm task-tracker:latest ^
                    /bin/sh -c "pip install pytest && export PYTHONPATH=/app && pytest tests --maxfail=1 -q"
                """
            }
        }
        stage("Code Quality") {
            steps {
                bat """
                  docker run --rm task-tracker:latest ^
                    /bin/sh -c "pip install flake8 && flake8 ."
                """
            }
        }
        stage("Deploy") {
            steps {
                bat """
                  docker rm -f task-tracker || echo Container not found^>nul
                  docker run -d --name task-tracker -p 5000:5000 task-tracker:latest
                """
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
