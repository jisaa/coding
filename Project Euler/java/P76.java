class P76 {
	public static void main(String... args) {
		new P76();
	}

	int SUMA = 100;

	P76() {
		int[] c = new int[SUMA];
		long cantidad = 0;
		c[1] = 1;
		int s = suma(c);
		while (s != 0) {
			if (s == SUMA) {
				// System.out.print("---> "); print(c);
				++cantidad;
			}
			if (s > SUMA)
				nextBase(c);
			else
				next(c);
			s = suma(c);
		}
		System.out.println(SUMA + " -> " + cantidad);
	}

	void nextBase(int[] x) {
		for (int i = 1; i <= a; ++i)
			x[i] = 0;
		++a;
		if (a < x.length)
			++x[a];
	}

	int a = 0;

	void next(int[] x) {
		for (int i = 1; i < x.length; ++i) {
			if (++x[i] <= SUMA / i) {
				a = i;
				break;
			}
			x[i] = 0;
		}
	}

	void print(int[] x) {
		for (int i = 1; i < x.length - 1; ++i)
			System.out.printf("%2d, ", x[i]);
		System.out.printf("%2d\n", x[x.length - 1]);
	}

	int s;

	int suma(int[] c) {
		s = 0;
		for (int i = 1; i < c.length; ++i)
			s += i * c[i];
		return s;
	}
}

/*
 * It is possible to write five as a sum in exactly six different ways:
 * 
 * 4 + 1
 * 3 + 2
 * 3 + 1 + 1
 * 2 + 2 + 1
 * 2 + 1 + 1 + 1
 * 1 + 1 + 1 + 1 + 1
 * 
 * How many different ways can one hundred be written as a sum of at least two
 * positive integers?
 */