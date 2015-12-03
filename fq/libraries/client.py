import foursquare
import json

from fq.models import Cities, Regions, Venues, Tips


class Client(object):

    def __init__(self):
        self.client = foursquare.Foursquare(
            client_id='LS3EXK2JJYIHUAWYNIJRO0SIMG2DAS2SBLP132BMOHYVCGL3',
            client_secret='0OJP5N4DR3FLDOFYV2HYSF0KKRBX0GDIH5OZPFL5FMJDAGVT'
        )

    def get_dict(self, near):
        fq_dict = self.client.venues.explore(params={'near': near, 'limit': 50})
        return fq_dict.get('groups', {})

    def get_city(self, id):
        city = Cities.objects.all().filter(id = id).first().city
        return city

    def get_cities(self):
        cities = Cities.objects.all()
        return cities

    def save_data_by_city(self, city):
        regions = Regions.objects.filter(cities_id_id = city)

        region_data = []
        for reg in regions:
            region_data += self.client.venues.explore(params={'near': reg.region, 'limit': 50}).get('groups', {})

        return region_data

    def get_venue_tips(self, id):
        tips = self.client.venues.tips(VENUE_ID = id, params={'limit': 500}).get('tips', {})
        # return tips['tips']['items']
        return tips

    def save_tips_by_venue(self, x, y):

        # terlalu lama, karena get.all() / pake offset [xx:xx]
        venues = Venues.objects.all()[x:y]

        result_data = []
        for venue in venues:
            data = self.get_venue_tips(venue.id)
            for d in data['items']:
                result_data.append({'id': venue.id, 'text': d['text']})
                try:
                    model = Tips(
                        text=d['text'],
                        venues_id_id=venue.id
                    )
                    model.save()
                except Exception:
                    pass

        return result_data
