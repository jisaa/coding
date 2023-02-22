class P206 {
	public static void main(String... args) {
		new P206();
	}

	public P206() {
		// Objetivo: 1_2_3_4_5_6_7_8_9_0
		// Bordes obtenidos de sqrt(1929394959697989990) y sqrt(1020304050607080900)
		long min = 1010101010, max = 1389026623;
		String test;
		// Pasos de 10, porque el resultado termina en 0.
		for (long i = min; i < max; i += 10) {
			test = "" + (i * i);
			if (test.charAt(0) == '1'
					&& test.charAt(2) == '2'
					&& test.charAt(4) == '3'
					&& test.charAt(6) == '4'
					&& test.charAt(8) == '5'
					&& test.charAt(10) == '6'
					&& test.charAt(12) == '7'
					&& test.charAt(14) == '8'
					&& test.charAt(16) == '9'
					&& test.charAt(18) == '0') {
				System.out.println(i + " al cuadrado es " + test);
				break;
			}

		}
	}
}
