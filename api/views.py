from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route
from service.DoubanService import DoubanService
from api.models import DouBan
from api import serializers
from common.common import Common
# Create your views here.


class HxyViewSet(GenericViewSet, Common):
    @list_route(methods=['GET'], url_path='get_all_data', serializer_class = serializers.AllDataSerializer)
    def get_all_data(self, request):
        douban = DoubanService()
        all_res = douban.get_all_data()
        return self.drf_success_response(all_res)

    @list_route(methods=['POST'], url_path='get_douban', serializer_class = serializers.DoubanSerializer)
    def get_doouban(self, request):
        # 序列化请求数据

        obj_serializer = self.get_serializer(data=request.data)
        obj_serializer.is_valid()
        serializer_data = obj_serializer.data

        douban = DoubanService(**serializer_data)
        res = douban.get_douban()
        return self.drf_success_response(res)
