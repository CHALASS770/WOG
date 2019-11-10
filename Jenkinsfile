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
             app.inside { 
            sh 'echo "Tests passés"'

        / * Enfin, nous allons pousser l'image avec deux balises: 
         * Premièrement, le numéro de build incrémental de Jenkins 
         * Deuxièmement, la balise 'latest'. 
         * Pousser plusieurs étiquettes est bon marché, car toutes les couches sont réutilisées. * / 
        docker.withRegistry ('https://registry.hub.docker.com', 'docker-hub-credentials') { 
            app.push ("$ {env.BUILD_NUMBER}") 
            app.push ("dernière") 
        } 
    } 
            sh "docker-compose up"

         }
      }
   }
}
