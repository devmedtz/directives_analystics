from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from main.models import School, SchoolExamResult
from .forms import SchoolForm, SchoolExamResultForm, SchoolExamResultInlineFormSet

@login_required
def dashboard(request):
    template_name = 'admins/dashboard.html'

    context = {}

    return render(request, template_name, context)


@login_required
def create_edit_school(request, id=None):
	"""
		This is an inline formset to create a new school entry along with exams results that can have multiple occurences.
	"""
 
	user = request.user
	schools = School.objects.all()
	
	if id: 
		school = get_object_or_404(School, id=id)
		school_exam_result = SchoolExamResult.objects.filter(school=school)
		formset = SchoolExamResultInlineFormSet(instance=school)
		if school.created_by != request.user:
			return HttpResponseForbidden()
	else:
		school = School(created_by=user)
		formset = SchoolExamResultInlineFormSet(instance=school)
	
	if request.POST:
		form = SchoolForm(request.POST, request.FILES, instance=school)
		formset = SchoolExamResultInlineFormSet(request.POST,prefix='school_exam_result')
		if form.is_valid():
			school_form = form.save(commit=False)

			formset = SchoolExamResultInlineFormSet(request.POST,prefix='school_exam_result',instance=school_form)
			if formset.is_valid():
				school_form.save()
				school_exam_results = formset.save(commit=False)
				for e in school_exam_results:
					e.created_by = user
					e.save()

				messages.success(request, 'Success, School was created', extra_tags='alert alert-success')
				return redirect(to='admins:create_school')

			else: 
				messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')

		else:
			messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')
	else:
		form = SchoolForm(instance=school)
		formset = SchoolExamResultInlineFormSet(instance=school, prefix='school_exam_result')
	
	context = {
		'form': form,
		'formset': formset,
		'schools':schools
	}
	
	template_name = 'admins/create_school.html'

	return render(request, template_name, context)



# @login_required
# def create_edit_school(request, id=None):

# 	user = request.user
# 	schools = School.objects.all()

# 	if id:
# 		obj = get_object_or_404(School, id=id)
# 		if obj.created_by != user:
# 			return HttpResponseForbidden()
# 	else:
# 		obj = School(created_by=user)

# 	if request.POST:
# 		form = SchoolForm(request.POST, request.FILES, instance=obj)
		
# 		if form.is_valid():
# 			school_obj = form.save(commit=False)
# 			school_obj.created_by = user
# 			school_obj.save()
				
# 			messages.success(request, 'Success, School was created', extra_tags='alert alert-success')

# 			return redirect(to='admins:create_school')

# 		else:
# 			messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')
# 	else:
# 		form = SchoolForm(instance=obj)
	
# 	context = {
# 		'form': form,
# 		'schools':schools,
# 	}

# 	template_name = 'admins/create_school.html'

# 	return render(request, template_name, context=context)


