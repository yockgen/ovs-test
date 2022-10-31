## An Ansible Playbook example on Docker Container with Open vSwitch as network bridge automation    

This is example is assumed that user has been:
1. Installed Ansible engine 
2. SSH setup on all hosts    

Tutorial could be found on https://docs.ansible.com/ansible/latest/getting_started/index.html

### Verifying Ansible is proper configured        
```
ansible -i /etc/ansible/hosts all -m ping    
```

### Run OvS Container Playbook
```
ansible-playbook main.yaml
```


