import java.lang.StringBuffer;
import java.math.BigInteger;

class P55 {
	public static void main(String... args) {
		new P55();
	}

	public P55() {
		int l = 0;
		for (int i = 1; i < 10000; ++i) {
			if (esL(i)) {
				System.out.println(i);
				++l;
			}
		}
		System.out.println("Hay " + l + " numeros de Lychrel bajo 10000.");
	}

	boolean esL(int x) {
		BigInteger a = new BigInteger("" + x), b;
		for (int i = 0; i < 50; ++i) {
			b = new BigInteger(new StringBuffer(a.toString()).reverse().toString());
			a = a.add(b);
			if (a.toString().equals(new StringBuffer(a.toString()).reverse().toString()))
				return false;
		}
		return true;
	}
}
