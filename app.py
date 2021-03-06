from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 및 sqlalchemy 설정
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_flask.sqlite3"
app.config["SQLALCHEMY_TREACK_MODIFICATIONS"] = False

# post 방식의 secret_key 설정
app.secret_key = "qhshqhshqksksk"


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



# 첫 메인 화면 생성
@app.route("/")
def main():
    return render_template("main.html")

# movies 페이지 생성
@app.route("/movies")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies = movies)

# movies/new 페이지 생성. 사용자에게 영화 목록 추가 할 form 생성
@app.route("/movies/new")
def new_movie():
    return render_template("new.html")
    
# movies/create 페이지 생성.
@app.route("/movies/create", methods=["POST"])
def create_movie():
    movie = Movie()
    movie = Movie(**request.form)
    

    # lists = dict(request.form)
    
    # for key, val in lists.items():
    #     print(key, val)
    #     movie.key = val
    
    # for key, val in lists.items():
    #     print(movie.key)

    # movie.title = request.form.get("title")
    # movie.title_en = request.form.get("title_en")
    # movie.audience = request.form.get("audience")
    # movie.open_date = request.form.get("open_date")
    # movie.genre = request.form.get("genre")
    # movie.watch_grade = request.form.get("watch_grade")
    # movie.score = request.form.get("score")
    # movie.poster_url = request.form.get("poster_url")
    # movie.description = request.form.get("description")
    

    
    
    
    
    db.session.add(movie)
    db.session.commit()
    
    flash(f"{movie.title}이/가 생성되었습니다.", "success")
    return redirect(f"/movies/{movie.id}")


# 영화 정보 조회 페이지 생성
@app.route("/movies/<int:id>")
def read_movie(id):
    movie = Movie.query.get(id)
    return render_template("show.html", movie=movie)
    
# 영화 정보 수정 Form
@app.route("/movies/<int:id>/edit")
def edit_movie(id):
    movie = Movie.query.get(id)
    return render_template("edit.html", movie=movie)

# 영화 정보 업데이트
@app.route("/movies/<int:id>/update", methods=["POST"])
def update_movie(id):
    movie = Movie.query.get(id)
    # for key, value in request.form.items():
    #     setattr(movie, key, value)
    #     movie.__setattr__(key, value)
    
    movie.title = request.form.get("title")
    movie.title_en = request.form.get("title_en")
    movie.audience = request.form.get("audience")
    movie.open_date = request.form.get("open_date")
    movie.genre = request.form.get("genre")
    movie.watch_grade = request.form.get("watch_grade")
    movie.score = request.form.get("score")
    movie.poster_url = request.form.get("poster_url")
    movie.description = request.form.get("description")
    
    
    db.session.commit()
    
    return redirect(f"/movies/{movie.id}")
    # return render_template("update.html")

# 영화 정보 삭제
@app.route("/movies/<int:id>/delete")
def delete_movie(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    flash(f"{movie.title}이/가 삭제되었습니다.", "danger")
    return redirect("/movies")
    
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)