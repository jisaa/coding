import java.util.ArrayList;

class P70 {
	public static void main(String... args) {
		new P70();
	}

	P70() {
		generarPrimos(5000);
		System.out.println("*");

		double min = 2, t;
		int iMin = -1, f;

		for (int a = 0; a < primos.size(); ++a)
			for (int b = a + 1; b < primos.size(); ++b) {
				long x = (long) primos.get(a) * primos.get(b);
				if (x > 10000000)
					break;
				int i = (int) x;

				// cálculo de phi válido solo para x=p1*p2, con p1 y p2 primos.
				f = (primos.get(a) - 1) * (primos.get(b) - 1);
				if (!esPermutacion(i, f))
					continue;
				t = ((double) i) / ((double) f);
				if (t < min) {
					min = t;
					iMin = i;
					System.out.println(primos.get(a) + "->" + iMin + " (" + f + ") -> " + min);
				}
			}
		System.out.println();
		System.out.println("---> " + iMin + " (" + phi(iMin) + ") -> " + min);
	}

	boolean esPermutacion(int x, int y) {
		int[] dx = new int[10];
		while (x > 0) {
			++dx[(int) x % 10];
			x /= 10;
		}
		int[] dy = new int[10];
		while (y > 0) {
			++dy[(int) y % 10];
			y /= 10;
		}
		for (int i = 0; i < 10; ++i)
			if (dy[i] != dx[i])
				return false;
		return true;
	}

	int phi(int x) {
		// phi(x)=x*PI(p-1)/(PI(p)), PI=multiplicatoria, p=factor primo de x
		if (esPrimo(x))
			return x - 1;
		long phi = x;
		for (int p : primos)
			if (2 * p > x) {
				break;
			} else if (x % p == 0) {
				phi = phi * (p - 1) / p;
			}
		return (int) phi;
	}

	ArrayList<Integer> primos = new ArrayList<Integer>();

	void generarPrimos(int max) {
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
 * Euler's Totient function, φ(n) [sometimes called the phi function], is used
 * to determine the number of positive numbers less than or equal to n which are
 * relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
 * than nine and relatively prime to nine, φ(9)=6.
 * The number 1 is considered to be relatively prime to every positive number,
 * so φ(1)=1.
 * 
 * Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
 * of 79180.
 * 
 * Find the value of n, 1 < n < 10⁷, for which φ(n) is a permutation of n and
 * the ratio n/φ(n) produces a minimum.
 */