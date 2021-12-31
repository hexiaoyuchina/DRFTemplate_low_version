from rest_framework.response import Response


class Common(object):

    def drf_success_response(self, data):
        result = {
            "code": "success",
            "msg": "操作成功",
            'data': data
        }

        res = Response(result)
        res.set_cookie("cookie_flag", 1)
        return res
