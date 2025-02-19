// Escreva um código que mostre um menu para o usuário com as operações matemáticas
//básicas (soma, subtração, multiplicação e divisão). Peça para o usuário escolher uma operação
//e informar 2 valores. Faça a operação de acordo com a escolha do usuário e exiba o resultado.

package ex1;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        while (true) {
            int v1;
            int v2;
            int op;
            double resultado;

            Scanner sc = new Scanner(System.in);

            System.out.println("----Escolha uma operação e digite dois valores----");
            System.out.println("[1] Adição");
            System.out.println("[2] Subtração");
            System.out.println("[3] Multiplicação");
            System.out.println("[4] Dividir");
            System.out.println("[5] Sair");
            op = sc.nextInt();

            if (op == 5) {
                System.out.println("Saindo...");
                break;
            }

            System.out.println("Digite o primeiro valor: ");
            v1 = sc.nextInt();
            System.out.println("Digite o segundo valor: ");
            v2 = sc.nextInt();

            if (v2 == 0) {
                System.out.println("Impossível dividir por 0. Tente novamente");
            } else {
                switch (op) {
                    case 1:
                        resultado = v1 + v2;
                        System.out.println("Resultado da soma: " + resultado);
                        break;
                    case 2:
                        resultado = v1 - v2;
                        System.out.println("Resultado da subtração: " + resultado);
                        break;
                    case 3:
                        resultado = v1 * v2;
                        System.out.println("Resultado da multiplicação: " + resultado);
                        break;
                    case 4:
                        resultado = v1 / v2;
                        System.out.println("Resultado da divisão: " + resultado);
                        break;
                }
            }
        }


        System.out.println("Fim do programa");

    }
}
