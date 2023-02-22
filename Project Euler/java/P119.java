import java.util.Collections;
import java.util.ArrayList;

public class P119 {
	public static void main(String... args) {
		new P119();
	}

	P119() {
		long n;
		int s;
		ArrayList<Long> nums = new ArrayList<Long>();

		for (int base = 2; base < 150; ++base) {
			n = base;
			for (int e = 2; e < 15; ++e) {
				n *= base;
				s = sumaDigitos(n);
				if (s == base) {
					nums.add(n);
				}
			}
		}
		Collections.sort(nums);
		// for(int i=0; i<nums.size(); ++i)
		// System.out.println((i+1)+": "+nums.get(i));
		System.out.println(nums.get(29));
	}

	int sumaDigitos(long x) {
		int s = 0;
		while (x > 0) {
			s += x % 10;
			x /= 10;
		}
		return s;
	}
}

/*
 * The number 512 is interesting because it is equal to the sum of its digits
 * raised to some power: 5 + 1 + 2 = 8, and 8³ = 512. Another example of a
 * number with this property is 614656 = 28⁴.
 * 
 * We shall define a_n to be the nth term of this sequence and insist that a
 * number must contain at least two digits to have a sum.
 * 
 * You are given that a_2 = 512 and a_10 = 614656.
 * 
 * Find a_30.
 */
