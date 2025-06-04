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
        stage("Demo") {
            steps {
                // Wait a moment for the container to be fully up
                bat "timeout 3"
                
                // 1. Wake up at 6 am
                bat "curl -X POST http://localhost:5000/tasks ^\n" +
                    "-H \"Content-Type: application/json\" ^\n" +
                    "-d \"{\\\"title\\\":\\\"Wake up at 6am\\\"}\""
                
                // 2. Go to gym
                bat "curl -X POST http://localhost:5000/tasks ^\n" +
                    "-H \"Content-Type: application/json\" ^\n" +
                    "-d \"{\\\"title\\\":\\\"Go to gym\\\"}\""
                
                // 3. Study two chapters
                bat "curl -X POST http://localhost:5000/tasks ^\n" +
                    "-H \"Content-Type: application/json\" ^\n" +
                    "-d \"{\\\"title\\\":\\\"Study two chapters\\\"}\""
                
                // 4. Do laundry
                bat "curl -X POST http://localhost:5000/tasks ^\n" +
                    "-H \"Content-Type: application/json\" ^\n" +
                    "-d \"{\\\"title\\\":\\\"Do laundry\\\"}\""
                
                // Finally, GET the complete list of tasks
                bat "curl http://localhost:5000/tasks"
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}
