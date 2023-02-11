import jsc.combinatorics.Permutations;
import jsc.combinatorics.Permutation;

class P43 {
	public static void main(String... args) {
		new P43();
	}

	public P43() {
		Permutations p = new Permutations(10);
		Permutation t;
		long suma = 0L;
		long i;
		while (p.hasNext()) {
			t = p.nextPermutation();
			i = toInt(t.toIntArray());
			// descartar permutaciones que empiezan con 0.
			if (i > 1000000000 && cumple(i)) {
				suma += i;
			}
		}
		System.out.println("La suma es: " + suma);
	}

	private long toInt(int[] x) {
		long t = 0;
		for (int i : x) {
			t *= 10;
			if (i != 10)
				t += i;
		}
		return t;
	}

	private boolean cumple(long x) {
		String n = "" + x;
		String t = n.charAt(1) + "" + n.charAt(2) + "" + n.charAt(3);
		if (Integer.parseInt(t) % 2 != 0)
			return false;
		t = n.charAt(2) + "" + n.charAt(3) + "" + n.charAt(4);
		if (Integer.parseInt(t) % 3 != 0)
			return false;
		t = n.charAt(3) + "" + n.charAt(4) + "" + n.charAt(5);
		if (Integer.parseInt(t) % 5 != 0)
			return false;
		t = n.charAt(4) + "" + n.charAt(5) + "" + n.charAt(6);
		if (Integer.parseInt(t) % 7 != 0)
			return false;
		t = n.charAt(5) + "" + n.charAt(6) + "" + n.charAt(7);
		if (Integer.parseInt(t) % 11 != 0)
			return false;
		t = n.charAt(6) + "" + n.charAt(7) + "" + n.charAt(8);
		if (Integer.parseInt(t) % 13 != 0)
			return false;
		t = n.charAt(7) + "" + n.charAt(8) + "" + n.charAt(9);
		if (Integer.parseInt(t) % 17 != 0)
			return false;

		return true;
	}
}

/*
 * The number, 1406357289, is a 0 to 9 pandigital number because it is made up
 * of each of the digits 0 to 9 in some order, but it also has a rather
 * interesting sub-string divisibility property.
 * 
 * Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
 * the following:
 * 
 * d2d3d4=406 is divisible by 2
 * d3d4d5=063 is divisible by 3
 * d4d5d6=635 is divisible by 5
 * d5d6d7=357 is divisible by 7
 * d6d7d8=572 is divisible by 11
 * d7d8d9=728 is divisible by 13
 * d8d9d10=289 is divisible by 17
 * 
 * Find the sum of all 0 to 9 pandigital numbers with this property.
 */