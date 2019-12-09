from django.shortcuts import render
from django.http import Http404, HttpRequest
from .models import *
from .forms import *
from django.core.mail import send_mail

	###List Cars By Category###
def list_cars_by_category(request, category_name):
	cat_all = Category.objects.all()
	if category_name:
		category = Category.objects.get(name = category_name)
		cars = Car.objects.filter(category = category)
		template = 'main/list_cars_by_category.html'
		context = {'cat_all' : cat_all, 'category' : category, 'cars' : cars}
		return render(request, template, context)

	###Main Page###
def home(request):
	queryset = Car.objects.all()
	cat_all = Category.objects.all()
	context = {"car_list" : queryset, 'cat_all' : cat_all,}
	return render(request, "main/index.html", context)

	###Contact Page###
def contacts(request):
	cat_all = Category.objects.all()


	return render(request, "main/contact.html", {'cat_all' : cat_all})

	###Car_detail###
def car_detail(request, name):
	cat_all = Category.objects.all()
	car_detail = Car.objects.get(name = name)
	template = 'main/detail.html'
	context = {'car_detail' : car_detail, 'cat_all' : cat_all}
	return render(request, template, context)


def page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name',]
		message = form.cleaned_data['message',]
		subject = form.cleaned_data['subject',]
		email = form.cleaned_data['email',]
		form.save()
		recipients = ['info@example.com']
	if email:
		recipients.append(subject)

	send_mail(name, message, subject, recipients)
	cat_all = Category.objects.all()
	context = {'cat_all' : cat_all, 'form' : form}
	return render(request, 'main/includes/page.html', context)


	###Service###
def service(request):
	cat_all = Category.objects.all()
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data['EMAIL']
		form.save()
	context = {'cat_all' : cat_all, 'form' : form}
	return render(request, 'main/service.html', context)
