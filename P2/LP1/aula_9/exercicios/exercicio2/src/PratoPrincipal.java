public final class PratoPrincipal extends Refeicao implements Preparo {

    public PratoPrincipal(Dieta dieta) {
        super(dieta);
    }

    @Override
    public void preparar() {
        System.out.println("Preparando seu Prato Principal!");
    }

    @Override
    public void servir() {
        System.out.println("Servindo seu Prato Principal!");
    }

    @Override
    public void temperar() {
        System.out.println("Temperando seu Prato Principal!");
    }

    @Override
    public void esquentar() {
        System.out.println("Esquindo seu Prato Principal!");
    }

}
