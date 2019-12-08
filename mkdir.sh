DIR=~/.azure

if [ ! -d "$DIR" ]; then
    # Создать папку, только если ее не было
    sh prepare_environment.sh
fi