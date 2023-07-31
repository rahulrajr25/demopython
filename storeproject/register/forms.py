from django import forms
from .models import CV, Course


Gender= [('Male','Male'),('Female','Female')]
materials=[('Pencil','Pencil'),('debit','debit'),('paper','paper')]
class CVForm(forms.ModelForm):

    gender=forms.ChoiceField(choices=Gender,widget=forms.RadioSelect)
    materials=forms.MultipleChoiceField(choices=materials,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model=CV
        fields=['name','dob','age','gender','mob','email','address','department','course','purpose','materials']
        labels={'name':'Fullname','dob':'Date of Birth','age':'Age','gender':'Gender','mob':'Mobile',
                'email':'EmailID','address':'Address','department':'Department','course':'Course','purpose':'Purpose','materials':'Materials'}



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.all()