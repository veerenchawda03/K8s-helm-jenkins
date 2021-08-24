pipeline {
  agent any
  stages {
    stage('Git clone') {
      steps {
        git(url: 'https://github.com/veerenchawda03/K8s-helm-jenkins.git', branch: 'main', credentialsId: '	497c6d82-3e51-4e07-80fa-81170e4495c3')
      }
    }

    stage('Docker build') {
      steps {
        sh 'docker build -t veeren03/fastapi03:latest .'
      }
    }

    stage('Docker push') {
      steps {
        sh 'docker push veeren03/fastapi03:latest'
      }
    }

    stage('') {
      steps {
        kubernetesEngineDeploy(cluster: 'cluster-1', clusterName: 'cluster-1', credentialsId: 'c7fe6dc8-c52e-4bb0-aaef-100f294535e2', location: 'us-central1-c', manifestPattern: '/Deployment.yaml', projectId: 'erudite-store-319509', verifyTimeoutInMinutes: 5, zone: 'c')
      }
    }

  }
}