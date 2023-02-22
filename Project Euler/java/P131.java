import java.lang.Math;
import java.util.ArrayList;

class P131 {
	public static void main(String... args) throws Exception {
		new P131();
	}

	public P131() throws Exception {
		generarPrimos(1000000);
		int total = 0;
		for (int p : primos) {
			if (cumple(p))
				++total;
		}
		System.out.println(total);
	}

	private long j = 1;

	boolean cumple(long x) {
		// El límite para i fue por instinto...
		for (long i = j; i < Math.sqrt(x); ++i) {
			if (Math.cbrt(i * i * i + x) % 1 == 0) {
				j = i;
				return true;
			}
		}
		return false;
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
 * There are some prime values, p, for which there exists a positive integer, n,
 * such that the expression n³+n²p=n²(n+p) is a perfect cube.
 * 
 * For example, when p = 19, 8³ + 8²×19 = 12³.
 * 
 * What is perhaps most surprising is that for each prime with this property the
 * value of n is unique, and there are only four such primes below one-hundred.
 * 
 * How many primes below one million have this remarkable property?
 */
