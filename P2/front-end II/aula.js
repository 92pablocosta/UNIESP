<<<<<<< HEAD
var aluno = "Raíssa";
var nota = 10;


function somar() {

    console.log(aluno);
    var nota1=10;
    var nota2=8;
    var total= nota1+nota2;
    return total;

}

// após essa linha a variavel total é excluida pois é escopo local e não total. diferente da variavel de aluno. para imprimir
//O que ta fora, consegue usar dentro, o que ta dentro não consegue usar fora;

console.log(somar())

function somar2() {
    var nota1=10;
    var nota2=8;
    var total= nota1+nota2; 
    let mensagem;
    
    if (total >= 18) {
        mensagem = "Maior que 18"; 
        console.log("fulano");
    } else {
        mensagem = "Menor que 18";
    }
    console.log(mensagem);
// Ja esse if é um bloco. Ele não está preocupado com a identação, ele vai agrupar para executar sob determinada condição.
    // var só tem valor local e global.
    // let usa no bloco
    //var dentro do bloco vai ignorar o contexto mais funciona.     

}

somar2(); // assim ele imprime o que ta dentro do bloco, sem definir a função (que seria undefined)


// null: difernete de branco, diferente de undefined = porém todos são false; 
//tipos --> undefined, null, number, string, boolean, array, object, function;
// Se não atribuir valor a variavel ela vai ser undefined.

=======
var aluno = "Raíssa";
var nota = 10;


function somar() {

    console.log(aluno);
    var nota1=10;
    var nota2=8;
    var total= nota1+nota2;
    return total;

}

// após essa linha a variavel total é excluida pois é escopo local e não total. diferente da variavel de aluno. para imprimir
//O que ta fora, consegue usar dentro, o que ta dentro não consegue usar fora;

console.log(somar())

function somar2() {
    var nota1=10;
    var nota2=8;
    var total= nota1+nota2; 
    let mensagem;
    
    if (total >= 18) {
        mensagem = "Maior que 18"; 
        console.log("fulano");
    } else {
        mensagem = "Menor que 18";
    }
    console.log(mensagem);
// Ja esse if é um bloco. Ele não está preocupado com a identação, ele vai agrupar para executar sob determinada condição.
    // var só tem valor local e global.
    // let usa no bloco
    //var dentro do bloco vai ignorar o contexto mais funciona.     

}

somar2(); // assim ele imprime o que ta dentro do bloco, sem definir a função (que seria undefined)


// null: difernete de branco, diferente de undefined = porém todos são false; 
//tipos --> undefined, null, number, string, boolean, array, object, function;
// Se não atribuir valor a variavel ela vai ser undefined.

>>>>>>> master
console.log(somar2());