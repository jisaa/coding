import java.math.BigInteger;

public class P63 {
	public static void main(String... args) {
		new P63();
	}

	P63() {
		int total = 0;
		for (int i = 1; i < 200; ++i)
			total += nPotencias(i);

		System.out.println(total);
	}

	int nPotencias(int b) {
		int total = 0;
		BigInteger t = new BigInteger("" + b), t2;
		for (int e = 1; e < 40; ++e) {
			t2 = t.pow(e);
			if (t2.toString().length() == e) {
				++total;
				// System.out.println(b+"^"+e+" = "+t2.toString());
			}
		}
		return total;
	}
}

/*
 * The 5-digit number, 16807=7⁵, is also a fifth power. Similarly, the 9-digit
 * number, 134217728=8⁹, is a ninth power.
 * 
 * How many n-digit positive integers exist which are also an nth power?
 */