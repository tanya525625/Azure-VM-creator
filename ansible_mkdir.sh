DIR=/etc/ansible/
FILE=/etc/ansible/hosts

if [ ! -f "$FILE" ]; then
    # make dir if it doesn't exist
    if [ ! -d "$DIR" ]; then
      mkdir $DIR
    fi
    echo "VM ansible_host=$VM_IP ansible_ssh_user=$admin_username ansible_ssh_pass=$admin_password" > /etc/ansible/hosts
fi

rm ~/.ssh/known_hosts
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook start_environment_preparation_for_VM.yml