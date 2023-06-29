from flask import Blueprint, request
from database.postservice import get_comments_for_post, change_comment_text_db, delete_comment_db, add_comment_post_db
comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_comment(post_id: int):
    comments = get_comments_for_post(post_id)
    if comments:
        return {'status': 1, 'message': comments}
    return {'status': 0, 'message': 'Not found'}


@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['POST'])
def publish_comment(post_id: int, comment_user_id: int):
    comment_text = request.json.get('comment_text')
    add_comment_post_db(post_id, comment_user_id, comment_text)
    return {'message': 'comment posted'}


@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['PUT'])
def change_comment(comment_id: int, comment_user_id: int):
    new_text = request.json.get('new_text')
    change_comment_text_db(comment_id, new_text, comment_user_id)
    return {'message': 'Comment changed successfully'}


@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['DELETE'])
def delete_comment(comment_id: int, comment_user_id: int):
    delete_comment_db(comment_id, comment_user_id)
    return {'message': 'Comment deleted successfully'}
