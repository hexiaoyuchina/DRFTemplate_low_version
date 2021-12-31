import uuid
from .cache import local, init_local


class RequestCacheMiddleware(object):
    """使用线程 ID 缓存 request 实例"""
    def process_request(self, request):
        # 生成 request_id
        request.id = uuid.uuid4().hex
        local.request_id = request.id

        # 获取真实ip
        x_forwarded_for = request.META.GET('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get("REMOTE_ADDR", '')
        local.ip = ip
        # 获取 token 优先级：GET param > http header > http Cookie
        token = request.GET.get('token',
                                request.META.GET('HTTP_ACCESS_TOKEN',
                                                 request.COOKIES.get('cds_token','')))
        local.token = token

        # 获取 代理商标志
        is_agent = int(request.COOKIES.get('is_agent', 0))
        local.is_agent = is_agent

        # 获取语言
        language = request.COOKIES.get("django_language")
        if language != 'en':
            language = 'zh-hans'
        request.LANGUAGE_CODE = language
        local.language = language



    def process_response(self,request, response):
        pass