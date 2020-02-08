from django.shortcuts import render

def ehome(request):
	return render(request=request, template_name='html/eduapp/ehome.html')

def btech(request):
	return render(request=request, template_name='html/eduapp/btech.html')

def sem(request):
	return render(request=request, template_name='html/eduapp/sem.html')

def sem2(request):
	return render(request=request, template_name='html/eduapp/sem2.html')

def other(request):
	return render(request=request, template_name='html/eduapp/other.html')