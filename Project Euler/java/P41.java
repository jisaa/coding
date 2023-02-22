import java.math.BigInteger;
import jsc.combinatorics.Permutations;
import jsc.combinatorics.Permutation;

class P41 {
	public static void main(String... args) {
		new P41();
	}

	public P41() {
		Permutations p = new Permutations(7);
		Permutation t;
		BigInteger b;
		int i, mejor = 0;
		while (p.hasNext()) {
			t = p.nextPermutation();
			i = toInt(t.toIntArray());
			if (i % 2 == 0)
				continue;
			b = new BigInteger("" + i);
			if (esPandigital(i) && b.isProbablePrime(100)) {
				if (i > mejor)
					mejor = i;
			}
		}
		System.out.println(mejor);

	}

	public int toInt(int[] x) {
		int t = 0;
		for (int i : x) {
			t *= 10;
			t += i;
		}
		return t;
	}

	public boolean esPandigital(int x) {
		boolean[] digitos = { true, false, false, false, false, false, false, false, false, false };
		for (int i = 0; i < 7; ++i) {
			digitos[x % 10] = true;
			x /= 10;
		}
		for (int i = 1; i < 8; ++i)
			if (digitos[i] == false)
				return false;
		return true;
	}
}
