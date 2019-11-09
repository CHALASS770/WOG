pipeline {
   agent any

   stages {
      stage('checkout')
      {
         steps{
         git "https://github.com/CHALASS770/WOG.git"
            }
      }
      stage('start'){
         steps{
            sh "bash start.sh"
         }
      }
      stage('build') {
         steps {
            sh "docker-compose up"

         }
      }
   }
}
