## An Ansible Playbook example on Docker Container with Open vSwitch as network bridge automation    

This example is assumed that user has been:
1. Installed Ansible engine 
2. SSH setup on all hosts    

Tutorial could be found on https://docs.ansible.com/ansible/latest/getting_started/index.html

### Verifying Ansible is proper configured        
```
ansible -i /etc/ansible/hosts all -m ping    
```

### Run OvS Container Playbook
The playbook is expected the host directory all shell scripts files (the *.sh files in this project) will be located inside /data/ovs-test, if this not the case, please change the main.yaml "path" variable accordingly:
```
ansible-playbook main.yaml
```


