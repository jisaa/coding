import java.math.BigInteger;

class P37 {
	public static void main(String... args) {
		new P37();
	}

	public P37() {
		int nTruncables = 0;
		BigInteger a, total = new BigInteger("0");
		for (int i = 23; nTruncables < 11; i += 2) {
			a = new BigInteger("" + i);
			if (a.isProbablePrime(100) && esTruncable(a)) {
				total = total.add(a);
				++nTruncables;
				System.out.println(nTruncables + ":\t" + a.toString());
			}
		}
		System.out.println("La suma es: " + total.toString());
	}

	private boolean esTruncable(BigInteger x) {
		String t = x.toString();
		BigInteger b;
		while (t.length() > 1) {
			t = t.substring(1);
			b = new BigInteger(t);
			if (!b.isProbablePrime(100))
				return false;
		}
		t = x.toString();
		while (t.length() > 1) {
			t = t.substring(0, t.length() - 1);
			b = new BigInteger(t);
			if (!b.isProbablePrime(100))
				return false;
		}
		return true;
	}
}
/*
 * The number 3797 has an interesting property. Being prime itself, it is
 * possible to continuously remove digits from left to right, and remain prime
 * at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
 * left: 3797, 379, 37, and 3.
 * 
 * Find the sum of the only eleven primes that are both truncatable from left to
 * right and right to left.
 * 
 * NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
 */