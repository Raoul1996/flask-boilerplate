from api import create_app

# sets up the app
app = create_app()

# adds the python manage.py db init, db migrate, db upgrade commands

if __name__ == "__main__":
        app.run()

