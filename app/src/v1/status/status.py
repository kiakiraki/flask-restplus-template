from typing import Dict, List, Tuple

from flask_restplus import Namespace, Resource, fields

ns_status = Namespace('restplus_sample/v1/status', description='ステータス確認APIのエンドポイント')

status_result_model = ns_status.model('Status check results', {
    'error_code': fields.Integer(
        required=True,
        description='Status code',
        example=200
    ),
    'message': fields.String(
        required=True,
        description='Status message',
        example='OK'
    )
})

status_model = ns_status.model('Status', {
    'status': fields.Nested(status_result_model)
})


@ns_status.route('')
class Status(Resource):
    def __get_status(self) -> Tuple[List[Dict[str, str]], int]:
        response = {
            'status': {
                'error_code': '200',
                'message': 'OK'
            }
        }
        return response, 200

    @ns_status.marshal_list_with(status_model)
    def get(self) -> Tuple[List[Dict[str, str]], int]:
        response = self.__get_status()
        return response
