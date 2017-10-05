import os

def get(env_path=None):
    token = None
    if env_path:
        with open(os.path.abspath(env_path)) as fp:
            token = fp.read().strip() or None
    return token or os.environ.get('KOKOROIO_ACCESS_TOKEN')
