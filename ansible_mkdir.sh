DIR=/etc/ansible

if [ ! -d "$DIR" ]; then
    # make dir if it doesn't exist
    sudo -n echo "VM ansible_host=$VM_IP ansible_ssh_user=$admin_username ansible_ssh_pass=$admin_password" > /etc/ansible/hosts
fi
ansible-playbook start_environment_preparation_for_VM.yml