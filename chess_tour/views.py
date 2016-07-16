from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def index(request):
	return HttpResponse("Hello Wrold!")