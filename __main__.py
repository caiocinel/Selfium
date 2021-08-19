from app import cli
from app import auth
from app.filesystem import validate

if __name__ == '__main__':
    cli.logo()
    auth.run()