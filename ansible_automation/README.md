# Simple Ansible example of Docker Container with Open vSwitch as network bridge    


## Verifying Ansible is proper configured        
ansible -i /etc/ansible/hosts all -m ping    

## Run OvS Container Playbook
ansible-playbook main.yaml


