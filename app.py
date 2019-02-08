import datetime
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

# movies 테이블 생성
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    poster_url = db.Column(db.TEXT, nullable=False)
    description = db.Column(db.TEXT, nullable=False)




@app.route("/")
def index():
    return "hi"
    
    
    
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)