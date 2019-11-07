from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #titulo=_("Mi título molón")
    #template = loader.get_template('home/index.html')
    #context = {'titulo': titulo}
    #return HttpResponse(template.render(context, request))
    return HttpResponse("Index")
def otra(request):
    #titulo=_("Mi título molón")
    #template = loader.get_template('home/index.html')
    #context = {'titulo': titulo}
    #return HttpResponse(template.render(context, request))
    return HttpResponse("Otra")

def detail(request,n):
    #template = loader.get_template('home/detail.html')
    #context={
    #    'n':n,
    #    'param_post': request.POST,
    #}
    #return HttpResponse(template.render(context, request))
    return HttpResponse("Detail")