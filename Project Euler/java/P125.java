import java.util.Scanner;
import java.io.File;

public class P125 {
	public static void main(String... args) throws Exception {
		new P125();
	}

	P125() throws Exception {
		// hay 19989 palíndromos bajo 10⁸
		// están precalculados (11s) en el archivo p125.in
		Scanner s = new Scanner(new File("Project Euler/inputs/p125.in"));
		long i, total = 0;
		while (s.hasNext()) {
			i = s.nextLong();
			if (esSuma(i)) {
				total += i;
			}
		}
		System.out.println(total);
	}

	boolean esSuma(long x) {
		int i, j;
		for (i = 1; i * i < x; ++i) {
			long t = i * i + (i + 1) * (i + 1);
			for (j = 2; t < x; ++j) {
				t += (i + j) * (i + j);
			}
			if (t == x)
				return true;
		}
		return false;
	}

	boolean esPalindromo(long x) {
		long t = x, r = 0;
		while (t > 0) {
			r *= 10;
			r += t % 10;
			t /= 10;
		}
		return r == x;
	}
}
/*
 * The palindromic number 595 is interesting because it can be written as the
 * sum of consecutive squares: 6² + 7² + 8² + 9² + 10² + 11² + 12².
 * 
 * There are exactly eleven palindromes below one-thousand that can be written
 * as consecutive square sums, and the sum of these palindromes is 4164. Note
 * that 1 = 0² + 1² has not been included as this problem is concerned with the
 * squares of positive integers.
 * 
 * Find the sum of all the numbers less than 10⁸ that are both palindromic and
 * can be written as the sum of consecutive squares.
 */