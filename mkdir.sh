DIR=~/.azure

if [ ! -d "$DIR" ]; then
    # make dir if it doesn't exist
    sh prepare_environment.sh
fi
