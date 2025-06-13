from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート
import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    return {"result" : omikuji_list[random.randrange(10)]}
### コードいろいろ... ###
@app.get("/index")
def index():
    html_content = """
    <!DOCTYPE html>
　　<html lang="ja">
        <head>
        　<meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pythonたいへんだそん</title>
        </head>
    <body>
    <h1>基本情報受かりたい</h1>
    <p>目指せ後二日で巻き返し</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
@app.post("/zyanken")
async def givepresent(zyanken):
          givepresent_list = [
            "グー",
            "チョキ",
            "パー"
            ]
          return {"response": f"サーバです。ジャンケンしましょ！ {zyanken}ありがとう。私の手は{givepresent_list[random.randrange(3)]}です"}  # f文字列というPythonの機能を使っている