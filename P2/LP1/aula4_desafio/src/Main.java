/*Defina um sistema que calcule o IMC de uma Pessoa.
Para isso, o sistema deve solicitar do usuário digite o valor do
peso e da altura.

IMC = peso/(altura * altura)

Realize esse código utilizando os conceitos de
Classes, objetos + métodos e modificadores de acesso*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Pessoa p = new Pessoa();

        System.out.println("Olá! Digite seu nome para começarmos: ");
        p.setNome(sc.next());

        System.out.println("Olá, " + p.getNome() + "!");
        System.out.println("Para calcular seu IMC vamos precisar dos seus dados de altura e peso. Digite abaixo: ");

        System.out.print("Sua altura (Ex. 1,80): ");
        p.setAltura(sc.nextDouble());

        System.out.print("Seu peso (Ex. 90,8 Kg: ");
        p.setPeso(sc.nextDouble());

        System.out.println("*****IMC*****");
        p.calcula_imc();
        p.faixas_imc();

    }
}
