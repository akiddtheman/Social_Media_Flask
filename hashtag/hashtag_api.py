from flask import Blueprint

hashtag_bp = Blueprint('hashtag',__name__, url_prefix='/hashtag')

# Получить хэштэг по количеству
@hashtag_bp.route('/', methods=['POST'])
def get_hashtags(size: int):
    pass

# Получить определенный хэштег по названию
@hashtag_bp.route('/string:hashtag_name', methods=['GET'])
def get_exact_hashtag(hashtag_name: str):
    pass



