from django.shortcuts import render


import email
from http.client import HTTPResponse
from django.http import HttpResponse

from django.shortcuts import render, redirect
from seuapp.forms import UsersForm, LoginForm
from seuapp.models import Usuario


# Create your views here.
def dologout(request):
	try:
		del request.session['uid']
		return redirect ("logout")
	except KeyError:
		pass
	return render(request, "home.html")
	

def home(request):
	profile = {}
	try:
		profile['uid'] = Usuario.objects.get(id=request.session['uid'])
		profile['custom'] = "LOGOUT"
		print(profile)
	except KeyError:
		profile['custom'] = "LOGIN"
	return render(request,'home.html', profile)

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def login(request):
	data = {}
	data['login'] = LoginForm()
	return render(request,'login.html',data)

def esqueceusenha(request):
	data = {}
	data['esqueceusenha'] = UsersForm()
	return render(request,'esqueceusenha.html',data)

def altersenha(request):
	data = {}
	data['altersenha'] = UsersForm()
	return render(request,'alterenha.html',data)

def errorLogin(request):
	data = {}
	return render(request,'errorLogin.html',data)

def errocadastro(request):
	data = {}
	data['errocadastro'] = UsersForm()
	return render(request,'errocadastro.html',data)
	
def erroemail(request):
	data = {}
	data['erroemail'] = UsersForm()
	return render(request,'erroemail.html',data)
	
def errouser(request):
	data = {}
	data['errouser'] = UsersForm()
	return render(request,'errouser.html',data)

def suceslogin(request):
	data = {}
	data['suceslogin'] = UsersForm()
	return render(request,'suceslogin.html',data)

def logout(request):
	data = {}
	return render(request,'logout.html',data)

def docad(request):
	tabela = Usuario.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in tabela:
		if form['usuario'].data == c.usuario :
			erro ="Mensagem de erro"
	if form.is_valid() and erro == '':
		form.save()
	return render(login)


def dolog(request):
	if request.method == "POST":
		try:
			u = Usuario.objects.get(usuario=request.POST['usuario'])
		except:
			return redirect("errorLogin")
		print(u.usuario)
		if u.senha == request.POST['senha']:
			request.session['uid'] = u.id
			return redirect('home')
		else:
			return redirect("errorLogin")
	else: 
		return redirect ('login')




def profile(request):
	profile = {}
	try:
		profile['perfil']= UsersForm(instance=Usuario.objects.get(id=request.session['uid']))
		return render(request,'profile.html', profile)
	except:
		return HttpResponse("Você não está logado")


def do_update(request):
	form= Usuario.objects.get(id=request.session['uid'])
	form.usuario = request.POST['usuario']
	form.nome = request.POST['nome']
	form.sobrenome = request.POST['sobrenome']
	form.senha = request.POST['senha']
	form.save()
	return redirect('home')




def comentario(request):
	data ={}
	if request.method == 'POST':
		c = Comentario(usuario=Usuario.object.get(id=request.session 'uid'), comentario=request.POST['comentario'])
		c.save()
		return redirect ('comentario')

	else: 
		data['form'] = ComentariosForm()
		data['history'] =Comentario.objects.filter(usuario=request.session['uid'])
		print(data['history'])
	    return render(request, 'comentario.html', data)

def edit_coment(request, id):
	c = Comentario.objects.get(id=id) #model-está ouando no banco
	f = ComentariosForm(instance=c)   #form
	return render(request, 'comentario.html', {'form':f})