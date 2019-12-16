DIR=~/.azure
FILE=~/.azure/credentials

if [ ! -f "$FILE" ]; then
  if [ ! -d "$DIR" ]; then
    mkdir ~/.azure
  fi
  # make dir if it doesn't exist
  touch ~/.azure/credentials
  echo -n "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
fi

curl -sL https://aka.ms/InstallAzureCLIDeb | bash
pip3 install azure
apt install sshpass
pip3 install ansible[azure]
pip3 install azure-servicebus==0.21.0
# ansible-playbook create_vm.yml
