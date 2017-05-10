from django import forms

class AskForm(forms.Form):
    Title = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'rows':"1", 'placeholder':"Title of the question"}), label='Title', max_length=100)
    Tags = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'rows':"1", 'placeholder':"tag1, tag2, tag3"}), label='Tags', max_length=100)
    Text = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'rows':"10", 'placeholder':"Your question print here"}),label='Text', min_length=50)

class QuestionForm(forms.Form):
    Answer = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'rows':"4", 'placeholder':"Enter your answer here"}), label='Answer', min_length=100)

class SignupForm(forms.Form):
    Login = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Login"}), label='Login', min_length=3)
    Email = forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control", 'placeholder':"Email"}), label='Email')
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password"}), label='Password', min_length=6)
    File = forms.FileField( label='File')

class LoginForm(forms.Form):
    Login = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Login"}), label='Login', min_length=3)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password"}), label='Password')
    Remember = forms.BooleanField(label='Remember')

class SettingsForm(forms.Form):
    Login = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Login"}), label='Login', min_length=3)
    Email = forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control", 'placeholder':"Email"}), label='Email')
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password"}), label='Password', min_length=6)
    File = forms.FileField( label='File')
