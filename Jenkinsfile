pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'kubernates_django_userSystem', url: 'https://github.com/it21918/userSystem.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    source myvenv/bin/activate
                    pip install -r requirements.txt
                    cd userSystem
                    cp userSystem/.env.example userSystem/.env
                    ./manage.py test'''
            }
        }
        
    
        stage('deploym to vm 1') {
            steps{
                sshagent (credentials: ['ssh-deploy']) {
                    sh '''
                        ansible-playbook -i ~/workspace/ansible-project/ansible-test-jenkins/hosts.yml -l deploymentjenkins ~/workspace/ansible-project/ansible-test-jenkins/playbooks/django2-install-microk8s.yml
                    '''
                }

            }

        }
    }
}
