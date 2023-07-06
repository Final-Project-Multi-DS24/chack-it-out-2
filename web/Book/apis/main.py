from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def index():
    # current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('main.html'))