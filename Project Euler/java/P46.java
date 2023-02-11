import java.util.ArrayList;

class P46 {
	public static void main(String... args) {
		new P46();
	}

	public P46() {
		generarPrimos(1000000);
		// el valor máximo para buscar se encontró probando.
		for (int i = 33; i < 1000000; i += 2) {
			// Saltarse los primos.
			boolean esPrimo = true;
			for (int p : primos)
				if (i % p == 0) {
					esPrimo = false;
					break;
				} else if (p * p > i)
					break;
			if (esPrimo)
				continue;
			// Revisar si se puede escribir como primo + doble de cuadrado
			boolean sePuede = false;
			for (int p : primos) {
				if (p > i)
					break;
				int c;
				for (c = 1; 2 * c * c + p < i; ++c)
					;
				if (2 * c * c + p == i) {
					sePuede = true;
					break;
				}
			}
			if (!sePuede) {
				System.out.println("---> " + i);
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
 * It was proposed by Christian Goldbach that every odd composite number can be
 * written as the sum of a prime and twice a square.
 * 
 * 9 = 7 + 2×1²
 * 15 = 7 + 2×2²
 * 21 = 3 + 2×3²
 * 25 = 7 + 2×3²
 * 27 = 19 + 2×2²
 * 33 = 31 + 2×1²
 * 
 * It turns out that the conjecture was false.
 * 
 * What is the smallest odd composite that cannot be written as the sum of a
 * prime and twice a square?
 */
