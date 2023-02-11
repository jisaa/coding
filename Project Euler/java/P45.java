
/*P45:
T(n)=n(n+1)/2	-> n = (sqrt(8T+1)-1)/2
P(n)=n(3n-1)/2	-> n = (sqrt(24P+1)+1)/6
H(n)=n(2n-1)/2	-> n = (sqrt(8H+1)+1/4

40755

*/
import java.lang.Math;

class P45 {
	public static void main(String... args) {
		new P45();
	}

	public P45() {
		long i = 40756;
		double r1, r2;
		while (true) {
			r1 = Math.sqrt(8 * i + 1);
			r2 = Math.sqrt(24 * i + 1);
			if ((r2 + 1) % 6 == 0 && (r1 + 1) % 4 == 0) {
				System.out.println(i);
				break;
			}
			++i;
		}
	}
}
