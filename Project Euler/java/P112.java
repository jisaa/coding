public class P112 {
	public static void main(String... args) {
		new P112();
	}

	P112() {
		double porcentaje = 0;
		int b = 0, i;

		for (i = 100; porcentaje < .99; ++i) {
			if (esBouncy(i))
				++b;
			porcentaje = (double) b / i;
		}
		System.out.println(i - 1);
	}

	boolean esBouncy(int x) {
		if (x < 100)
			return false;
		String t = "" + x;
		// creciente al principio
		int i = 1;
		while (t.charAt(i - 1) == t.charAt(i)) {
			if (++i == t.length())
				return false;
		}
		if (t.charAt(i - 1) < t.charAt(i)) {
			for (; i < t.length(); ++i)
				if (t.charAt(i - 1) > t.charAt(i))
					return true;
		} else { // decreciente al principio
			for (; i < t.length(); ++i)
				if (t.charAt(i - 1) < t.charAt(i))
					return true;
		}
		return false;
	}
}

/*
 * Working from left-to-right if no digit is exceeded by the digit to its left
 * it is called an increasing number; for example, 134468.
 * 
 * Similarly if no digit is exceeded by the digit to its right it is called a
 * decreasing number; for example, 66420.
 * 
 * We shall call a positive integer that is neither increasing nor decreasing a
 * "bouncy" number; for example, 155349.
 * 
 * Clearly there cannot be any bouncy numbers below one-hundred, but just over
 * half of the numbers below one-thousand (525) are bouncy. In fact, the least
 * number for which the proportion of bouncy numbers first reaches 50% is 538.
 * 
 * Surprisingly, bouncy numbers become more and more common and by the time we
 * reach 21780 the proportion of bouncy numbers is equal to 90%.
 * 
 * Find the least number for which the proportion of bouncy numbers is exactly
 * 99%.
 */
