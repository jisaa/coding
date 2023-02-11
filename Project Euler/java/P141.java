class P141 {
	public static void main(String... args) {
		new P141();
	}

	P141() {
		long suma = 0, n = 0;
		for (long i = 3; i < 1000000; ++i) {
			n = i * i;
			for (long d = 1; d < i; ++d) {
				if (esProgresivo(d, n % d, n / d)) {
					suma += n;
					System.out.printf("%12d, %6d, %6d, %6d\n", n, d, n / d, n % d);
				}
			}
		}
		System.out.println(n + " ---> " + suma);
	}

	double t;

	boolean esProgresivo(double x, double y, double z) {
		// ordenar
		if (y < x) {
			t = x;
			x = y;
			y = t;
		}
		if (z < y) {
			t = z;
			z = y;
			y = t;
			if (y < x) {
				t = x;
				x = y;
				y = t;
			}
		}
		// ahora x<=y<=z
		return x / y == y / z;
	}
}

/*
 * A positive integer, n, is divided by d and the quotient and remainder are q
 * and r respectively. In addition d, q, and r are consecutive positive integer
 * terms in a geometric sequence, but not necessarily in that order.
 * 
 * For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be
 * seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio
 * 3/2).
 * We will call such numbers, n, progressive.
 * 
 * Some progressive numbers, such as 9 and 10404 = 102², happen to also be
 * perfect squares.
 * The sum of all progressive perfect squares below one hundred thousand is
 * 124657.
 * 
 * Find the sum of all progressive perfect squares below one trillion (10¹²).
 */