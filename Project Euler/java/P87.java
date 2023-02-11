import java.util.ArrayList;

final class P87 {
	public static void main(String... args) {
		new P87();
	}
	P87() {
		generarPrimos(10000);

		int[] bases = { 0, 0, 0 };
		boolean[] es = new boolean[50000000];
		int total = 1; // se va a saltar 2²+2³+2⁴
		while (next(bases)) {
			long p = p(bases);
			if (p < 50000000L) {
				if (!es[(int) p]) {
					es[(int) p] = true;
					++total;
				}
			} else {
				nextBase(bases);
			}
		}
		System.out.println(total);
	}

	void nextBase(int[] x) {
		for (int i = 0; i <= a; ++i)
			x[i] = primos.size() - 1;
		++a;
	}

	int a = 0;

	boolean next(int[] b) {
		for (int i = 0; i < b.length; ++i) {
			if (++b[i] < primos.size()) {
				a = i;
				return true;
			}
			b[i] = 0;
		}
		return false;
	}

	long p(int[] b) {
		return (long) primos.get(b[0]) * primos.get(b[0])
				+ (long) primos.get(b[1]) * primos.get(b[1]) * primos.get(b[1])
				+ (long) primos.get(b[2]) * primos.get(b[2]) * primos.get(b[2]) * primos.get(b[2]);
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
 * The smallest number expressible as the sum of a prime square, prime cube, and
 * prime fourth power is 28. In fact, there are exactly four numbers below fifty
 * that can be expressed in such a way:
 * 
 * 28 = 2² + 2³ + 2⁴
 * 33 = 3² + 2³ + 2⁴
 * 49 = 5² + 2³ + 2⁴
 * 47 = 2² + 3³ + 2⁴
 * 
 * How many numbers below fifty million can be expressed as the sum of a prime
 * square, prime cube, and prime fourth power?
 */
