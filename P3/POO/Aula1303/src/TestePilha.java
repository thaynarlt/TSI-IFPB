public class TestePilha {
	public static void main(String[] args) {
		Pilha p1 = new Pilha();

		p1.empilhar("joao");
		p1.empilhar("maria");
//		p1.empilhar("jose");
//		p1.empilhar("ana");

		System.out.println(p1.topo());

		try {
			p1.desempilha();
			System.out.println(p1.topo());
			p1.desempilha();
			p1.desempilha();
		} catch (Exception e) {
			System.err.println("Deu erro!");
		}

		p1.esvaziar();

		System.out.println("Pilha esvaziada");
		System.out.println(p1.vazia());
	}
}