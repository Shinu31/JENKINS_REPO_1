pipeline{
    agent any
    environment{
                 Python = "C:\\Users\\Shinu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
               }
    stages{
        stage('checkout code'){
            steps{
                {
                    checkout scm
                }}
        stage('show python version'){
            steps{
                
                    bat "${env.python} --version"
                }
        }
        stage('run extract script'){
            steps{
                
                    bat "${env.python} extract.py"
                }
        }
    }
    }
}




