from django.shortcuts import render_to_response
from django.template import RequestContext

#Templates for homepage come from settings.py -> TEMPLATE_DIRS, that's why there's no need to import django.templates: 
#from django.template import RequestContext

import datetime

def index(request):
	now = datetime.datetime.today()
	return render_to_response('meu_blog/index.html',{'now':now},context_instance=RequestContext(request))
