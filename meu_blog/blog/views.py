from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Artigo

def list_of_articles(request):
	artigos = Artigo.objects.all()
	return render_to_response('blog/list_of_articles.html',
		locals(), context_instance=RequestContext(request)
		#{'artigos':artigos}
		
	)

def article(request,artigo_id):
	artigo = Artigo.objects.get(id=artigo_id)
	return render_to_response('blog/artigo.html',locals())


#def index(request):
# 	return HttpResponse("It works! new_version")
