from http import HTTPStatus

from flask import Flask, request
from flask_restful import Resource, Api

from models import Handphone

app = Flask(__name__)
api = Api(app)

class Recommendation(Resource):

    def post(self):
        criteria = request.get_json()
        validCriteria = ['Brand', 'Reputasi', 'Antutu Score', 'Batery', 'Harga', 'Ukuran Layar']
        handphone = Handphone()

        if not criteria:
            return 'criteria is empty', HTTPStatus.BAD_REQUEST.value

        if not all([v in validCriteria for v in criteria]):
            return 'criteria is not found', HTTPStatus.NOT_FOUND.value

        recommendations = handphone.get_recs(criteria)

        return {
            'alternatif': recommendations
        }, HTTPStatus.OK.value


api.add_resource(Recommendation, '/recommendation')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
