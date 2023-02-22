import java.util.ArrayList;

class P95 {
	public static void main(String... args) {
		new P95();
	}

	P95() {
		int max = 1000000;
		int[] sd = new int[max];
		for (int i = 2; i < max; ++i)
			sd[i] = sumDivs(i);

		// buscar cadena más larga.
		int menor = -1, largoCadena = 0;
		ArrayList<Integer> lista;
		for (int i = 2; i < max; ++i) {
			lista = new ArrayList<Integer>();
			lista.add(i);
			int t = sd[i], min = i;
			while (!lista.contains(t)) {
				lista.add(t);
				if (t < max)
					t = sd[t];
				if (t < min)
					min = t;
			}
			if (t > max || t != i)
				continue;
			if (lista.size() > largoCadena) {
				largoCadena = lista.size();
				menor = min;
			}
		}
		System.out.println("La cadena más larga tiene como menor a " + menor + " y es de largo " + largoCadena);
	}

	int sumDivs(int x) {
		int t = 1, m = x / 2;
		for (int d = 2; d < m; ++d)
			if (x % d == 0) {
				t += d + (d * d == x ? 0 : x / d);
				m = x / d;
			}
		return t;
	}
}

/*
 * The proper divisors of a number are all the divisors excluding the number
 * itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
 * sum of these divisors is equal to 28, we call it a perfect number.
 * 
 * Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
 * proper divisors of 284 is 220, forming a chain of two numbers. For this
 * reason, 220 and 284 are called an amicable pair.
 * 
 * Perhaps less well known are longer chains. For example, starting with 12496,
 * we form a chain of five numbers:
 * 
 * 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
 * 
 * Since this chain returns to its starting point, it is called an amicable
 * chain.
 * 
 * Find the smallest member of the longest amicable chain with no element
 * exceeding one million.
 */