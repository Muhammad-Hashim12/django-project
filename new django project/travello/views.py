from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    # dest1=Packages()
    # # name: str
    # # days: str
    # # person: str
    # # price: int
    # # desc: str
    # dest1.name='Mumbai'
    # dest1.img='package-1.jpg'
    # dest1.days='10 days'
    # dest1.person='6 members'
    # dest1.price=7000
    # dest1.desc='The place which never sleep'


    # dest2=Packages()
    # dest2.name='Bangalore'
    # dest2.img='package-2.jpg'
    # dest2.days='25 days'
    # dest2.person='10 members'
    # dest2.price=35000
    # dest2.desc='Beautiful place'

    # dest3=Packages()
    # dest3.img='package-3.jpg'
    # dest3.name='delhi'
    # dest3.days='15 days'
    # dest3.person='3members'
    # dest3.price=12000
    # dest3.desc='smallest city'

    # listt=[dest1,dest2,dest3]

    listt=Packages.objects.all()

    return render(request,'index.html',{'dests':listt,})