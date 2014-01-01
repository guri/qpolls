from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from Polls.models import Poll

# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {	'latest_poll_list' : latest_poll_list }
	
	#output = ', '.join([p.question for p in latest_poll_list])
	return render(request, 'polls/index.html', context)


def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk = poll_id)
	return render(request, 'polls/detail.html', {'poll' : poll})

def results(request, poll_id):
	return HttpResponse("Results Poll id : %s " % poll_id)


def vote(request, poll_id):
	#return HttpResponse(request.POST)
	poll = get_object_or_404(Poll, pk = poll_id)

	if "choice" in request.POST.keys():
		choice = get_object_or_404(poll.choice_set, pk = request.POST["choice"])

		choice.votes += 1
		choice.save()

	return render(request, 'polls/detail.html', {'poll' : poll})
