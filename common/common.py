from rest_framework.response import Response


class Common(object):

    def drf_success_response(self, data):
        result = {
            "code": "success",
            "msg": "操作成功",
            'data': data
        }
        return Response(result)
