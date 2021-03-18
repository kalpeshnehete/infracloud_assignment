from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shortapp.models import URL
import string,random


# Create your views here.


def home(request):
    current_site = get_current_site(request)
    return HttpResponse("<center><h1>Url Shortner<br>Please got to local:8000/shorten to shorten your url</h1></center>")

def all(request):
    allhash = URL.objects.all()
    keys=[]
    values=[]
    for d in allhash:
        keys.append(d.full_url)
    for d2 in allhash:
        values.append(d2.hash)
    dictionary = dict(zip(keys, values))
    print(dictionary)
    return JsonResponse({"success":True,"dictionary":dictionary})
    




@csrf_exempt
def short_url(request):
    long_url = request.POST.get("url")
    if URL.objects.filter(full_url=long_url).exists():
        existing_url=URL.objects.filter(full_url=long_url).values('full_url','hash')
        return JsonResponse({"success": False,"existing_url":list(existing_url)})
    else:
        hash = shortit(long_url)
        current_site = get_current_site(request)
        data = {
            "success":True,
            "id":hash,
            "link": "http://{}/{}".format(current_site,hash),
            "long_url":long_url
        }
        return JsonResponse(data)

def shortit(long_url):
    N=7
    s=string.ascii_uppercase+string.ascii_lowercase+string.digits
    url_id= ''.join(random.choices(s,k=N))
    if not URL.objects.filter(hash=url_id).exists():
        create=URL.objects.create(full_url=long_url,hash=url_id)
        return url_id
    else:
        shortit(url)


def redirector(request,hash_id=None):
    if not hash_id or hash_id is None:
        return HttpResponse("<h6>Invalid </h6>")
    if URL.objects.filter(hash=hash_id).exists():
        url=URL.objects.get(hash=hash_id)
        return redirect(url.full_url)
    else:
        return JsonResponse({"success":False})
















