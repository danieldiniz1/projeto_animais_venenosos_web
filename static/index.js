function validar() {
    var nomeanimal = document.getElementById("nomeanimal");
    var nomecientifico = document.getElementById("nomecientifico");
    var imagemurl = document.getElementById("imagemurl");
    var nivelperigo = document.getElementById("nivelperigo");

    if (nomeanimal.value == "") { // verifica se o campo NÃO foi preenchido //
        alert("Nome do animal não informado"); // se verdadeiro, emite um alerta //
        nomeanimal.focus();  //deixa o input com o focus //
        return false; // retorna a função e não olha as outras linhas
    }

    if (nomecientifico.value == "") { 
        alert("Nome científico do animal não informado"); 
        nomecientifico.focus(); 
        return false; 
    }

    if (imagemurl.value == "") { 
        alert("URL da imagem não foi informado"); 
        imagemurl.focus(); 
        return false; 
    }

    if (nivelperigo.value == "") { 
        alert("O nível de perigo não foi informado"); 
        nivelperigo.focus(); 
        return false; 
    }


}