from django.shortcuts import render
from django.http import HttpResponse
from Polls.models import Poll

# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {	'latest_poll_list' : latest_poll_list }
	
	#output = ', '.join([p.question for p in latest_poll_list])
	return render(request, 'polls/index.html', context)


def detail(request, poll_id):
	return HttpResponse("Poll id : %s " % poll_id)

def results(request, poll_id):
	return HttpResponse("Results Poll id : %s " % poll_id)

def vote(request, poll_id):
	return HttpResponse("Vote Poll id : %s" % poll_id)