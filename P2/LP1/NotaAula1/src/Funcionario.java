import java.util.Scanner;
import java.time.LocalDate;
import java.time.Period;

public class Funcionario {

    Scanner sc = new Scanner(System.in);
    String nome;
    int dia_nascimento;
    int mes_nascimento;
    int ano_nascimento;
    double salario;

    public void informarSalario() {

        System.out.println("Informe o valor do seu salario: ");
        salario = sc.nextDouble();

    }

    public int calcularIdade() {

        System.out.println("Digite o dia do seu nascimento: ");
        dia_nascimento = sc.nextInt();

        System.out.println("Digite o mes do seu nascimento: ");
        mes_nascimento = sc.nextInt();

        System.out.println("Digite o ano do seu nascimento: ");
        ano_nascimento = sc.nextInt();

        LocalDate dataAtual = LocalDate.now();
        LocalDate dataNascimento = LocalDate.of(ano_nascimento, mes_nascimento, dia_nascimento);

        Period periodo = Period.between(dataNascimento, dataAtual);
        int idade = periodo.getYears();

        System.out.println("Sua idade é: " + idade + " anos.");

    }

    }
