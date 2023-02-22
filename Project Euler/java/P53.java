import java.math.BigInteger;

public class P53 {
	public static void main(String... args) {
		new P53();
	}

	P53() {
		calcularFactoriales();
		int total = 0;
		BigInteger millon = new BigInteger("1000000");
		for (int n = 1; n < 101; ++n) {
			for (int r = 1; r < n; ++r) {
				if (fac[n].divide(fac[r].multiply(fac[n - r])).compareTo(millon) > 0)
					++total;
			}
		}
		System.out.println(total);
	}

	BigInteger[] fac = new BigInteger[101];

	void calcularFactoriales() {
		fac[0] = new BigInteger("1");
		for (int i = 1; i < 101; ++i)
			fac[i] = fac[i - 1].multiply(new BigInteger("" + i));
	}
}

/*
 * There are exactly ten ways of selecting three from five, 12345:
 * 
 * 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
 * 
 * In combinatorics, we use the notation, 5C3 = 10.
 * 
 * In general,
 * nCr = n!/(r!(n−r)!) ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
 * 
 * It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
 * 
 * How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are
 * greater than one-million?
 * 
 */