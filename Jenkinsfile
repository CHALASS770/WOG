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
             sh "docker-compose up" 
           
      
            

         }
      }
   }
}
