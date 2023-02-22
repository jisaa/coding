import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class P98 {
	public static void main(String... args) throws FileNotFoundException {
		new P98();
	}

	P98() throws FileNotFoundException {
		generarCuadrados();
		Scanner s = new Scanner(new File("Project Euler/inputs/p98.in"));
		// El largo máximo es 14
		// La mayor cantidad es 343 para largo=4
		String[][] lista = new String[14][343];
		int[] cantidades = new int[14];
		while (s.hasNext()) {
			String t = s.next();
			lista[t.length() - 1][cantidades[t.length() - 1]++] = t;
		}

		// para cada lista, partiendo de la más larga
		for (int i = 13; i >= 0; --i) {
			int mayor = 0;
			for (int j = 0; j < cantidades[i]; ++j) {
				for (int k = j + 1; k < cantidades[i]; ++k)
					if (esAnagrama(lista[i][j], lista[i][k])) {
						int c = mayorCuadrado(lista[i][j], lista[i][k]);
						if (c > mayor)
							mayor = c;
					}
			}
			if (mayor > 0) {
				System.out.println("--->" + mayor);
				break;
			}
		}
		s.close();
	}

	int mayorCuadrado(String x, String y) {
		for (int i = 0; i < nCuadrados[x.length() - 1]; ++i) {
			int c = cuadradosPorLargo[x.length() - 1][i];
			if (!esPosible(x, c))
				continue;
			int t = 0;
			for (int j = 0; j < y.length(); ++j) {
				t *= 10;
				t += conversion[y.charAt(j) - 'A'];
			}
			for (int cx : cuadradosPorLargo[x.length() - 1])
				if (cx == t)
					return cx > c ? cx : c;
				else if (cx > t)
					break;
		}
		return -1;
	}

	// Revisa si el String se puede convertir en el cuadrado c
	int[] conversion;

	boolean esPosible(String x, int c) {
		conversion = new int[26];
		for (int i = 0; i < 26; ++i)
			conversion[i] = -1;
		int t = c;
		for (int i = x.length() - 1; i >= 0; --i) {
			for (int p : conversion)
				if (p == t % 10)
					return false;
			conversion[x.charAt(i) - 'A'] = t % 10;
			t /= 10;
		}
		t = 0;
		for (int i = 0; i < x.length(); ++i) {
			t *= 10;
			t += conversion[x.charAt(i) - 'A'];
		}
		return t == c;
	}

	// Hay 31622 cuadrados con largo menor a 10
	// El anagrama más largo encontrado tiene largo 9
	int[][] cuadradosPorLargo = new int[9][21623];
	int[] nCuadrados = new int[9];

	void generarCuadrados() {
		int max = 10, n = 0;
		for (int i = 0; i < 31622; ++i) {
			int c = i * i;
			if (c >= max) {
				max *= 10;
				++n;
			}
			cuadradosPorLargo[n][nCuadrados[n]++] = c;
		}
	}

	// Asume que son del mismo largo y que son solo mayúsculas
	boolean esAnagrama(String x, String y) {
		int[] letras = new int[26];

		for (int i = 0; i < x.length(); ++i) {
			++letras[x.charAt(i) - 'A'];
			--letras[y.charAt(i) - 'A'];
		}
		for (int i : letras)
			if (i != 0)
				return false;
		return true;
	}
}

/*
 * By replacing each of the letters in the word CARE with 1, 2, 9, and 6
 * respectively, we form a square number: 1296 = 36². What is remarkable is
 * that, by using the same digital substitutions, the anagram, RACE, also forms
 * a square number: 9216 = 96². We shall call CARE (and RACE) a square anagram
 * word pair and specify further that leading zeroes are not permitted, neither
 * may a different letter have the same digital value as another letter.
 * 
 * Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
 * containing nearly two-thousand common English words, find all the square
 * anagram word pairs (a palindromic word is NOT considered to be an anagram of
 * itself).
 * 
 * What is the largest square number formed by any member of such a pair?
 * 
 * NOTE: All anagrams formed must be contained in the given text file.
 */
