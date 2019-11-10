pipeline {
   agent any

   stages {
      stage('checkout')
      {
         steps{
         git "https://github.com/CHALASS770/WOG.git"
            }
      }
      
      stage('build-docker') {
         steps {
            sh "systemctl start docker" /*don't work i don't know why*/
             sh "docker-compose up" /*don't work its said docker can't start */ 
         }
      }
      stage('build-e2e.py')
      {
         steps
         {
            sh "python2.5 e2e.py" /*don't work it's said selenium don't exist*/
         }
      }
   }
}
