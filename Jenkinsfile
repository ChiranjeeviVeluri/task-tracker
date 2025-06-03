pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                // Build the Docker image on the Windows host
                bat "docker build -t task-tracker:latest ."
            }
        }
        stage("Test") {
            steps {
                // Run pytest inside the Linux-based container
                bat """
                  docker run --rm task-tracker:latest ^
                    /bin/sh -c "pip install pytest && pytest --maxfail=1 -q"
                """
            }
        }
        stage("Code Quality") {
            steps {
                // Run flake8 inside the Linux-based container
                bat """
                  docker run --rm task-tracker:latest ^
                    /bin/sh -c "pip install flake8 && flake8 ."
                """
            }
        }
        stage("Deploy") {
            steps {
                // Remove any old container, then run a new one
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
