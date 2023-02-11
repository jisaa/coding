import java.util.Scanner;
import java.io.File;

class P82 {
	public static void main(String... args) throws Exception {
		new P82();
	}

	public P82() throws Exception {
		Scanner s = new Scanner(new File("Project Euler/inputs/p82.in"));
		int[][] m = new int[80][80];
		for (int i = 0; i < 80; ++i)
			for (int j = 0; j < 80; ++j)
				m[i][j] = s.nextInt();

		// sumar las columnas de derecha a izquierda
		int c[] = new int[80]; // columna temporal
		for (int j = 78; j >= 0; --j) {
			for (int i = 0; i < 80; ++i) {
				// para la derecha.
				int min = m[i][j + 1];
				// para abajo
				if (i < 79) {
					int abajo = 0;
					for (int i1 = i + 1; i1 < 80; ++i1) {
						abajo += m[i1][j];
						if (abajo + m[i1][j + 1] < min)
							min = abajo + m[i1][j + 1];
					}
				}
				// para arriba
				if (i > 0) {
					int arriba = 0;
					for (int i1 = i - 1; i1 >= 0; --i1) {
						arriba += m[i1][j];
						if (arriba + m[i1][j + 1] < min)
							min = arriba + m[i1][j + 1];
					}
				}
				c[i] = min;
			}
			for (int i = 0; i < 80; ++i)
				m[i][j] += c[i];

		}

		int min = m[0][0];
		for (int i = 1; i < 80; ++i)
			if (m[i][0] < min)
				min = m[i][0];

		System.out.println("El camino más corto suma " + min);
	}
}

/*
 * The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
 * the left column and finishing in any cell in the right column, and only
 * moving up, down, and right, is indicated in red and bold; the sum is equal to
 * 994.
 * 
 * 
 * 131 673 234 103 18
 * 201 96 342 965 150
 * 630 53 746 422 111
 * 537 699 497 121 956
 * 55 732 524 37 331
 * 
 * 
 * Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
 * As...'), a 31K text file containing a 5 by 5 matrix, from the left column to
 * the right column.
 */