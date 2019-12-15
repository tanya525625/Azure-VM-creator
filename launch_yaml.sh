sh mkdir.sh
pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
pip3 install azure
pip3 install azure-servicebus==0.21.1
apt install sshpass
ansible-playbook launch_vm.yml