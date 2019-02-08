from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 및 sqlalchemy 설정
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_flask.sqlite3"
app.config["SQLALCHEMY_TREACK_MODIFICATIONS"] = False

# sqlalchemy 및 migration 초기화
db = SQLAlchemy(app)
migrate = Migrate(app, db)




@app.route("/")
def index():
    return "hi"
    
    
    
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)