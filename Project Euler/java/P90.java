public class P90 {
	public static void main(String... args) {
		new P90();
	}

	public P90() {
		int[] x = { 0, 1, 2, 3, 4, 5 }, y;

		int total = 0;
		do {
			y = copia(x);
			while (next(y)) {
				if (generaCuadrados(x, y))
					++total;
				// System.out.println(++i);
			}
		} while (next(x));
		System.out.println("--->" + total);
	}

	int[] cuadrados = { 1, 4, 9, 16, 25, 36, 49, 64, 81 };

	boolean generaCuadrados(int[] a, int[] b) {
		boolean[] generado = new boolean[9];
		for (int i = 0; i < 6; ++i)
			for (int j = 0; j < 6; ++j) {
				for (int c = 0; c < 9; ++c) {
					int x = cuadrados[c];
					if (10 * a[i] + b[j] == x
							|| 10 * b[j] + a[i] == x
							|| (a[i] == 6 && (90 + b[j] == x || 10 * b[j] + 9 == x))
							|| (b[j] == 6 && (90 + a[i] == x || 10 * a[i] + 9 == x))
							|| (a[i] == 9 && (60 + b[j] == x || 10 * b[j] + 6 == x))
							|| (b[j] == 9 && (60 + a[i] == x || 10 * a[i] + 6 == x))) {
						generado[c] = true;
					}
				}
			}
		for (int c = 0; c < 9; ++c)
			if (!generado[c])
				return false;

		return true;
	}

	int[] b = { 0, 1, 2, 3, 4, 5 }, m = { 4, 5, 6, 7, 8, 9 };

	boolean next(int[] cubo) {
		boolean[] arreglar = new boolean[6];
		for (int i = 5; i > -1; --i)
			if (++cubo[i] > m[i]) {
				arreglar[i] = true;
			} else
				break;
		int max = cubo[0];
		for (int i = 1; i < 6; ++i) {
			if (arreglar[i])
				cubo[i] = max + 1;
			if (cubo[i] > max)
				max = cubo[i];
		}
		return cubo[5] < 10;
	}

	void print(int[] x) {
		System.out.println(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + x[4] + ", " + x[5]);
	}

	int[] copia(int[] x) {
		int[] y = new int[6];
		for (int i = 0; i < 6; ++i)
			y[i] = x[i];
		return y;
	}
}

/*
 * Each of the six faces on a cube has a different digit (0 to 9) written on it;
 * the same is done to a second cube. By placing the two cubes side-by-side in
 * different positions we can form a variety of 2-digit numbers.
 * 
 * For example, the square number 64 could be formed:
 * 
 * In fact, by carefully choosing the digits on both cubes it is possible to
 * display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36,
 * 49, 64, and 81.
 * 
 * For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
 * one cube and {1, 2, 3, 4, 8, 9} on the other cube.
 * 
 * However, for this problem we shall allow the 6 or 9 to be turned upside-down
 * so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
 * for all nine square numbers to be displayed; otherwise it would be impossible
 * to obtain 09.
 * 
 * In determining a distinct arrangement we are interested in the digits on each
 * cube, not the order.
 * 
 * {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
 * {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
 * 
 * But because we are allowing 6 and 9 to be reversed, the two distinct sets in
 * the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for
 * the purpose of forming 2-digit numbers.
 * 
 * How many distinct arrangements of the two cubes allow for all of the square
 * numbers to be displayed?
 */
