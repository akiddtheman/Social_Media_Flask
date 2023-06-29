from flask import Flask, render_template
from flask_restx import Api

from comment.comment_api import comment_bp
from hashtag.hashtag_api import hashtag_bp
from photo.photo_api import photo_bp
from posts.posts_api import post_bp
from user.user_api import user_bp
from swagger.test_swagger import swagger_bp
from database.models import db

# Объект Swagger
api = Api()
# Объект Flask
app = Flask(__name__)
# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)
# Регистрация сайта к Swagger
api.init_app(app)


@app.route('/')
def test_api():
    html_dexkan = render_template('test.html')
    return html_dexkan

app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(post_bp)
app.register_blueprint(user_bp)
# Swagger
app.register_blueprint(swagger_bp)

# Запуск
# app.run()




