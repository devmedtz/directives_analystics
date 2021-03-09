from django.shortcuts import render, redirect,get_object_or_404, HttpResponse, reverse
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Min, Sum, Count, Avg
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

from main.models import *
from .forms import *

@login_required
def dashboard(request):
	template_name = 'admins/dashboard.html'

	context = {}

	return render(request, template_name, context)


def get_o_exam_rank(request,school_id):

	print(school_id)

	exam_results = ExamResult.objects.filter(school=school_id, classe=4)
	
	dv1T = exam_results.aggregate(total=Sum('division_one'))
	print(dv1T['total'])
	dv2T = exam_results.aggregate(total=Sum('division_two'))
	dv3T = exam_results.aggregate(total=Sum('division_three'))
	dv4T = exam_results.aggregate(total=Sum('division_four'))
	dv0T = exam_results.aggregate(total=Sum('division_zero'))

	exam_rank = ExamRank(
		school_id = school_id,
		classe = 4,
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

	return exam_rank

def get_a_exam_rank(request,school_id):

	exam_results = ExamResult.objects.filter(school=school_id, classe=6)

	dv1T = exam_results.aggregate(total=Sum('division_one'))
	print(dv1T)
	dv2T = exam_results.aggregate(total=Sum('division_two'))
	dv3T = exam_results.aggregate(total=Sum('division_three'))
	dv4T = exam_results.aggregate(total=Sum('division_four'))
	dv0T = exam_results.aggregate(total=Sum('division_zero'))

	exam_rank = ExamRank(
		school_id = school_id,
		classe = 6,
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

	return exam_rank


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

					school_id = school_form.id
					print('school_id:',school_id)

					if e.classe == 4:
						exam_o_rank = get_o_exam_rank(request,school_id)
					elif e.classe == 6:
						exam_a_rank = get_a_exam_rank(request,school_id)

				combination = form.cleaned_data['subject_combination']
				subject = form.cleaned_data['school_subjects']
				
				if combination:
					for f in combination:
						f_obj = SubjectCombination.objects.get(name=f)
						school_form.subject_combination.add(f_obj)

				if subject:
					for f in subject:
						f_obj = SchoolSubject.objects.get(name=f)
						school_form.school_subjects.add(f_obj)

				

				

				messages.success(request, 'Success, School was created', extra_tags='alert alert-success')

				if id:
					return redirect(reverse('admins:edit_school', kwargs={'id':id}))
				else:
					return redirect(to='admins:create_school')

			else: 
				messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')

		else:
			messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')
	else:
		form = SchoolForm(instance=school)
		formset = ExamResultInlineFormSet(instance=school, prefix='all_exam_results')
	
	values = request.POST
	context = {
		'form': form,
		'formset': formset,
		'schools':schools,
		'values':values,
	}
	
	if id:
		template_name = 'admins/edit_school.html'
	else:
		template_name = 'admins/create_school.html'

	return render(request, template_name, context)

@login_required
def list_school(request):

	school_qs = School.objects.order_by('-created_at')

	context = {
		'school_qs': school_qs,
	}

	template_name = 'admins/list_school.html'

	return render(request, template_name, context)


class SubjectGroupList(LoginRequiredMixin, generic.ListView):
	model = SchoolSubject
	context_object_name = 'subjects'
	template_name = 'admins/subject_group_list.html'

# Create
class SubjectCreateView(LoginRequiredMixin, BSModalCreateView):
	template_name = 'admins/create_subject_groups.html'
	form_class = SchoolSubjectForm
	success_message = 'Success: School subject was added.'
	success_url = reverse_lazy('admins:subject_list')

# Update
class SubjectUpdateView(LoginRequiredMixin, BSModalUpdateView):
	model = SchoolSubject
	template_name = 'admins/update_subject_group.html'
	form_class = SchoolSubjectForm
	success_message = 'Success: Subject group was updated.'
	success_url = reverse_lazy('admins:subject_list')

# Delete
class SubjectDeleteView(LoginRequiredMixin, BSModalDeleteView):
	model = SchoolSubject
	template_name = 'admins/delete.html'
	context_object_name = 'obj'
	success_message = 'Success: Subject Group was deleted.'
	success_url = reverse_lazy('admins:subject_list')


class CombinationList(LoginRequiredMixin, generic.ListView):
	model = SubjectCombination
	context_object_name = 'combinations'
	template_name = 'admins/combination_list.html'

# Create
class CombinationCreateView(LoginRequiredMixin, BSModalCreateView):
	template_name = 'admins/create_combination.html'
	form_class = SubjectCombinationForm
	success_message = 'Success: combination was added.'
	success_url = reverse_lazy('admins:combination_list')

# Update
class CombinationUpdateView(LoginRequiredMixin, BSModalUpdateView):
	model = SubjectCombination
	template_name = 'admins/update_combination.html'
	form_class = SubjectCombinationForm
	success_message = 'Success: Combination was updated.'
	success_url = reverse_lazy('admins:combination_list')

# Delete
class CombinationDeleteView(LoginRequiredMixin, BSModalDeleteView):
	model = SubjectCombination
	template_name = 'admins/delete.html'
	context_object_name = 'obj'
	success_message = 'Success: Combination was deleted.'
	success_url = reverse_lazy('admins:combination_list')


class SchoolDeleteView(LoginRequiredMixin, generic.DeleteView):
	model = School
	template_name = 'admins/comfirm_delete.html'
	success_url = reverse_lazy('admins:list_school')