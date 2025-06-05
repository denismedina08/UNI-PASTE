public class Monitor extends Produto {
    private String modelo;
    private float tamanho;
    private int patrimonio;

    public Monitor(String nome, double preco, String modelo, float tamanho, int patrimonio) {
        super(nome, preco);
        this.modelo = modelo;
        this.tamanho = tamanho;
        this.patrimonio = patrimonio;
    }

    @Override
    public void exibirInfo() {
        super.exibirInfo();
        System.out.println("Modelo: " + modelo);
        System.out.println("Tamanho: " + tamanho+" cm");
        System.out.println("Patrimonio: " + patrimonio);
    }
}