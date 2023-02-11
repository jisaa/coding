class P205 {
	public static void main(String... args) {
		new P205();
	}

	// Fuerza bruta, generando todas las combinaciones.
	P205() {
		// 4⁹·6⁶ = 12.230.590.464
		long totalCombinaciones = 12230590464L;
		int[] d = { 1, 1, 1, 1, 1, 1, 1, 1, 1, // 9d4
				1, 1, 1, 1, 1, 1 }; // 6d6
		long n = 0;
		for (long l = 0; l < totalCombinaciones; ++l) {
			if (d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8] > d[9] + d[10] + d[11] + d[12] + d[13]
					+ d[14])
				++n;
			next(d);
		}
		System.out.printf(n + "/" + totalCombinaciones + " = %.7f\n", (double) n / totalCombinaciones);
	}

	int[] m = { 4, 4, 4, 4, 4, 4, 4, 4, 4,
			6, 6, 6, 6, 6, 6 };

	void next(int[] d) {
		for (int i = 0; i < 15; ++i) {
			if (++d[i] <= m[i])
				break;
			d[i] = 1;
		}
	}

	void print(int[] d) {
		System.out.println(d[0] + ", " + d[1] + ", " + d[2] + ", " + d[3] + ", " + d[4] + ", " + d[5] + ", " + d[6]
				+ ", " + d[7] + ", " + d[8] + " " + d[9] + ", " + d[10] + ", " + d[11] + ", " + d[12] + ", " + d[13]
				+ ", " + d[14]);
	}
}

/*
 * Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3,
 * 4.
 * Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5,
 * 6.
 * 
 * Peter and Colin roll their dice and compare totals: the highest total wins.
 * The result is a draw if the totals are equal.
 * 
 * What is the probability that Pyramidal Pete beats Cubic Colin? Give your
 * answer rounded to seven decimal places in the form 0.abcdefg
 */