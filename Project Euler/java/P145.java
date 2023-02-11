public class P145 {
	public static void main(String... args) {
		new P145();
	}

	P145() {
		int total = 0;
		for (long i = 1; i < 1000000000L; ++i)
			if (reversible(i))
				++total;
		System.out.println(total);
	}

	boolean reversible(long x) {
		if (x % 10 == 0)
			return false;
		// revertir
		long t = x, r = 0;
		while (t > 0) {
			r *= 10;
			r += t % 10;
			t /= 10;
		}
		// sumar
		x += r;
		// revisar que todos los dígitos sean impares
		while (x > 0) {
			if (x % 2 == 0)
				return false;
			x /= 10;
		}
		return true;
	}
}
/*
 * Some positive integers n have the property that the sum [ n + reverse(n) ]
 * consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409
 * + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904
 * are reversible. Leading zeroes are not allowed in either n or reverse(n).
 * 
 * There are 120 reversible numbers below one-thousand.
 * 
 * How many reversible numbers are there below one-billion (10⁹)?
 * 
 */