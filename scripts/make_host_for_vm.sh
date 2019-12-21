sudo mkdir /etc/ansible
sudo -n echo "VM ansible_host=$VM_IP ansible_ssh_user=$admin_username ansible_ssh_pass=$admin_password">/etc/ansible/hosts
ansible-playbook ./configs/start_environment_preparation_for_VM.yml