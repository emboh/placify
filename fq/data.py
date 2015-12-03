from django.http import HttpResponse

import foursquare

client = foursquare.Foursquare(
    client_id='LS3EXK2JJYIHUAWYNIJRO0SIMG2DAS2SBLP132BMOHYVCGL3',
    client_secret='0OJP5N4DR3FLDOFYV2HYSF0KKRBX0GDIH5OZPFL5FMJDAGVT'
)

def index(request):
    c = client.venues.search(params={'near': 'Surabaya'})
    return HttpResponse(c['venues'])