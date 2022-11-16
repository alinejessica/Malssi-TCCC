from cgitb import text
from faulthandler import disable
from multiprocessing.resource_sharer import stop
from django.forms import UsersForm, ComentariosForms
from django import forms
from seuapp.models import Usuario, Comentario

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'email', 'senha', 'confirma_senha', 'tel', 'nascimento']

class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']

class Comentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario') 



    #create the forma class- caso precise este é o de antes
    #confirma_senha = forms.CharField(widget=forms.PasswordInput)
    #nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))