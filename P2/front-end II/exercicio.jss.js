/* Obtenha dados da altura e o gênero (Masculino ou Feminino) de 15 pessoas e apresente os seguintes resultados:

- A maior e a menor altura do grupo;
- A média de altura das pessoas do gênero Masculino;
- O número de pessoas do gênero Feminino.


O aluno deve, obrigatoriamente, desenvolver a solução utilizando a linguagem Javascript. */

var pessoas = [
    { altura: 1.70, genero: 'Masculino' },
    { altura: 1.65, genero: 'Feminino' },
    { altura: 1.80, genero: 'Masculino' },
    { altura: 1.60, genero: 'Feminino' },
    { altura: 1.75, genero: 'Masculino' },
    { altura: 1.68, genero: 'Feminino' },
    { altura: 1.82, genero: 'Masculino' },
    { altura: 1.58, genero: 'Feminino' },
    { altura: 1.77, genero: 'Masculino' },
    { altura: 1.72, genero: 'Feminino' },
    { altura: 1.85, genero: 'Masculino' },
    { altura: 1.60, genero: 'Feminino' },
    { altura: 1.65, genero: 'Masculino' },
    { altura: 1.55, genero: 'Feminino' },
    { altura: 1.90, genero: 'Masculino' }
];

var maior;
var menor;
var media_altura;
var contador_M;
var contador_F;

for (let i = 0; i < pessoas.length; i+=1) {
    var altura = pessoas[i].altura;
    var genero = pessoas[i].genero;

    if (altura > maior) {
        maior = altura;
    }
    if (altura < menor) {
        menor = altura;
    }
    if (genero === 'Masculino') {
        media_altura += altura
        contador_M++;
    }else if (genero === 'Feminino') {
        contador_F++;
    }
    let mediaAlturaMasculino = somaAlturaMasculino / contMasculino;

// Apresentar resultados
console.log("A maior altura do grupo: " + maiorAltura.toFixed(2) + " metros");
console.log("A menor altura do grupo: " + menorAltura.toFixed(2) + " metros");
console.log("A média de altura das pessoas do gênero Masculino: " + mediaAlturaMasculino.toFixed(2) + " metros");
console.log("O número de pessoas do gênero Feminino: " + contFeminino);
}