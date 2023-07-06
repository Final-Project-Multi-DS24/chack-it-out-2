# 모듈 로드
import pandas as pd
import random
from flask import Flask, render_template, request

# flask 객체 생성
app = Flask(__name__)


# 홈 경로 + 라우터 함수
@app.route("/")
def index():
    df = pd.read_csv("sampledata.csv")
    urls = list(df["urls"])
    url = urls[random.randint(0, 24)]
    return render_template("index.html", random=random, urls=urls)


# 회원가입_라우터
@app.route("/register/")
def register():
    return render_template("register.html")


# app.py를 직접 실행해야만 flask 앱이 실행.
# 개발중 - debug=True
if __name__ == "__main__":
    app.run(debug=True)
