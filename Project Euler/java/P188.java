import java.math.BigInteger;

class P188 {
	public static void main(String... args) {
		new P188();
	}

	P188() {
		int k = 1855;
		BigInteger b = new BigInteger("" + 1777);
		BigInteger e = new BigInteger("1");
		BigInteger mod = new BigInteger("100000000");
		while (k-- > 0) {
			e = b.modPow(e, mod);
		}
		System.out.println(e);
	}

	// por definición, lentísimo
	long t(long a, long k) {
		if (k == 1)
			return a;
		long e = t(a, k - 1);
		long r = 1;
		while (e-- > 0)
			r *= a;
		return r;
	}
}

/*
 * The hyperexponentiation or tetration of a number a by a positive integer b,
 * denoted by a↑↑b , is recursively defined by:
 * 
 * a↑↑1 = a,
 * a↑↑(k+1) = a^(a↑↑k).
 * 
 * Thus we have e.g. 3↑↑2 = 3³ = 27, hence 3↑↑3 = 3²⁷ = 7625597484987 and 3↑↑4
 * is roughly 103.6383346400240996*10^12.
 * 
 * Find the last 8 digits of 1777↑↑1855.
 */