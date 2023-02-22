import java.io.File;
import java.util.Scanner;

class P99 {
	public static void main(String... args) throws Exception {
		new P99();
	}

	public P99() throws Exception {
		Scanner s = new Scanner(new File("Project Euler/inputs/p99.in"));
		int linea = 1, mejorLinea = 0;
		double mejor = 0, t;

		while (s.hasNext()) {
			int base = s.nextInt();
			int exponente = s.nextInt();
			t = exponente * Math.log(base);
			if (t > mejor) {
				mejor = t;
				mejorLinea = linea;
			}
			++linea;
		}
		System.out.println("---> " + mejorLinea);
	}
}

/*
 * Comparing two numbers written in index form like 2^11 and 3^7 is not
 * difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.
 * 
 * However, confirming that 632382^518061 > 519432^525806 would be much more
 * difficult, as both numbers contain over three million digits.
 * 
 * Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text
 * file containing one thousand lines with a base/exponent pair on each line,
 * determine which line number has the greatest numerical value.
 * 
 * NOTE: The first two lines in the file represent the numbers in the example
 * given above.
 * 
 */