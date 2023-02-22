class P62 {
	public static void main(String... args) {
		new P62();
	}

	P62() {
		for (int largo = 2; largo < 15; ++largo) {
			// rellenar con todos los cubos de 'largo' dígitos
			long[] cubos = generarCubos(largo);
			for (int i = 0; i < cubos.length; ++i) {
				int nPermutaciones = 0;
				for (int j = i + 1; j < cubos.length; ++j) {
					try {
						if (esPermutacion(cubos[i], cubos[j]))
							++nPermutaciones;
					} catch (Exception e) {
						System.out.println(i + ", " + j);
						System.out.println(cubos[i] + ", " + cubos[j]);
					}
				}
				if (nPermutaciones == 4) {
					System.out.println("---> " + cubos[i]);
					System.exit(0);
				}
			}
		}
	}

	void print(long[] x) {
		for (int i = 0; i < x.length - 1; ++i)
			System.out.print(x[i] + ", ");
		System.out.println(x[x.length - 1]);
		System.out.println();
	}

	long[] generarCubos(int largo) {
		int t = largo;
		long max = 1;
		while (t-- > 0)
			max *= 10;
		long min = max / 10 - 1;
		int n = 0;
		long[] cubos = new long[4];
		for (long i = 2; i * i * i < max; ++i) {
			if (i * i * i > min) {
				// Si es necesario, agrandar el arreglo de cubos
				if (n == cubos.length) {
					long[] temp = cubos;
					cubos = new long[2 * n];
					for (int j = 0; j < n; ++j)
						cubos[j] = temp[j];
				}
				cubos[n++] = i * i * i;
			}
		}
		// Truncar el arreglo de cubos para que no hayan posiciones vacías.
		if (n < cubos.length) {
			long[] temp = cubos;
			cubos = new long[n];
			for (int j = 0; j < n; ++j)
				cubos[j] = temp[j];
		}
		return cubos;
	}

	boolean esPermutacion(long x, long y) {
		int[] dx = new int[10];
		while (x > 0) {
			++dx[(int) (x % 10)];
			x /= 10;
		}
		int[] dy = new int[10];
		while (y > 0) {
			++dy[(int) (y % 10)];
			y /= 10;
		}
		for (int i = 0; i < 10; ++i)
			if (dy[i] != dx[i])
				return false;
		return true;
	}
}

/*
 * The cube, 41.063.625 (345³), can be permuted to produce two other cubes:
 * 56.623.104 (384³) and 66.430.125 (405³). In fact, 41.063.625 is the smallest
 * cube which has exactly three permutations of its digits which are also cube.
 * 
 * Find the smallest cube for which exactly five permutations of its digits are
 * cube.
 */