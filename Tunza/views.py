from django.shortcuts import render
from django.http import HttpResponse
from .forms import Table

# Create your views here.


def index(request):
	return render (request,'Tunza/index.html')


def gallery(request):
	return render (request,'Tunza/gallery.html')

def submit(request):
	if request.method== 'POST':
		form = Table(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Data sent')
		# return render(request, 'Tunza/contact.html', args)
		else:
			form = Table()
			args = {'form':form}
			return render(request, 'Tunza/contact.html', args)
	form = Table()
	args = {'form':form}
	return render (request,"Tunza/contact.html", args)

def about(request):
	return render (request,'Tunza/about.html')