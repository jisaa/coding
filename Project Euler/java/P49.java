import java.util.ArrayList;

class P49 {
	public static void main(String... args) throws Exception {
		new P49();
	}

	P49() throws Exception {
		// Primos de 4 cifras
		generarPrimos(10000);
		while (primos.get(0) < 1000)
			primos.remove(0);

		for (int i = 0; i < primos.size(); ++i)
			for (int j = i + 1; j < primos.size(); ++j)
				for (int k = j + 1; k < primos.size(); ++k)
					if (sirve(primos.get(i), primos.get(j), primos.get(k)))
						System.out.println(primos.get(i) + " " + primos.get(j) + " " + primos.get(k));
	}

	// asume a < b < c
	boolean sirve(int a, int b, int c) {
		// Secuencia aritmética
		if (c - b != b - a)
			return false;
		// Permutaciones
		int[] da = new int[10], db = new int[10], dc = new int[10];
		for (int i = 0; i < 4; ++i) {
			++da[a % 10];
			a /= 10;
			++db[b % 10];
			b /= 10;
			++dc[c % 10];
			c /= 10;
		}
		for (int i = 0; i < 10; ++i) {
			if (da[i] != db[i] || da[i] != dc[i])
				return false;
		}
		return true;
	}

	ArrayList<Integer> primos = new ArrayList<Integer>();

	void generarPrimos(int max) {
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
 * The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
 * increases by 3330, is unusual in two ways: (i) each of the three terms are
 * prime, and, (ii) each of the 4-digit numbers are permutations of one another.
 * 
 * There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
 * exhibiting this property, but there is one other 4-digit increasing sequence.
 * 
 * What 12-digit number do you form by concatenating the three terms in this
 * sequence?
 * 
 */
