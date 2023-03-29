from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import lxml, requests

def index(request):
    
    r = requests.get("https://www.imdb.com/chart/top/")
    f='/Users/haynescromartie/django_projects/mfdw_project/scrape/templates/scrape/index.html'
    fp=open(f)
    soup=bs(r.text,'lxml')
    
    fp.close()

        
    context={
         

    }
    return render(request,'scrape/index.html',context)

