public final class Entrada extends Refeicao implements Preparo {

    public Entrada(Dieta dieta) {
        super(dieta);
    }

    @Override
    public void preparar() {
        System.out.println("Preparando sua entrada.");
    }

    @Override
    public void servir() {
        System.out.println("Sua Entrada foi servida. Bon Apettit");
    }

    @Override
    public void temperar() {
        System.out.println("Temperando...");
    }

    @Override
    public void esquentar() {
        System.out.println("Esquentando...");
    }


}
