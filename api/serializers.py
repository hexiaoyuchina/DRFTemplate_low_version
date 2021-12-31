from rest_framework import serializers
from api.models import DouBan


class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DouBan
        fields = ('title', 'rating_num', 'votes', 'move_type', 'country', 'time', 'director', 'actor')

class DoubanSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)

