from django.shortcuts import render
from django.http import HttpResponse
import json

from fq.libraries.client import Client
from fq.models import Venues

import foursquare

# client = foursquare.Foursquare(
#     client_id='LS3EXK2JJYIHUAWYNIJRO0SIMG2DAS2SBLP132BMOHYVCGL3',
#     client_secret='0OJP5N4DR3FLDOFYV2HYSF0KKRBX0GDIH5OZPFL5FMJDAGVT'
# )


def index(request):
    # c = client.venues.explore(params={'near': 'Gubeng', 'limit': 50})
    # b = client.venues.explore(params={'near': 'Mulyorejo', 'limit': 50})

    # groups = c['groups']
    # groups = list(c.keys())
    # groups = json.dumps(groups, ensure_ascii=False)

    # d = c.get('groups', {})
    # e = b.get('groups', {})

    # result = d+e
    # e = vars(c.__dict__)

    c = Client()

    ##mendapatkan 1 kota
    # a = c.get_city(1)
    s = c.save_data_by_city(1)

    for group in s:
        for v in group['items']:
            try:
                model = Venues(
                    id=v['venue']['id'],
                    name=v['venue']['name'],
                    address=v['venue']['location']['address'],
                    city=v['venue']['location']['city'],
                    lat=v['venue']['location']['lat'],
                    lng=v['venue']['location']['lng'],
                    regions_id_id=1
                )
                model.save()
            except ValueError as err:
                pass
            except KeyError as err:
                pass

    return render(request, 'data/venues.html', {'groups': s})


def tips(request):

    # venue = Client()

    # result = venue.save_tips_by_venue(2000,2100)
    result = 'selesai'

    return render(request, 'data/tips.html', {'tips': result})
