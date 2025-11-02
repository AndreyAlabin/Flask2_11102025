import os, sys
sys.path.append(os.path.pardir)
from my_app import create_app
# from my_app.config import ProductionConfig
# from my_app.config import DevelopmentConfig

app = create_app()

print(app.config)

if __name__ == '__main__':
    app.run(
        port=app.config['PORT'],
        host=app.config['SERVER_NAME'],
        debug=app.config['DEBUG']
    )
