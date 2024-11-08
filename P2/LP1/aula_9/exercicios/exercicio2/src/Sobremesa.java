public final class Sobremesa extends Refeicao {

    public Sobremesa(int mesa, String cliente, Dieta dieta) {
        super(mesa, cliente, dieta);
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
