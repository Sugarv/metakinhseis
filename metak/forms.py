from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import TabHolder, Tab, Div, Field

from .models import Metakinhsh


class MetakinhshForm(forms.ModelForm):
    class Meta:
        model = Metakinhsh
        fields = '__all__'
        exclude = ['person',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['egkrish'].disabled = True
        self.fields['date_from'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                },
            format="%Y-%m-%d"
            )
        self.fields['date_to'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                },
            format="%Y-%m-%d"
            )
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Αποθήκευση'))
