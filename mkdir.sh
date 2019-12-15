DIR=~/.azure
FILE=~/.azure/credentials

if [ ! -f "$FILE" ]; then
  if [ ! "$DIR" ]; then
    mkdir ~/.azure
  fi
  # make dir if it doesn't exist
  sh prepare_environment.sh
fi

pip3 install azure
pip3 install azure-servicebus==0.21.1
pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
apt install sshpass