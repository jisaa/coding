class P38 {
	public static void main(String... args) {
		new P38();
	}

	public P38() {
		int mejor = 918273645;
		String t;

		for (int base = 9000; base < 10000; ++base) {
			for (int largo = 2; largo < 5; ++largo) {
				t = "";
				for (int i = 1; i <= largo; ++i) {
					t += base * i;
				}
				try {
					if (esPandigital(Integer.parseInt(t)))
						mejor = Integer.parseInt(t);
				} catch (Exception e) {
				}
			}
		}
		System.out.println(mejor);
	}

	public boolean esPandigital(int x) {
		boolean[] digitos = { true, false, false, false, false, false, false, false, false, false };
		for (int i = 0; i < 9; ++i) {
			digitos[x % 10] = true;
			x /= 10;
		}
		for (int i = 1; i < 10; ++i)
			if (digitos[i] == false)
				return false;
		return true;
	}
}

/*
 * What is the largest 1 to 9 pandigital 9-digit number that can be formed as
 * the concatenated product of an integer with (1,2, ... , n) where n > 1?
 */