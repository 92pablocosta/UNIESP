public class Aluno extends Pessoa{
    private int matricula;
    private double nota1;
    private double nota2;

    @Override
    public String toString() {
        return "Aluno{" +
                "matricula=" + matricula +
                ", nota1=" + nota1 +
                ", nota=" + nota2 +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                ", genero='" + genero + '\'' +
                '}';
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public double getNota1() {
        return nota1;
    }

    public void setNota1(double nota1) {
        this.nota1 = nota1;
    }

    public double getNota2() {
        return nota2;
    }

    public void setNota2(double nota2) {
        this.nota2 = nota2;
    }

    @Override
    public void quemSouEu() {
        System.out.println("Sou Aluno");
    }

    @Override
    public void minhaAtividade() {
        System.out.println("Estudar");

    }
}
