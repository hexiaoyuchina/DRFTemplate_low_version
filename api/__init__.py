from django.contrib.auth import authenticate, login  # d登录用户校验及登录


def api_deco(api_msg):
    def _wrapper(func):
        def deco(*args, **kwargs):
            obj = args[0]
            req = args[1]


            res = func(*args, **kwargs)

            return
        return deco
    return _wrapper


