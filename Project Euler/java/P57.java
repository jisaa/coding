import java.math.BigInteger;

public class P57 {
	public static void main(String... args) {
		new P57();
	}

	P57() {
		BigInteger n = new BigInteger("3"), d = new BigInteger("2"), t;
		int i = 1, total = 0;
		while (i++ < 1000) {
			n = n.add(d); // +1
			t = d;
			d = n;
			n = t; // 1/()
			n = n.add(d); // +1
			if (n.toString().length() > d.toString().length())
				++total;
		}
		System.out.println(total);
	}
}

/*
 * It is possible to show that the square root of two can be expressed as an
 * infinite continued fraction.
 * 
 * √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
 * 
 * By expanding this for the first four iterations, we get:
 * 
 * 1 + 1/2 = 3/2 = 1.5
 * 1 + 1/(2 + 1/2) = 7/5 = 1.4
 * 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
 * 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
 * 
 * The next three expansions are 99/70, 239/169, and 577/408, but the eighth
 * expansion, 1393/985, is the first example where the number of digits in the
 * numerator exceeds the number of digits in the denominator.
 * 
 * In the first one-thousand expansions, how many fractions contain a numerator
 * with more digits than denominator?
 */