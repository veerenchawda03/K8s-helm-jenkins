pipeline {
  agent any
  stages {
    stage('Git clone') {
      agent any
      steps {
        git(url: 'https://github.com/veerenchawda03/K8s-helm-jenkins.git', branch: 'main', credentialsId: '0b3f05d2-f5f7-4827-96bc-890ddff5acd3')
      }
    }

    stage('Docker build') {
      agent {
        docker {
          image 'docker'
          
        }

      }
      steps {
        sh 'docker build -t veeren03/fastapi:latest .'
      }
    }

    stage('Docker push') {
      agent {
        docker {
          image 'docker'
          
        }

      }
      steps {
        sh 'docker push veeren03/fastapi03:latest'
      }
    }

    stage('Deploy staging') {
      agent any
      steps {
        kubernetesEngineDeploy(cluster: 'cluster-1	', clusterName: 'cluster-1	', credentialsId: '220f2d7e-4165-4885-aae4-d651d0e547d2', location: 'us-central1-c	', manifestPattern: '/Deployment.yaml', projectId: 'erudite-store-319509', verifyTimeoutInMinutes: 5, zone: 'c')
      }
    }

    stage('Deploy prod') {
      agent any
      steps {
        kubernetesEngineDeploy(cluster: 'cluster-2', clusterName: 'cluster-2', credentialsId: '220f2d7e-4165-4885-aae4-d651d0e547d2', location: 'us-central1-c	', manifestPattern: '/Deployment.yaml', projectId: 'erudite-store-319509', verifyTimeoutInMinutes: 5, zone: 'c')
      }
    }

  }
}
