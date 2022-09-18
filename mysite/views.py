import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def clock(request):
    return render(request, 'blog/clock.html', {})

