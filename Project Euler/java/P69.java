import java.util.ArrayList;

class P69 {
	public static void main(String... args) {
		new P69();
	}

	public P69() {
		generarPrimos(1000000);

		double max = 0, t;
		int iMax = 0;

		for (int i = 2; i < 1000001; ++i) {
			t = (double) i / phi(i);
			if (t > max) {
				max = t;
				iMax = i;
			}
		}
		System.out.println(iMax + " -> " + max);
	}

	public int phi(int x) {
		// x * PI(p-1) / (PI(p))
		int phi = x;
		ArrayList<Integer> divisores = new ArrayList<Integer>();
		for (int p : primos)
			if (p * p > x) {
				break;
			} else if (x % p == 0) {
				divisores.add(p);
			}
		for (int i : divisores) {
			phi *= (i - 1);
			phi /= i;
		}
		return phi;
	}

	ArrayList<Integer> primos = new ArrayList<Integer>();

	private void generarPrimos(int max) {
		primos.add(2);
		for (int i = 3; i < max; i += 2) {
			boolean esPrimo = true;
			for (int p : primos)
				if (p * p > i) {
					break;
				} else if (i % p == 0) {
					esPrimo = false;
					break;
				}
			if (esPrimo)
				primos.add(i);
		}
	}
}

/*
 * Euler's Totient function, φ(n) [sometimes called the phi function], is used
 * to determine the number of numbers less than n which are relatively prime to
 * n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
 * relatively prime to nine, φ(9)=6.
 * n Relatively Prime φ(n) n/φ(n)
 * 2 1 1 2
 * 3 1,2 2 1.5
 * 4 1,3 2 2
 * 5 1,2,3,4 4 1.25
 * 6 1,5 2 3
 * 7 1,2,3,4,5,6 6 1.1666...
 * 8 1,3,5,7 4 2
 * 9 1,2,4,5,7,8 6 1.5
 * 10 1,3,7,9 4 2.5
 * 
 * It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
 * 
 * Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
 */