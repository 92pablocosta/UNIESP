public final class Sobremesa extends Refeicao {

    public Sobremesa(Dieta dieta) {
        super(dieta);
    }

    @Override
    public void preparar() {
        System.out.println("Preparando Sobremesa...");
    }

    @Override
    public void servir() {
        System.out.println("Servindo Sobremesa...");
    }


}
