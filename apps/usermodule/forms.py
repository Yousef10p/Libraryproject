from django import forms
from .models import Student,Address,Student2
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__"
    
    name=forms.CharField(required=True,initial="",widget=forms.TextInput())
    age=forms.IntegerField(required=True,initial=0,widget=forms.NumberInput())
    
    address=forms.ModelChoiceField(queryset=Address.objects.all())


class StudentForm2(forms.ModelForm):
    class Meta:
        model=Student2
        fields="__all__"
    name=forms.CharField(required=True,initial="",widget=forms.TextInput())
    age=forms.IntegerField(required=True,initial=0,widget=forms.NumberInput())
    address=forms.ModelMultipleChoiceField(queryset=Address.objects.all(),widget=forms.CheckboxSelectMultiple())
    