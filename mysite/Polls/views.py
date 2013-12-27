from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from Polls.models import Poll

# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
			'latest_poll_list' : latest_poll_list,
		})
	#output = ', '.join([p.question for p in latest_poll_list])
	return HttpResponse(template.render(context))


def detail(request, poll_id):
	return HttpResponse("Poll id : %s " % poll_id)

def results(request, poll_id):
	return HttpResponse("Results Poll id : %s " % poll_id)

def vote(request, poll_id):
	return HttpResponse("Vote Poll id : %s" % poll_id)