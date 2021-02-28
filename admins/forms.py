from django import forms 
from django.forms.formsets import formset_factory

from bootstrap_modal_forms.forms import BSModalModelForm

from main.models import School, ExamResult, SchoolSubject, SubjectCombination
from location.models import Region, District

class SchoolForm(forms.ModelForm):
	region = forms.ModelChoiceField(Region.objects.all(), empty_label='Select Region')
	school_subjects = forms.ModelMultipleChoiceField(SchoolSubject.objects.all(), widget=forms.CheckboxSelectMultiple())
	subject_combination = forms.ModelMultipleChoiceField(SubjectCombination.objects.all(), widget=forms.CheckboxSelectMultiple())


	class Meta:
		model = School
		exclude = ['created_at', 'modified_at', 'created_by', ]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['district'].queryset = District.objects.none()

		if 'region' in self.data:
			try:
				region_id = int(self.data.get('region'))
				self.fields['district'].queryset = District.objects.filter(region=region_id).order_by('id')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['district'].queryset = self.instance.region.district_set.order_by('id')


class ExamResultForm(forms.ModelForm):

	class Meta:
		model = ExamResult
		fields = ['year', 'classe', 'division_one', 'division_two', 'division_three', 'division_four', 'division_zero',]

ExamResultFormSet = formset_factory(ExamResultForm, extra=0)

ExamResultInlineFormSet = forms.inlineformset_factory(School, ExamResult, fields = ('id','year', 'classe', 'division_one', 'division_two', 'division_three', 'division_four', 'division_zero',), extra=1)


class SchoolSubjectForm(BSModalModelForm):

    class Meta:
        model = SchoolSubject
        fields = ['name',]


class SubjectCombinationForm(BSModalModelForm):

    class Meta:
        model = SubjectCombination
        fields = ['name',]