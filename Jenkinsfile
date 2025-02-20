pipeline {
    agent any

    environment {
        AZURE_WEBAPP_NAME = 'flask-api-app'
        AZURE_RESOURCE_GROUP = 'flask-api-group'
        DOCKER_IMAGE_NAME = 'flask-api'
        ACR_NAME = 'youracrname'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE_NAME .'
            }
        }

        stage('Push Docker Image to Azure Container Registry') {
            steps {
                withAzureCLI(credentialsId: 'azure-credentials') {
                    sh '''
                    az acr login --name $ACR_NAME
                    docker tag $DOCKER_IMAGE_NAME $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME
                    docker push $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy to Azure') {
            steps {
                withAzureCLI(credentialsId: 'azure-credentials') {
                    sh '''
                    az webapp create --resource-group $AZURE_RESOURCE_GROUP --plan myAppServicePlan \
                    --name $AZURE_WEBAPP_NAME --deployment-container-image-name $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
