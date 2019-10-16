from typing import Tuple

from flask import Flask
from flask import jsonify
from flask import Response
from werkzeug.exceptions import UnprocessableEntity

from app.routes import api

app = Flask(__name__)
app.register_blueprint(api.blueprint)


@app.errorhandler(UnprocessableEntity)
def handle_validation_error(err: UnprocessableEntity) -> Tuple[Response, int]:
    messages = getattr(err, 'data', {}).get('messages')
    if messages:
        data = {'error': 'validation_error', 'messages': messages}
    else:
        data = {'error': 'unprocessable_entity'}
    return jsonify(data), err.code
