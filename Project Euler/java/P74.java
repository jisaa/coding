import java.util.ArrayList;

public class P74 {
	public static void main(String... args) {
		new P74();
	}

	P74() {
		for (int i = 0; i < largoCadena.length; ++i)
			largoCadena[i] = -1;
		largoCadena[145] = 0;
		largoCadena[169] = largoCadena[363601] = largoCadena[1454] = 3;
		largoCadena[871] = largoCadena[872] = largoCadena[45361] = largoCadena[45362] = 2;

		int total = 0;
		for (int i = 1; i < 1000000; ++i) {
			if (largo(i) == 60)
				++total;
		}
		System.out.println(total);
	}

	int asdf(int[] x) {
		int t = 0;
		for (int i : x)
			if (i != -1)
				++t;
		return t;
	}

	// la mayor suma es 9!*6 = 2.177.280
	int[] largoCadena = new int[2177281];
	ArrayList<Integer> lista;

	int largo(int x) {
		int s = suma(x);
		if (largoCadena[s] == -1) {
			lista = new ArrayList<Integer>();
			lista.add(x);
			int s2 = s;
			while (!lista.contains(s2) && lista.size() < 62) {
				lista.add(s2);
				s2 = suma(s2);
			}
			largoCadena[s] = lista.size();
		}
		return largoCadena[s];
	}

	int[] f = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };

	int suma(int x) {
		int t = 0;
		while (x > 0) {
			t += f[x % 10];
			x /= 10;
		}
		return t;
	}
}
/*
 * The number 145 is well known for the property that the sum of the factorial
 * of its digits is equal to 145:
 * 
 * 1! + 4! + 5! = 1 + 24 + 120 = 145
 * 
 * Perhaps less well known is 169, in that it produces the longest chain of
 * numbers that link back to 169; it turns out that there are only three such
 * loops that exist:
 * 
 * 169 → 363601 → 1454 → 169
 * 871 → 45361 → 871
 * 872 → 45362 → 872
 * 
 * It is not difficult to prove that EVERY starting number will eventually get
 * stuck in a loop. For example,
 * 
 * 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
 * 78 → 45360 → 871 → 45361 (→ 871)
 * 540 → 145 (→ 145)
 * 
 * Starting with 69 produces a chain of five non-repeating terms, but the
 * longest non-repeating chain with a starting number below one million is sixty
 * terms.
 * 
 * How many chains, with a starting number below one million, contain exactly
 * sixty non-repeating terms?
 */