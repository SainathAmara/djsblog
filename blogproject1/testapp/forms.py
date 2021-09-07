from django import forms
class EmailSentForm(forms.Form):
    Name=forms.CharField()
    Email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)


from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

from testapp.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']

from testapp.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

from django import forms
from django.core import validators
#def starts_with_d(value):
#    if (value[0]!=True):
#        raise forms.ValidationError('Name should starts with d')

class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(3)])

    def clean(self):
        print('Total form validation')
        cleaned_data=super().clean()
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['Confirmpassword']
        if inputpwd!=inputrpwd:
            raise forms.ValidationError('passwords must ba matched')
        inputname=cleaned_data['name']
        if len(inputname)<10:
            raise forms.ValidationError('Name should compulsory contains minimum 10 characters')
        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno))!=3:
            raise forms.ValidationError('Rollno should contain exactly 3 digits')
