from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route
from service.DoubanService import DoubanService
from api.models import DouBan
from api import serializers, api_deco
from common.common import Common
# Create your views here.


class HxyViewSet(GenericViewSet, Common):
    @list_route(methods=['GET'], url_path='get_all_data')
    @api_deco("全部数据")
    def get_all_data(self, request):
        douban = DoubanService()
        all_res = douban.get_all_data()
        return self.drf_success_response(all_res)

    @list_route(methods=['POST'], url_path='get_douban', serializer_class = serializers.DoubanSerializer)
    @api_deco("详情数据")
    def get_doouban(self, request, serializer_data=None):
        # 序列化请求数据

        douban = DoubanService(**serializer_data)
        res = douban.get_douban()
        return self.drf_success_response(res)
