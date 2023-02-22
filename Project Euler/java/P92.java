public class P92 {
	public static void main(String... args) {
		new P92();
	}

	P92() {
		for (int i = 0; i < fin.length; ++i)
			fin[i] = -1;
		// del enunciado
		fin[44] = fin[32] = fin[13] = fin[10] = fin[1] = 1;
		fin[85] = fin[145] = fin[42] = fin[20] = fin[4] = fin[16] = fin[37] = fin[58] = fin[89] = 89;

		int total = 0;
		for (int i = 1; i < 10000000; ++i)
			if (calcularFin(i) == 89)
				++total;
		System.out.println(total);
	}

	// La máxima suma es sum(9², i=1..9) = 567
	int[] fin = new int[568];

	int calcularFin(int x) {
		int s = suma(x);
		if (fin[s] == -1)
			fin[s] = calcularFin(s);
		return fin[s];
	}

	int suma(int x) {
		int s = 0;
		while (x > 0) {
			s += (x % 10) * (x % 10);
			x /= 10;
		}
		return s;
	}
}

/*
 * A number chain is created by continuously adding the square of the digits in
 * a number to form a new number until it has been seen before.
 * 
 * For example,
 * 
 * 44 → 32 → 13 → 10 → 1 → 1
 * 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
 * 
 * Therefore any chain that arrives at 1 or 89 will become stuck in an endless
 * loop. What is most amazing is that EVERY starting number will eventually
 * arrive at 1 or 89.
 * 
 * How many starting numbers below ten million will arrive at 89?
 */