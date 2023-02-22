public class P40 {
	public static void main(String... args) {
		new P40();
	}

	public P40() {
		// Funciona, pero es muy lento ~17 minutos
		String n = ".";
		int i = 0;
		while (n.length() < 1000001)
			n += ++i;
		int prod = 1;
		for (i = 100; i < 1000001; i *= 10)
			prod *= Integer.parseInt("" + n.charAt(i));
		System.out.println(prod);

	}
}

/*
 * An irrational decimal fraction is created by concatenating the positive
 * integers:
 * 
 * 0.123456789101112131415161718192021...
 * 
 * It can be seen that the 12th digit of the fractional part is 1.
 * 
 * If dn represents the nth digit of the fractional part, find the value of the
 * following expression.
 * 
 * d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
 */