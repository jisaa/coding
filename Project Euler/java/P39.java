public class P39 {
	public static void main(String... args) {
		new P39();
	}

	public P39() {
		int nSoluciones = 0, mejorPerimetro = 0;
		for (int perimetro = 3; perimetro < 1001; ++perimetro) {
			int n = 0;
			for (int a = 1; a < perimetro / 2; ++a) {
				for (int b = a; b < perimetro - a; ++b) {
					int c = perimetro - a - b;
					if (a * a + b * b == c * c && ++n > nSoluciones) {
						nSoluciones = n;
						mejorPerimetro = perimetro;
					}
				}
			}
		}
		System.out.println(mejorPerimetro);
	}
}
/*
 * If p is the perimeter of a right angle triangle with integral length sides,
 * {a,b,c}, there are exactly three solutions for p = 120.
 * 
 * {20,48,52}, {24,45,51}, {30,40,50}
 * 
 * For which value of p ≤ 1000, is the number of solutions maximised?
 */
