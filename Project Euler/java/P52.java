public class P52 {
	public static void main(String... args) {
		new P52();
	}

	public P52() {
		for (int i = 1;; ++i)
			if (mismosDigitos(i, 6 * i)
					&& mismosDigitos(i, 5 * i)
					&& mismosDigitos(i, 4 * i)
					&& mismosDigitos(i, 3 * i)
					&& mismosDigitos(i, 2 * i)) {
				System.out.println(i);
				System.exit(0);
			}
	}

	private boolean mismosDigitos(int a, int b) {
		int[] da = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
				db = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		while (a > 0) {
			++da[a % 10];
			a /= 10;
		}
		while (b > 0) {
			++db[b % 10];
			b /= 10;
		}
		for (int i = 0; i < 10; ++i)
			if (da[i] != db[i])
				return false;
		return true;
	}
}

/*
 * It can be seen that the number, 125874, and its double, 251748, contain
 * exactly the same digits, but in a different order.
 * 
 * Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
 * contain the same digits.
 */