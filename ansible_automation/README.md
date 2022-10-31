nano /etc/ansible/hosts

//kbl01
cd /data/imsa

//test
ansible -i /etc/ansible/hosts all -m ping


//run playbook
ansible-playbook main.yaml


//ensure the host is accessible external
nano /etc/resolv.conf
