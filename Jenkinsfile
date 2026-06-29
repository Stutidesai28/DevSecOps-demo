def retryForTimeoutExceeded(count = 3, Closure closure) {
    for (int i = 1; i <= count; i++) {
        try {
            closure()
            break
        } catch (org.jenkinsci.plugins.workflow.steps.FlowInterruptedException error) {
            int retriesLeft = count - i
            def hasTimeoutExceeded = error.causes[0].getClass().toString() == 'class org.jenkinsci.plugins.workflow.steps.TimeoutStepExecution$ExceededTimeout'
            println "Timeout Exceeded for closure.\nRetries left: $retriesLeft"
            if (retriesLeft == 0 || !hasTimeoutExceeded) {
                throw error
            }
        }
    }
}

node('jenkins-jenkins-agent') {

    stage('SCM') {
        checkout scm
    }

    stage('SonarQube Analysis') {
        def scannerHome = tool 'SonarScanner'

        withSonarQubeEnv {
            sh """
                ${scannerHome}/bin/sonar-scanner \
                -Dsonar.projectKey=demo123 \
                -Dsonar.python.version=3.11
            """
        }
    }

    stage('Quality Gate') {
        timeout(time: 20, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
        }
    }

    stage('Trivy Filesystem Scan') {
        sh '''
        trivy fs \
            --format table \
            --severity HIGH,CRITICAL \
            --exit-code 1 \
            .
        '''
    }
}