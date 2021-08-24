pipeline {
  agent any
  stages {
    stage('Clone repo') {
      steps {
        git(url: 'https://github.com/veerenchawda03/K8s-helm-jenkins.git', branch: 'main', credentialsId: '497c6d82-3e51-4e07-80fa-81170e4495c3')
      }
    }

  }
}