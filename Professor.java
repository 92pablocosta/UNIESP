public final class Professor extends Pessoa implements FolhaPagamento{
    public CARGO cargo;
    private String especialidade;
    private double salario;

    @Override
    public String toString() {
        return "Professor{" +
                "especialidade='" + especialidade + '\'' +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                ", genero='" + genero + '\'' +
                '}';
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    public CARGO getCargo() {
        return cargo;
    }

    public void setCargo(CARGO cargo) {
        this.cargo = cargo;
    }

    @Override
    public void quemSouEu() {
        System.out.println("Sou professor");
    }

    @Override
    public void minhaAtividade() {
        System.out.println("Ensinar");

    }

    @Override
    public void calcularSalario() {


    }

    @Override
    public void aplicarBonus() {

    }
}
