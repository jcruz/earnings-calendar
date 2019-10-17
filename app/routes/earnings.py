from flask import Blueprint
from flask import jsonify
from flask import Response
from marshmallow import fields
from webargs.flaskparser import use_kwargs

from app.services import optionslam

blueprint = Blueprint('earnings', __name__)


@blueprint.route('/api/earnings/<stock_symbol>', methods=['GET'])
@use_kwargs({
    'last': fields.Integer(missing=1),
})
def earnings(stock_symbol: str, last: int) -> Response:
    earnings_dates = optionslam.get_earnings_dates(stock_symbol=stock_symbol, last=last)
    return jsonify(earnings_dates)
