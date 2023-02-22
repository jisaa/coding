class P17 {
	public static void main(String... args) {
		new P17();
	}

	P17() {
		String[] unidades = {
				"",
				"one",
				"two",
				"three",
				"four",
				"five",
				"six",
				"seven",
				"eight",
				"nine"
		};
		String[] diez = {
				"ten",
				"eleven",
				"twelve",
				"thirteen",
				"fourteen",
				"fifteen",
				"sixteen",
				"seventeen",
				"eighteen",
				"nineteen"
		};
		String[] decenas = {
				"",
				"",
				"twenty",
				"thirty",
				"forty",
				"fifty",
				"sixty",
				"seventy",
				"eighty",
				"ninety",
		};

		String[] centenas = {
				"onehundredand",
				"twohundredand",
				"threehundredand",
				"fourhundredand",
				"fivehundredand",
				"sixhundredand",
				"sevenhundredand",
				"eighthundredand",
				"ninehundredand",
		};
		int suma = 0;
		for (int d = 0; d < 10; ++d)
			for (int u = 0; u < 10; ++u) {
				if (d == 1)
					suma += diez[u].length();
				else
					suma += new String(decenas[d] + unidades[u]).length();
			}
		suma *= 10;
		for (String c : centenas) {
			// la centena exacta no tiene "and"
			suma += c.length() * 100 - 3;
		}
		suma += new String("onethousand").length();

		System.out.println(suma);
	}
}

/*
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 * then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 * 
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written out
 * in words, how many letters would be used?
 * 
 * NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
 * forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
 * letters. The use of "and" when writing out numbers is in compliance with
 * British usage.
 */