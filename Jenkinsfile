node {
     stage('Clone repository') {
         checkout scm
     }
     stage('Build image') {
         app = docker.build("34.132.155.133/admin/flask-example")
         
     }
     stage('Push image') {
         docker.withRegistry('https://34.132.155.133', 'harbor-cred') {
             app.push("${env.BUILD_NUMBER}")
             app.push("latest")
         }
     }
}

stage('Build image') {
  app = docker.build("34.132.155.133/admin/flask-example")
}

stage('Push image') {
  docker.withRegistry('https://34.132.155.133', 'harbor-cred') 
  {
     app.push("${env.BUILD_NUMBER}")
     app.push("latest")
  }
}
