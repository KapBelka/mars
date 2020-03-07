from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def mission_name():
    return """<h1 align="center">Миссия Колонизация Марса</h1>"""


@app.route("/index")
def mission_tagline():
    return """<h1 align="center">И на Марсе будут яблони цвести!</h1>"""


@app.route("/promotion")
def mission_ad():
    return """<h1 align="center">Миссия Колонизация Марса<p></h1>
              <h2 align="center">Человечество вырастает из детства.<br>
                                 Человечеству мала одна планета.<br>
                                 Мы сделаем обитаемыми безжизненные пока планеты.<br>
                                 И начнем с Марса!<br>
                                 Присоединяйся!</h2>"""


@app.route("/image_mars")
def image_mars():
    return f"""<title>Привет, Марс!</title>
               <h1>Жди нас, Марс!</h1>
               <img src="{url_for('static', filename='img/mars.gif')}">
               <p>Вот она какая, красная планета.</p>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.gif')}">
                    <p class="alert alert-info" role="alert">Человесество вырастает из детства.</p>
                    <p class="alert alert-warning" role="alert">Человечеству мала одна планета.</p>
                    <p class="alert alert-success" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert alert-primary" role="alert">И начнем с Марса!</p>
                    <p class="alert alert-danger" role="alert">Присоединяйся!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
