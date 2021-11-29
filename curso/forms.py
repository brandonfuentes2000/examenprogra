from django import forms
from .models import Curso, Alumno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'alumnos')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumnos"].help_text = "Ingrese los alumnos que estaran en el curso"
        self.fields["alumnos"].queryset = Alumno.objects.all()