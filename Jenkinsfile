pipeline {
  agent any
  stages {
    stage('Build Gradle') {
      steps {
        withGradle()
      }
    }

    stage('Code Inspection') {
      steps {
        archiveArtifacts '1'
      }
    }

    stage('Test') {
      steps {
        junit '1'
      }
    }

    stage('Security Check') {
      steps {
        readTrusted '1'
      }
    }

    stage('Package') {
      steps {
        archiveArtifacts '1'
      }
    }

    stage('Push to Storage(Artifact)') {
      steps {
        s3PresignURL(bucket: '33', key: '2', httpMethod: 'get', durationInSeconds: 60)
      }
    }

    stage('Request Deploy') {
      steps {
        waitUntil()
        input(message: 'Do you wanna trigger for Deploy pipeline?', id: '1', submitter: 'r.baek', submitterParameter: 'Yes')
      }
    }

  }
}