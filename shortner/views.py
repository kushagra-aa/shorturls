from django.shortcuts import render, redirect
import uuid
from .models import Urls
from django.http import HttpResponse
# Create your views here.


def go(request, pk):
    url_details = Urls.objects.get(uuid=pk)
    return redirect(url_details.link)


def create(request):
    print('heyy1')
    if request.method == 'POST':
        print('heyy2')
        url = request.POST['link']
        print('heyy3')
        uid = str(uuid.uuid4())[:5]
        print('heyy4')
        new_url = Urls(link=url, uuid=uid)
        print('heyy5')
        new_url.save()
        print('heyy6')
        return HttpResponse(uid)


def index(request):
    return render(request, "index.html")
