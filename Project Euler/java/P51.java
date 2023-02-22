import java.util.ArrayList;

class P51 {
	public static void main(String... args) {
		new P51();
	}

	P51() {
		int max = 1000000;
		generarPrimos(max);
		for (int p : primos) {
			if (generaPrimos(p)) {
				System.out.println("---> " + p);
				break;
			}
		}
	}

	boolean generaPrimos(int x) {
		boolean[] m = new boolean[("" + x).length()];
		int max = 0;
		while (next(m)) {
			// revisar que todos los dígitos a reeplazar sean iguales
			boolean sonIguales = true;
			char dx = 0;
			for (int i = 0; i < m.length; ++i) {
				if (m[i]) {
					if (dx == 0)
						dx = ("" + x).charAt(i);
					else if (dx != ("" + x).charAt(i)) {
						sonIguales = false;
						// break;
					}
				}
			}
			if (!sonIguales)
				continue;

			int nPrimos = 0;
			for (int d = 0; d < 10; ++d) {
				int t = x, r = 0, p = 1;
				for (int i = 0; i < m.length; ++i) {
					if (m[m.length - 1 - i])
						r += d * p;
					else
						r += (t % 10) * p;
					t /= 10;
					p *= 10;
				}
				if (r > p / 10 && esPrimo(r)) {
					++nPrimos;
				}
			}
			if (nPrimos > max)
				max = nPrimos;
		}
		return max == 8;
	}

	boolean next(boolean[] m) {
		for (int i = 0; i < m.length; ++i) {
			m[i] = !m[i];
			if (m[i])
				break;
		}
		boolean quedan = false;
		for (boolean b : m) {
			if (!b) {
				quedan = true;
				break;
			}
		}
		return quedan;
	}

	boolean esPrimo(int x) {
		for (int p : primos)
			if (x % p == 0)
				return false;
			else if (p * p > x)
				break;
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
 * By replacing the 1st digit of *3, it turns out that six of the nine possible
 * values: 13, 23, 43, 53, 73, and 83, are all prime.
 * 
 * By replacing the 3rd and 4th digits of 56**3 with the same digit, this
 * 5-digit number is the first example having seven primes among the ten
 * generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
 * 56773, and 56993. Consequently 56003, being the first member of this family,
 * is the smallest prime with this property.
 * 
 * Find the smallest prime which, by replacing part of the number (not
 * necessarily adjacent digits) with the same digit, is part of an eight prime
 * value family.
 */
