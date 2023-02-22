import java.util.ArrayList;

class P32 {
	public static void main(String... args) {
		new P32();
	}

	public P32() {
		ArrayList<Long> productos = new ArrayList<Long>();
		String t;
		long p;
		for (long a = 2; a < 10000000; ++a)
			for (long b = 2; b < 10000000; ++b) {
				p = a * b;
				t = a + "" + b + "" + p;
				if (t.length() > 9)
					break;
				if (esPandigital(Integer.parseInt(t)) && !productos.contains(p))
					productos.add(p);
			}
		long suma = 0;
		for (long l : productos)
			suma += l;
		System.out.println(suma);
	}

	public boolean esPandigital(int x) {
		boolean[] digitos = { true, false, false, false, false, false, false, false, false, false };
		for (int i = 0; i < 9; ++i) {
			digitos[x % 10] = true;
			x /= 10;
		}
		for (int i = 1; i < 10; ++i)
			if (digitos[i] == false)
				return false;
		return true;
	}
}

/*
 * We shall say that an n-digit number is pandigital if it makes use of all the
 * digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
 * through 5 pandigital.
 * 
 * The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
 * multiplicand, multiplier, and product is 1 through 9 pandigital.
 * 
 * Find the sum of all products whose multiplicand/multiplier/product identity
 * can be written as a 1 through 9 pandigital.
 * HINT: Some products can be obtained in more than one way so be sure to only
 * include it once in your sum.
 */
