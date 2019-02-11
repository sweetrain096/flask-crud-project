# Project 04 flaks-crud

## 1. 기본 설정

```python
# app.py

import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 및 sqlalchemy 설정
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_flask.sqlite3"
app.config["SQLALCHEMY_TREACK_MODIFICATIONS"] = False

# sqlalchemy 및 migration 초기화
db = SQLAlchemy(app)
migrate = Migrate(app, db)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
```





## 2. 데이터베이스 생성

- ORM을 통해서 작성 될 클래스의 이름은 Movie, 테이블 명은 movies 입니다. 
- 다음과 같은 정보를 저장합니다. 
  - 모든 필드 값에는 빈 값이 들어갈 수 없습니다. title 을 제외한 다른 필드는 중복이 허용됩니다.



```python
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

```



## 3. 데이터 추가

- python 터미널 (데이터 추가)

```python
from app import *
movie1 = Movie()                                                                
movie1.title = "극한직업"
movie1.title_en="Extreme Job"
movie1.audience=10,990,185
movie1.open_date = "01/23/19"
movie1.genre = "코미디"
movie1.watch_grade = "15세관람가"
movie1.score = 9.27
movie1.poster_url = "https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode=167651"
movie1.description = '''줄거리
... 낮에는 치킨장사! 밤에는 잠복근무!
... 지금까지 이런 수사는 없었다!
... 불철주야 달리고 구르지만 실적은 바닥, 급기야 해체 위기를 맞는 마약반!
...  더 이상 물러설 곳이 없는 팀의 맏형 고반장은 국제 범죄조직의 국내 마약 밀반입 정황을  포착하고
...  장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다.
...  마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되 고,
...  뜻밖의 절대미각을 지닌 마형사의 숨은 재능으로 치킨집은 일약 맛집으로 입소문이 나기 시작한다.
...  수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아 오는데…
...  
...  범인을 잡을 것인가, 닭을 잡을 것인가!'''


db.session.add(movie1)
db.session.commit()
```



- sqlite3 터미널(데이터 확인)

```sqlite
SELECT * FROM movies;
```

out:

1|극한직업|Extreme Job|10990185|01/23/19|코미디|15세관람가|9.27|https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode=167651|줄거리
낮에는 치킨장사! 밤에는 잠복근무!
지금까지 이런 수사는 없었다!
불철주야 달리고 구르지만 실적은 바닥, 급기야 해체 위기를 맞는 마약반!
 더 이상 물러설 곳이 없는 팀의 맏형 고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착 하고
 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다.
 마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되고,
 뜻밖의 절대미각을 지닌 마형사의 숨은 재능으로 치킨집은 일약 맛집으로 입소문이 나기 시작한다.
 수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아오는 데…

 범인을 잡을 것인가, 닭을 잡을 것인가!





## 4. 페이지 생성

### 1. 메인 페이지



- app.py

```python
from flask import Flask, render_template

# 첫 메인 화면 생성
@app.route("/")
def main():
    return render_template("main.html")
```

- main.html

```html
<h1>영화 목록 사이트입니다!</h1>
```



### 2. movies 페이지

- app.py

  ```python
  # movies 페이지 생성
  @app.route("/movies")
  def index():
      movies = Movie.query.all()
      return render_template("index.html", movies = movies)
  ```

- index.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h2><a href="/movies/new">새 영화 등록</a></h2>
      
      <ul>
          {% for movie in movies %}
              <p><a href="/movies/read/{{movie.id}}">{{movie.title}} ({{movie.title_en}}) : {{movie.score}}</a></p>
              <hr>
          {% endfor %}
      </ul>
  </body>
  </html>
  ```



### 3. movies/new 페이지

- app.py

  ```python
  # movies/new 페이지 생성. 사용자에게 영화 목록 추가 할 form 생성
  @app.route("/movies/new")
  def new_movie():
      return render_template("new.html")
  ```

- new.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>영화 추가</title>
  </head>
  <body>
      <form action="/movies/create", method="POST">
          영화명 : <input type="text" name="title"> <br>
          영화명(영문) : <input type="text" name="title_en"> <br>
          관객수 : <input type="int" name="audience"> <br>
          개봉일 : <input type="text" name="open_date"> <br>
          장르 : <input type="text" name="genre"> <br>
          등급 : <input type="text" name="watch_grade"> <br>
          별점 : <input type="float" name="score"> <br>
          영화 포스터 url : <input type="text" name="poster_url"> <br>
          줄거리 : <input type="text" name="description"> <br>
          <input type="submit" value="등록!">
      </form>
  </body>
  </html>
  ```



### 4. create

- app.py

  ```python
  # movies/create 페이지 생성.
  @app.route("/movies/create", methods=["POST"])
  def create_movie():
      movie = Movie()
      movie.title = request.form.get("title")
      movie.title_en = request.form.get("title_en")
      movie.audience = request.form.get("audience")
      movie.open_date = request.form.get("open_date")
      movie.genre = request.form.get("genre")
      movie.watch_grade = request.form.get("watch_grade")
      movie.score = request.form.get("score")
      movie.poster_url = request.form.get("poster_url")
      movie.description = request.form.get("description")
      db.session.add(movie)
      db.session.commit()
      return render_template("create.html")
  ```

- create.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <p>영화 정보 생성이 완료되었습니다.</p>
      <a href="/movies">영화 목록으로 돌아가기</a>
  </body>
  </html>
  ```

  

### 5. show

- app.py

  ```python
  # 영화 정보 조회 페이지 생성
  @app.route("/movies/<int:id>")
  def read_movie(id):
      movie = Movie.query.get(id)
      return render_template("show.html", movie=movie)
  ```

- show.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>영화 상세 정보</title>
  </head>
  <body>
      <ul>
          <h2>{{movie.title}} ({{movie.title_en}})</h2> <br>
          <img src="{{movie.poster_url}}"/> <br>
          <p>개봉 일 : {{movie.open_date}}</p> <br>
          <p>관객 수 : {{movie.audience}}</p> <br>
          <p>장르 : {{movie.genre}}</p> <br>
          <p>등급 : {{movie.watch_grade}}</p> <br>
          <p>평점 : {{movie.score}}</p> <br>
          <p>줄거리 : {{movie.description}}</p> <br>
          
      </ul>
  </body>
  </html>
  ```

  



### 6. 영화 정보 수정 form 생성(edit)

- app.py

  ```python
  # 영화 정보 수정 Form
  @app.route("/movies/<int:id>/edit")
  def edit_movie(id):
      movie = Movie.query.get(id)
      return render_template("edit.html", movie=movie)
  ```

- edit.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>영화 수정</title>
  </head>
  <body>
      <form action="/movies/{{movie.id}}/update", method="POST">
          영화명 : <input type="text" name="title" value={{movie.title}}> <br>
          영화명(영문) : <input type="text" name="title_en" value={{movie.title_en}}> <br>
          관객수 : <input type="int" name="audience" value={{movie.audience}}> <br>
          개봉일 : <input type="text" name="open_date" value={{movie.open_date}}> <br>
          장르 : <input type="text" name="genre" value={{movie.genre}}> <br>
          등급 : <input type="text" name="watch_grade" value={{movie.watch_grade}}> <br>
          별점 : <input type="float" name="score" value={{movie.score}}> <br>
          영화 포스터 url : <input type="text" name="poster_url" value={{movie.poster_url}}> <br>
          줄거리 : <input type="textarea" name="description"/> <br>
          <input type="submit" value="수정!">
      </form>
  </body>
  </html>
  ```

  

### 7. 영화 정보 업데이트

- app.py

  ```python
  # 영화 정보 업데이트
  @app.route("/movies/<int:id>/update", methods=["POST"])
  def update_movie(id):
      movie = Movie.query.get(id)
      
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
      
      return render_template("update.html")
  ```

- update.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h2>영화 정보 수정이 완료되었습니다.</h2>
      <a href="/movies">영화 목록으로 돌아가기</a>
  </body>
  </html>
  ```

  

### 8. 영화 정보 삭제

- app.py

  ```python
  # 영화 정보 삭제
  @app.route("/movies/<int:id>/delete")
  def delete_movie(id):
      movie = Movie.query.get(id)
      db.session.delete(movie)
      db.session.commit()
      return redirect("/movies")
      
  ```

  

