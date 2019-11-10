pipeline {
   agent any

   stages {
      stage('checkout')
      {
         steps{
         git "https://github.com/CHALASS770/WOG.git"
            }
      }
      
      stage('build') {
         steps {
            docker.withRegistry ('https://registry.hub.docker.com', 'docker-hub-credentials')
            sh "docker-compose up"

         }
      }
   }
}
