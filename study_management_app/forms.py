from django import forms

from study_management_app.models import Study, Sponsors


class Add_study_form(forms.ModelForm):
    class Meta:
        model = Study
        fields = ('__all__')

class Sponsors_add_form(forms.ModelForm):
    class Meta:
        model = Sponsors
        fields = ('__all__')