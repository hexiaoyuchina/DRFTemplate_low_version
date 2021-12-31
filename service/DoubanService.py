# -*- coding:utf-8 -*-
from api.models import DouBan


class DoubanService(object):
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title', '')
        self.rating_num = kwargs.get('rating_num', '')
        self.votes = kwargs.get('votes', '')
        self.move_type = kwargs.get('move_type', '')
        self.country = kwargs.get('country', '')
        self.time = kwargs.get('time', '')
        self.director = kwargs.get('director', '')
        self.actor = kwargs.get('actor', '')

    def get_all_data(self):
        res_list = list()
        doubans = DouBan.objects.all()
        for douban in doubans:
            res_list.append({
                                "id": douban.id,
                                "title": douban.title,
                                "rating_num": douban.rating_num,
                                "votes": douban.votes,
                                "move_type": douban.move_type,
                                "country": douban.country,
                                "time": douban.time,
                                "director": douban.director,
                                "actor": douban.actor
                                    })
        return res_list

    def get_douban(self):
        douban = DouBan.objects.get(id=self.id)
        res = {
            "id": douban.id,
            "title": douban.title,
            "rating_num": douban.rating_num,
            "votes": douban.votes,
            "move_type": douban.move_type,
            "country": douban.country,
            "time": douban.time,
            "director": douban.director,
            "actor": douban.actor
        }
        return res

