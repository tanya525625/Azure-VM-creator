DIR=~/.azure

if [ ! -d "$DIR" ]; then
    # make dir if it doesn't exist
    sh prepare_environment.sh
fi
pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
pip3 install azure
pip3 install azure-servicebus==0.21.1
apt install sshpass