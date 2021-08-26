env.WORKSPACE = "D:/test_jenkins/Feishu"


pipeline{
    agent any

    stages {

		stage('start') {
			steps {
				echo 'Strat Test ~~~~'
				}
			}

        stage("download-code"){
            steps {
				dir(env.WORKSPACE){
					checkout([$class: 'GitSCM', branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[credentialsId: 'gitee-redmi', url: 'https://gitee.com/blue-juziupup/feishu-test.git']]])
					}
				}
			}
		stage("Run Test"){
            steps {
				dir(env.WORKSPACE){
					bat 'python main.py'
				}
			}
		}
		stage("reports"){
            steps {
				dir(env.WORKSPACE){
					bat "allure includeProperties: false, jdk: '', results: [[path: 'report/result']]"
				}
			}
        }

		stage("end"){
            steps {
				echo "End test ~~~~"
				}
		}
	}
}