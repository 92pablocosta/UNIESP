public final class Coordenador extends Pessoa implements FolhaPagamento{
    private int martricula;

    public int getMartricula() {
        return martricula;
    }

    public void setMartricula(int martricula) {
        this.martricula = martricula;
    }

    @Override
    public String toString() {
        return "Coordenador{" +
                "martricula=" + martricula +
                ", nome='" + nome + '\'' +
                ", idade=" + idade +
                ", genero='" + genero + '\'' +
                '}';
    }

    @Override
    public void quemSouEu() {
        System.out.println("Sou coordenador");
    }

    @Override
    public void minhaAtividade() {
        System.out.println("Coordenar");

    }

    @Override
    public void calcularSalario() {

    }

    @Override
    public void aplicarBonus() {

    }
}
