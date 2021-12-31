class RequestCacheMiddleware(object):
    """使用线程 ID 缓存 request 实例"""
    def process_request(self, request):
        pass
    def process_response(self,request, response):
        pass