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
            sh "systemctl start docker"
             sh "docker-compose up" 
           
      
            

         }
      }
   }
}
