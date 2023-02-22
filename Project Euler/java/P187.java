import java.util.ArrayList;

class P187 {
	public static void main(String... args) {
		new P187();
	}

	P187() {
		generarPrimos(50000000);
		int total = 0;
		for (int i = 0; i < primos.size(); ++i) {
			for (int j = i; j < primos.size(); ++j) {
				long t = (long) primos.get(i) * primos.get(j);
				if (t < 100000000)
					++total;
				else
					break;
			}
		}
		System.out.println("--> " + total);
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

	boolean esPrimo(int x) {
		for (int p : primos)
			if (x % p == 0)
				return false;
			else if (p * p > x)
				break;
		return true;
	}
}

/*
 * A composite is a number containing at least two prime factors. For example,
 * 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
 * 
 * There are ten composites below thirty containing precisely two, not
 * necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
 * 
 * How many composite integers, n < 10⁸, have precisely two, not necessarily
 * distinct, prime factors?
 */