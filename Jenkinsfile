pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'cred-jenkins', 
                    url: 'https://github.com/CHINNAKOTLAJAGANNATH/Flask_API_Capstone_Project.git',
                    branch: 'main'
            }
        }
    }
}
