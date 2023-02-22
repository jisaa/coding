import java.util.ArrayList;

class P71 {
	public static void main(String... args) {
		new P71();
	}

	P71() {
		generarPrimos(1000000);
		int mejorD = 8, mejorN = 1, n;
		for (int d = 2; d < 1000001; ++d) {
			if (d % 7 == 0)
				n = 3 * d / 7 - 1;
			else
				n = 3 * d / 7;
			if (d * mejorN < n * mejorD && esPrimoRelativo(n, d)) {
				mejorN = n;
				mejorD = d;
			}
		}
		System.out.println();
		System.out.println(mejorN + " / " + mejorD);
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
 * It can be seen that 2/5 is the fraction immediately to the left of 3/7.
 * 
 * By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
 * order of size, find the numerator of the fraction immediately to the left of
 * 3/7.
 */