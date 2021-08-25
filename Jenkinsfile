pipeline {
  agent any
  stages {
    stage('Git clone') {
      agent any
      steps {
        git(url: 'https://github.com/veerenchawda03/K8s-helm-jenkins.git', branch: 'main')
      }
    }

    stage('Docker build') {
      agent {
        docker {
          image 'docker:20.10'
        }

      }
      steps {
        sh 'docker build -t veeren03/fastapi03:latest .'
      }
    }

    stage('Docker push') {
      agent {
        docker {
          image 'docker:20.10'
        }

      }
      steps {
        sh 'docker push veeren03/fastapi03:latest'
      }
    }

    stage('') {
      agent any
      steps {
        kubernetesEngineDeploy(cluster: 'cluster-1', clusterName: 'cluster-1', credentialsId: 'f54befdf-0ffb-43d7-ad7c-dd25238a0b23', location: 'us-central1-c	', manifestPattern: '/Deployment.yaml', projectId: 'erudite-store-319509', verifyTimeoutInMinutes: 5, zone: 'c')
      }
    }

  }
}