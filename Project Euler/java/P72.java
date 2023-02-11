import java.util.ArrayList;

class P72 {
	public static void main(String... args) {
		new P72();
	}

	P72() {
		generarPrimos(1000000);
		long total = 1;
		for (int d = 3; d < 1000001; ++d) {
			total += phi(d);
		}
		System.out.println();
		System.out.println("---> " + total);
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

	// no funciona para el 2.
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
 * Consider the fraction, n/d, where n and d are positive integers. If n<d and
 * HCF(n,d)=1, it is called a reduced proper fraction.
 * 
 * If we list the set of reduced proper fractions for d ≤ 8, we get:
 * 
 * 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
 * 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
 * 
 * It can be seen that there are 21 elements in this set.
 * 
 * How many elements would be contained in the set of reduced proper fractions
 * for d ≤ 1,000,000?
 */