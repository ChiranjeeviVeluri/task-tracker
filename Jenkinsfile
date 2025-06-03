pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                // Build the Docker image on Windows
                bat "docker build -t task-tracker:latest ."
            }
        }
        stage("Test") {
            steps {
                // Run pytest inside a temporary container on Windows
                bat """
                  docker run --rm task-tracker:latest ^
                    cmd /c "pip install pytest && pytest --maxfail=1 -q"
                """
            }
        }
        stage("Code Quality") {
            steps {
                // Run flake8 inside a temporary container on Windows
                bat """
                  docker run --rm task-tracker:latest ^
                    cmd /c "pip install flake8 && flake8 ."
                """
            }
        }
        stage("Deploy") {
            steps {
                // Remove any old container, then run a new one (Windows syntax)
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
