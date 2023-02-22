class P85 {
	public static void main(String... args) {
		new P85();
	}

	P85() {
		// se pueden poner (filasLibres+1)*(columnasLibres+1) rectángulos chicos.

		// para una grilla de n·m, m>=n por simetría
		int ancho = 1, alto = 1;
		long mejor = 1, d = 2000000;
		for (int n = 1; n < 100; ++n)
			for (int m = n; m < 100; ++m) {
				// cantidad de rectángulos de i·j
				long cantidad = 0;
				for (int i = 1; i <= n; ++i)
					for (int j = 1; j <= m; ++j) {
						cantidad += (n - i + 1) * (m - j + 1);
					}
				if (cantidad > 2000000) {
					if (cantidad - 2000000 < d) {
						d = cantidad - 2000000;
						mejor = cantidad;
						alto = n;
						ancho = m;
					}
				} else {
					if (2000000 - cantidad < d) {
						d = 2000000 - cantidad;
						mejor = cantidad;
						alto = n;
						ancho = m;
					}
				}
			}
		System.out.println(alto + "·" + ancho + " = " + (alto * ancho) + "  (" + mejor + ")");
	}
}

/*
 * By counting carefully it can be seen that a rectangular grid measuring 3 by 2
 * contains eighteen rectangles:
 * 
 * Although there exists no rectangular grid that contains exactly two million
 * rectangles, find the area of the grid with the nearest solution.
 */