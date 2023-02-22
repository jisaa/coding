import java.math.BigInteger;

public class P56 {
	public static void main(String... args) {
		new P56();
	}

	public P56() {
		BigInteger x, y;
		int sum = 0, t;
		for (int a = 2; a < 100; ++a) {
			x = new BigInteger("" + a);
			for (int b = 2; b < 100; ++b) {
				y = x.pow(b);
				t = sumarDigitos(y);
				if (t > sum)
					sum = t;
			}
		}
		System.out.println(sum);
	}

	private int sumarDigitos(BigInteger x) {
		String t = x.toString();
		int suma = 0;
		for (int i = 0; i < t.length(); ++i)
			suma += Integer.parseInt("" + t.charAt(i));
		return suma;
	}
}

/*
 * A googol (10100) is a massive number: one followed by one-hundred zeros;
 * 100100 is almost unimaginably large: one followed by two-hundred zeros.
 * Despite their size, the sum of the digits in each number is only 1.
 * 
 * Considering natural numbers of the form, ab, where a, b < 100, what is the
 * maximum digital sum?
 * 
 */