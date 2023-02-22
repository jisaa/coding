import java.util.ArrayList;

class P73 {
	public static void main(String... args) {
		new P73();
	}

	P73() {
		generarPrimos(1000000);
		long total = 0;
		for (int d = 2; d < 12001; ++d) {
			for (int n = 1; n < d; ++n) {
				if (2 * n < d && d < 3 * n && esPrimoRelativo(n, d)) {
					++total;
					// System.out.println(n+"/"+d+" = "+(double)n/d);
				}
			}
			if (d % 1000 == 0)
				System.out.println(d + ": " + total);
		}
		System.out.println();
		System.out.println(total);
	}

	// x<=y
	boolean esPrimoRelativo(int x, int y) {
		if (x == 1)
			return true;
		if (y % x == 0)
			return false;
		for (int p : primos) {
			if (x % p == 0 && y % p == 0)
				return false;
			else if (2 * p > x)
				break;
		}
		return true;
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
 * Consider the fraction, n/d, where n and d are positive integers. If n<d and
 * HCF(n,d)=1, it is called a reduced proper fraction.
 * 
 * If we list the set of reduced proper fractions for d ≤ 8 in ascending order
 * of size, we get:
 * 
 * 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
 * 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
 * 
 * It can be seen that there are 3 fractions between 1/3 and 1/2.
 * 
 * How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
 * proper fractions for d ≤ 12,000?
 */