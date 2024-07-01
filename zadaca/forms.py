from django import forms

from zadaca.models import Exhibition


class ExhibitionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExhibitionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter ' + visible.field.label

    class Meta:
        model = Exhibition
        fields = '__all__'
