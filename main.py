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


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета перетендента</h1>
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="astronaut_form" method="post">
                                    <input type="text" name="surname" placeholder="Введите фамилию" class="form-control">
                                    <input type="text" name="name" placeholder="Введите имя" class="form-control"><br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="selectEducation">Какое у вас образование?</label>
                                        <select class="form-control" id="selectEducation" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее профессиональное</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="jobs">Какие у Вас есть профессии?</label><br>
                                        <input type="checkbox" name="jobs" value="job1">
                                        <label for="jobs">инженер-исследователь</label><br>
                                        <input type="checkbox" name="jobs" value="job2">
                                        <label for="jobs">пилот</label><br>
                                        <input type="checkbox" name="jobs" value="job3">
                                        <label for="jobs">строитель</label><br>
                                        <input type="checkbox" name="jobs" value="job4">
                                        <label for="jobs">экзобиолог</label><br>
                                        <input type="checkbox" name="jobs" value="job5">
                                        <label for="jobs">врач</label><br>
                                        <input type="checkbox" name="jobs" value="job6">
                                        <label for="jobs">инженер по терраформированию</label><br>
                                        <input type="checkbox" name="jobs" value="job7">
                                        <label for="jobs">климатолог</label><br>
                                        <input type="checkbox" name="jobs" value="job8">
                                        <label for="jobs">специалист по радиационной защите</label><br>
                                        <input type="checkbox" name="jobs" value="job9">
                                        <label for="jobs">астрогеолог</label><br>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="reason">Почему Вы хотите принять участе в миссии</label>
                                        <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form["surname"])
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["education"])
        print(request.form.getlist('jobs'))
        print(request.form["sex"])
        print(request.form["reason"])
        print(request.form["file"])
        print(request.form["accept"])
        return "Форма отправлена"


@app.route("/choice/<planet>")
def choice(planet):
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
                    <h1>Моё предложение: {planet}<p></h1>
                    <p class="alert alert-info" role="alert">Эта планета близка к земле;</p>
                    <p class="alert alert-warning" role="alert">На ней много необходимых ресурсов;</p>
                    <p class="alert alert-success" role="alert">На ней есть вода и атмосфера;</p>
                    <p class="alert alert-primary" role="alert">На ней есть небольшое магнитное поле;</p>
                    <p class="alert alert-danger" role="alert">Наконец, она просто красива!</p>
                  </body>
                </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
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
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <p class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</p>
                    <p>составляет {rating}!</p>
                    <p class="alert alert-warning" role="alert">Желаем удачи!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
