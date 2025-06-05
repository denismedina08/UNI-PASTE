public class Main {
    public static void main(String[] args) {
        Produto celular = new Celular("Iphone", 999.9, 3213412, "Apple", true);
        Produto monitor = new Monitor("Monitor TI", 259.99, "Inspiron", 90, 909120);

        System.out.println("Informações do Celular:");
        celular.exibirInfo();

        System.out.println("\nInformações da Monitor:");
        monitor.exibirInfo();
    }
}