import os


class CreadentialsParser:
    def __init__(self, subscription_id, client_id, secret, tenant):
        self.credentials = f'[default] \n' \
                           f'subscription_id={subscription_id} \n' \
                           f'client_id={client_id} \n' \
                           f'secret={secret} \n' \
                           f'tenant={tenant}'

    def make_credentials(self):
        os.chmod(r"/root", 777)
        make_dir('/root/.azure')
        with open('/root/.azure/credentials', 'w') as out_file:
            out_file.write(self.credentials)


def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
