from django.shortcuts import render

def home(request):
	return render(request=request, template_name='html/home.html')

def phome(request):
	return render(request=request, template_name='html/personalapp/phome.html')
