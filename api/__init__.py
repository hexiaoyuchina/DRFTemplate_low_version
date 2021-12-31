from django.contrib.auth import authenticate, login  # d登录用户校验及登录


def api_deco(api_msg):
    def _wrapper(func):
        def deco(*args, **kwargs):
            obj = args[0]
            req = args[1]
            obj_serializer = None  # 不传递参数时，不会进行序列化
            if obj.serializer_class:  # 未实现get_serializer_class，默认使用self.serializer_class,list_route指定
                if req.method == 'GET':  # GET 方法传递参数
                    obj_serializer = obj.get_serializer(
                        data=req.GET)
                else:
                    obj_serializer = obj.get_serializer(
                        data=req.data)

            if not obj_serializer or obj_serializer.is_valid():  # 不指定serializer_class不会进行序列化
                if obj_serializer:
                    serializer_data = obj_serializer.data
                    kwargs['serializer_data'] = serializer_data

            res = func(*args, **kwargs)

            return res
        return deco
    return _wrapper


