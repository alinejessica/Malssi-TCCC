from django.urls import path, include
from . import views

urlpatterns = [
    path(", include('malssi.urls')"),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('dolog/',views.dolog, name="dolog"),
    path('login/', views.login, name='login'),
    path('esqueceusenha/', views.esqueceusenha, name='esqueceusenha'),
    path('altersenha/', views.altersenha, name='altersenha'),
    path('errouser/', views.errouser, name='errouser'),
    path('dologout/', views.dologout, name='dologout'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.profile, name='profile'),
    path('cometario/', views.comentario, name='comentario'),

]
