import java.util.Scanner;
import java.io.File;

class P81 {
	public static void main(String... args) throws Exception {
		new P81();
	}

	public P81() throws Exception {
		Scanner s = new Scanner(new File("Project Euler/inputs/p81.in"));
		int[][] m = new int[80][80];
		for (int i = 0; i < 80; ++i)
			for (int j = 0; j < 80; ++j)
				m[i][j] = s.nextInt();

		// sumar la columna derecha y la fila de abajo
		for (int i = 78; i >= 0; --i) {
			m[i][79] += m[i + 1][79];
			m[79][i] += m[79][i + 1];
		}

		// sumar los valores intermedios
		for (int i = 78; i >= 0; --i)
			for (int j = 78; j >= 0; --j)
				m[i][j] += m[i + 1][j] < m[i][j + 1] ? m[i + 1][j] : m[i][j + 1];

		System.out.println("El camino más corto suma " + m[0][0]);
	}
}

/*
 * In the 5 by 5 matrix below, the minimal path sum from the top left to the
 * bottom right, by only moving to the right and down, is indicated in bold red
 * and is equal to 2427.
 * 
 * 
 * 131 673 234 103 18
 * 201 96 342 965 150
 * 630 803 746 422 111
 * 537 699 497 121 956
 * 805 732 524 37 331
 * 
 * 
 * Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
 * As...'), a 31K text file containing a 80 by 80 matrix, from the top left to
 * the bottom right by only moving right and down.
 * 
 */