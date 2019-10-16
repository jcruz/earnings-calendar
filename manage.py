from app.flask_app import app  # noreorder

from flask_script import Manager

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
