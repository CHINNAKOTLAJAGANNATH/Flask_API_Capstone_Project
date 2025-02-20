pipeline {
    agent any

   
    stage('Clone Repository') {
    steps {
        git credentialsId: 'cred-jenkins', 
            url: 'https://github.com/CHINNAKOTLAJAGANNATH/Flask_API_Capstone_Project.git',
            branch: 'main'
    }
}

        stage('Set Up Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    

    post {
        success {
            echo 'Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}
