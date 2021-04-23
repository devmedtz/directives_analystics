from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from django.db.models import Max, Min, Sum, Count, Avg
from bootstrap_modal_forms.generic import (
  BSModalCreateView,
)
from django.core import serializers
import json

from .models import *

from .forms import SchoolForm,SubscribeForm

from .filter import SchoolFilter


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
		print('ip1',ip)
	else:
		ip = request.META.get('REMOTE_ADDR')
		print('ip2',ip)
	return ip


def school_list(request):

	f = SchoolFilter(request.GET, queryset=School.objects.all())

	schools = f.qs

	data = serializers.serialize('json', schools, fields=('name',))
	
	request.session['schools'] = data

	search = request.GET
	request.session['search'] = search


	fee_from = request.GET.get('fee_from')
	

	search_result = SearchResult(
		gender = request.GET.get('gender'),
		accomodation_type = request.GET.get('accomodation_type'),
		class_size = request.GET.get('class_size'),
		ownership = request.GET.get('ownership'),
		school_multicultural = request.GET.get('school_multicultural'),
		school_location = request.GET.get('school_location'),
		curricular_system = request.GET.get('curricular_system'),
		fee_from = request.GET.get('fee_from'),
		fee_to = request.GET.get('fee_to'),
		no_fee = request.GET.get('charity_support'),
		region_id = request.GET.get('region'),
		district_id = request.GET.get('district'),
		ip = get_client_ip(request),
	)
	search_result.save()
	search_result.school_subjects.set(request.GET.getlist('school_subjects'))
	search_result.subject_combination.set(request.GET.getlist('subject_combination'))
	search_result.school.set(schools)
	

	for school in schools:
		sc = get_object_or_404(School, id=school.id)
		sc.search_count += 1
		sc.save()

	form_4_rank = ExamRank.objects.filter(school__in=schools.values_list('id'), classe=4).order_by('total_point')

	form_6_rank = ExamRank.objects.filter(school__in=schools.values_list('id'), classe=6).order_by('total_point')


	context = {
		'values':request.GET,
		'filter': f,
		'form_4_rank':form_4_rank,
		'form_6_rank':form_6_rank,

	}

	return render(request, 'main/school_list.html', context)



def homepage(request):

	school_qs = School.objects.order_by('-created_at')
	form = SchoolForm(use_required_attribute=False)

	if 'gender' in request.GET:
		gender = request.GET['gender']
		if gender:
			school_qs = school_qs.filter(gender=gender)

	if 'accomodation' in request.GET:
		accomodation = request.GET['accomodation']
		if accomodation:
			school_qs = school_qs.filter(accomodation_type=accomodation)

	if 'class_size' in request.GET:
		class_size = request.GET['class_size']
		if class_size:
			school_qs = school_qs.filter(class_size=class_size)

	if 'multicultural' in request.GET:
		multicultural = request.GET['multicultural']
		if multicultural:
			school_qs = school_qs.filter(school_multicultural=multicultural)

	if 'school_location' in request.GET:
		school_location = request.GET['school_location']
		if school_location:
			school_qs = school_qs.filter(school_location=school_location)

	if 'curricular_system' in request.GET:
		curricular_system = request.GET['curricular_system']
		if curricular_system:
			school_qs = school_qs.filter(curricular_system=curricular_system)

	if 'school_subjects' in request.GET:
		school_subjects = request.GET.getlist('school_subjects')
		if school_subjects:
			school_qs = school_qs.filter(school_subjects=school_subjects)

	if 'exam_4_review' in request.GET:
		exam_4_review = request.GET['exam_4_review']
		if exam_4_review:
			pass

	if 'exam_6_review' in request.GET:
		exam_6_review = request.GET['exam_6_review']
		if exam_6_review:
			pass

	if 'combination' in request.GET:
		combination = request.GET.getlist('combination')
		if combination:
			school_qs = school_qs.filter(subject_combination__in=combination)
	 
	subjects = SchoolSubject.objects.all()
	combination = SubjectCombination.objects.all()

	context = {
		'school_qs':school_qs,
		'values': request.GET,
		'subjects':subjects,
		'combinations':combination,
		'form':form,
	}

	template_name = 'main/index.html'

	
	return render(request, template_name, context)


# Create
class SubscribeCreateView(BSModalCreateView):
	template_name = 'main/subscribe_form.html'
	form_class = SubscribeForm
	success_message = 'Success: School subject was added.'
	success_url = reverse_lazy('main:school_list')

	def form_valid(self, form):
		schools = self.request.session.get('schools')
		search = self.request.session.get('search')
		ip = get_client_ip(self.request)
		form.instance.ip = ip
		form.instance.school = schools
		form.instance.search = search
		return super().form_valid(form)

