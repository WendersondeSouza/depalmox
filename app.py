from flask import Flask
from routes import route_register
from database import criar_db

app = Flask(__name__)

criar_db()
route_register(app)

if __name__ == "__main__":
    criar_db()
    app.run(debug=True)



