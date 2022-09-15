pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'docker_django_userSystem', url: 'https://github.com/it21918/django_userSystem.git'

                
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
                    chmod +x manage.py
                    ./manage.py test'''
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
    

    }
}
