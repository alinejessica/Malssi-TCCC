let btn = document.querySelector ('.fa-eye')

btn.addEventListener ('click', ()=>{

let inputSenha = document.querySelector ('#senha')

if(inputSenha.getAttribute ('type') == 'password'){
  inputSenha.setAttribute ('type', 'text')
} else {

inputSenha.setAttribute('type', 'password')

 }
})

function entrar ( ){
let usuario = document.querySelector ('#usuario')
let userLabel = document.querySelector('#userLabel')

let senha = document.querySelector('#senha')
let senhaLabel = document.querySelector('#senhaLabel')

let msgError = document.querySelector('#msgError')
let listUser = []

}

let UserValid = {
    nome: '',
    user: '',
    senha: ''
}

listUser = JSON.parse(localStorage.getItem('listUser'))

listUser.forEach(element => {
    if (usuario.value == element.userCad && senha.value == element.senhaCad){
        
        UserValid = {
            nome: element.nomeCad,
            user: element.userCad,
            senha: element.senhaCad
    }

    }

});

if(usuario.value == UserValid.user && senha.value == UserValid.senha){
    alert('Deu Certo')

 } else {
    userLabel.setAttribute('style', 'color:pink')
    usuario.setAttribute('style', 'border-color:pink')
    SenhaLabel.setAttribute('style', 'color:pink')
    senha.setAttribute('style', 'border-color:pink')
    msgError.userLabel.setAttribute('style', 'color:pink')
    msgError.innerHTML = 'Usuario ou senha incorretos'
    usuario.focus()
}