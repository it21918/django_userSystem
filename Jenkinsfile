pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/it21918/django_userSystem.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    #source myvenv/bin/activate
                    source myvenv/Scripts/activate
                    pip install -r requirements.txt
                    cd userSystem
                    cp userSystem/.env.example userSystem/.env
                    chmod +x manage.py
                    ./manage.py test'''
            }
        }
        
        stage('Prepare DB') {
            steps {
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        pwd
                        echo $WORKSPACE
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l database ~/workspace/ansible-django/playbooks/postgres.yml
                        '''
            }
            }
        }
        
        stage('Prepare Docker') {
            steps {
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        pwd
                        echo $WORKSPACE
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l database ~/workspace/ansible-django/playbooks/docker-install.yml
                        '''
            }
            }
        }
        
        stage('deploy docker userSystem image to vm 1') {
            steps {
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        pwd
                        echo $WORKSPACE
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l database ~/workspace/ansible-django/playbooks/django-userSystem-docker.yml
                        '''
            }
            }
        }
    
        stage('deploym to vm 1') {
            steps{
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                        ansible-playbook -i ~/workspace/ansible-django/hosts.yml -l deploymentservers ~/workspace/ansible-django/playbooks/django-project-install-userSystem.yml
                    '''
                }

            }

        }
    }
}
