import java.util.ArrayList;

class P47 {
	public static void main(String... args) {
		new P47();
	}

	public P47() {
		generarPrimos(1000000);
		// el valor máximo para buscar se encontró probando.
		for (int i = 10; i < 1000000; ++i) {
			int n1 = 0, n2 = 0, n3 = 0, n4 = 0;
			for (int p : primos) {
				if (2 * p > i + 3)
					break;
				if (i % p == 0)
					++n1;
				if ((i + 1) % p == 0)
					++n2;
				if ((i + 2) % p == 0)
					++n3;
				if ((i + 3) % p == 0)
					++n4;
				if (n1 > 3 && n2 > 3 && n3 > 3 && n4 > 3)
					break;
			}
			if (n1 > 3 && n2 > 3 && n3 > 3 && n4 > 3) {
				System.out.println("----> " + i);
				break;
			}
		}
	}

	ArrayList<Integer> primos = new ArrayList<Integer>();

	private void generarPrimos(int max) {
		primos.add(2);
		for (int i = 3; i < max; i += 2) {
			boolean esPrimo = true;
			for (int p : primos)
				if (i % p == 0) {
					esPrimo = false;
					break;
				} else if (p * p > i)
					break;
			if (esPrimo)
				primos.add(i);
		}
	}
}

/*
 * The first two consecutive numbers to have two distinct prime factors are:
 * 
 * 14 = 2 × 7
 * 15 = 3 × 5
 * 
 * The first three consecutive numbers to have three distinct prime factors are:
 * 
 * 644 = 2² × 7 × 23
 * 645 = 3 × 5 × 43
 * 646 = 2 × 17 × 19.
 * 
 * Find the first four consecutive integers to have four distinct primes
 * factors. What is the first of these numbers?
 */
