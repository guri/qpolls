from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("XXX")


def detail(request, poll_id):
	return HttpResponse("Poll id : %s " % poll_id)

def results(request, poll_id):
	return HttpResponse("Results Poll id : %s " % poll_id)

def vote(request, poll_id):
	return HttpResponse("Vote Poll id : %s" % poll_id)