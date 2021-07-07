function validar() {
    var nomeanimal = document.getElementById("nomeanimal")
    var nomecientifico = document.getElementById("nomecientifico")
    var imagemurl = document.getElementById("imagemurl")

    if (nomeanimal.value == "") { // verifica se o campo NÃO foi preenchido //
        alert("Nome do animal não informado"); // se verdadeiro, emite um alerta //
        nomeanimal.focus();  //deixa o input com o focus //
        return; // retorna a função e não olha as outras linhas
    }

    if (nomecientifico.value == "") { // verifica se o campo NÃO foi preenchido //
        alert("Nome científico do animal não informado"); // se verdadeiro, emite um alerta //
        nomecientifico.focus(); // deixa o input com o focus //
        return; // retorna a função e não olha as outras linhas
    }

    if (imagemurl.value == "") { // verifica se o campo NÃO foi preenchido //
        alert("URL da imagem não foi informado"); // se verdadeiro, emite um alerta //
        imagemurl.focus(); // deixa o input com o focus //
        return; // retorna a função e não olha as outras linhas
    }
}