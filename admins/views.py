from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Sum, Count, Avg

from datetime import datetime, timedelta

from main.models import *
from .forms import SchoolForm, ExamResultInlineFormSet, ExamResultForm

@login_required
def dashboard(request):
    template_name = 'admins/dashboard.html'

    context = {}

    return render(request, template_name, context)


def get_exam_rank(request, school_id):
	
	school_id = 4

	no_of_year = 4

	classe = 4

	start_year = (datetime.now() - timedelta(days=no_of_year*365)).year
	end_year = datetime.now().year

	exam_results = ExamResult.objects.filter(school=school_id, classe=classe, year__range=(start_year,end_year))

	dv1T = exam_results.aggregate(total=Sum('division_one'))
	dv2T = exam_results.aggregate(total=Sum('division_two'))
	dv3T = exam_results.aggregate(total=Sum('division_three'))
	dv4T = exam_results.aggregate(total=Sum('division_four'))
	dv0T = exam_results.aggregate(total=Sum('division_zero'))

	exam_rank = ExamRank(
		school_id = 4,
		dv1T = dv1T['total'],
		dv2T = dv2T['total'],
		dv3T = dv3T['total'],
		dv4T = dv4T['total'],
		dv0T = dv0T['total'],
		dv1P = dv1T['total']*5.5,
		dv2P = dv2T['total']*1.5,
		dv3P = dv3T['total']*0.25,
		dv4P = dv4T['total']*-1.5,
		dv0P = dv0T['total']*-5.5,
		total_point= (dv1T['total']*5.5)+(dv2T['total']*1.5)+(dv3T['total']*0.25)+(dv4T['total']*-1.5)+(dv0T['total']*-5.5)
	)
	exam_rank.save()

	return HttpResponse('Success')


@login_required
def create_edit_school(request, id=None):
	"""
		This is an inline formset to create a new school entry along with exams results that can have multiple occurences.
	"""
 
	user = request.user
	schools = School.objects.all()
	
	if id: 
		school = get_object_or_404(School, id=id)

		exam_result = ExamResult.objects.filter(school=school)

		formset = ExamResultInlineFormSet(instance=school)

		if school.created_by != request.user:
			return HttpResponseForbidden()
	else:
		school = School(created_by=user)
		formset = ExamResultInlineFormSet(instance=school)
	
	if request.POST:
		form = SchoolForm(request.POST, request.FILES, instance=school)
		formset = ExamResultInlineFormSet(request.POST,prefix='all_exam_results')

		if form.is_valid():
			school_form = form.save(commit=False)

			formset = ExamResultInlineFormSet(request.POST,prefix='all_exam_results',instance=school_form)
			
			if formset.is_valid():
				school_form.save()
				exam_results = formset.save(commit=False)

				for e in exam_results:
					e.created_by = user
					e.save()

				combination = form.cleaned_data['subject_combination']
				subject = form.cleaned_data['school_subjects']
				
				for f in combination:
					f_obj = SubjectCombination.objects.get(name=f)
					school_form.subject_combination.add(f_obj)

				
				for f in subject:
					f_obj = SchoolSubject.objects.get(name=f)
					school_form.school_subjects.add(f_obj)

				messages.success(request, 'Success, School was created', extra_tags='alert alert-success')
				return redirect(to='admins:create_school')

			else: 
				messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')

		else:
			messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')
	else:
		form = SchoolForm(instance=school)
		formset = ExamResultInlineFormSet(instance=school, prefix='all_exam_results')
	
	context = {
		'form': form,
		'formset': formset,
		'schools':schools
	}
	
	if id:
		template_name = 'admins/edit_school.html'
	else:
		template_name = 'admins/create_school.html'

	return render(request, template_name, context)


def list_school(request):

	school_qs = School.objects.order_by('-created_at')

	context = {
		'school_qs': school_qs,
	}

	template_name = 'admins/list_school.html'

	return render(request, template_name, context)