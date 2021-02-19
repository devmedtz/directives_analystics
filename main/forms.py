from django import forms
from django.forms import RadioSelect


class HorizontalRadioSelect(RadioSelect):
    template_name = 'admin/horizontal_radios.html'
    option_template_name = 'admin/horizontal_option.html'


GENDER = (
    ('Boys', 'Boys'),
    ('Girls', 'Girls'),
    ('Co-ed/boys and girls', 'Co-ed/boys and girls'),
)

class FilterForm(forms.Form):
    gender = forms.ChoiceField(choices=GENDER, label='test', widget=HorizontalRadioSelect())