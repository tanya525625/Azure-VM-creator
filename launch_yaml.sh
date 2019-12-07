mkdir ~/.azure
touch ~/.azure/credentials
echo -n "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
pip3 install -r requirements.txt
ansible-playbook launch_vm.yml
