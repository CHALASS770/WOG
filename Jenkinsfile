pipeline {
   agent any

   stages {
      stage('connect')
      {
         steps{
         git "https://github.com/CHALASS770/WOG.git"
            }
      }
      stage('build') {
         steps {
            sh "docker-compose up"

         }
      }
   }
}
