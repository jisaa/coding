import java.util.ArrayList;

class P109 {
	public static void main(String... args) {
		new P109();
	}

	P109() {
		int t = 0;
		for (int i = 2; i < 100; ++i)
			t += nFormas(i);
		System.out.println(t);
	}

	int nFormas(int x) {
		// restar primer doble
		ArrayList<Checkout> l = new ArrayList<Checkout>();
		for (int i = 1; i < 22; ++i) {
			int r = x - 2 * (i == 21 ? 25 : i);
			if (r < 0)
				break;
			if (r == 0) {
				// System.out.println(x+" -> D"+(i==21?25:i));
				l.add(new Checkout(i, -1, -1, -1, -1));
				break;
			}
			for (int m = 1; m < 4; ++m)
				for (int a = 1; a < 22; ++a) {
					if (m == 3 && a == 21)
						break;
					if (r - m * (a == 21 ? 25 : a) == 0) {
						// System.out.println(x+" -> "+(m==1?"S":m==2?"D":"T")+(a==21?25:a)+"
						// D"+(i==21?25:i));
						Checkout c = new Checkout(i, a, -1, m, -1);
						if (!l.contains(c))
							l.add(c);
						break;
					}
					if (r - m * (a == 21 ? 25 : a) < 0)
						break;
					for (int n = 1; n < 4; ++n)
						for (int b = 1; b < 22; ++b) {
							if (n == 3 && b == 21)
								break;
							if (r - m * (a == 21 ? 25 : a) - n * (b == 21 ? 25 : b) == 0) {
								// System.out.println(x+" -> "+(n==1?"S":n==2?"D":"T")+(b==21?25:b)+"
								// "+(m==1?"S":m==2?"D":"T")+(a==21?25:a)+" D"+(i==21?25:i));
								Checkout c = new Checkout(i, a, b, m, n);
								if (!l.contains(c))
									l.add(c);
								break;
							}
							if (r - m * (a == 21 ? 25 : a) - n * (b == 21 ? 25 : b) < 0)
								break;
						}
				}
		}
		return l.size();
	}

	class Checkout {
		int i, a, b, n, m;

		public Checkout(int i, int a, int b, int n, int m) {
			this.i = i;
			this.a = a;
			this.b = b;
			this.n = n;
			this.m = m;
		}

		public boolean equals(Object otro) {
			if (i == ((Checkout) otro).i) {
				if (b == ((Checkout) otro).b && m == ((Checkout) otro).m && a == ((Checkout) otro).a
						&& n == ((Checkout) otro).n)
					return true;
				if (b == ((Checkout) otro).a && m == ((Checkout) otro).n && a == ((Checkout) otro).b
						&& n == ((Checkout) otro).m)
					return true;
			}
			return false;
		}
	}
}

/*
 * In the game of darts a player throws three darts at a target board which is
 * split into twenty equal sized sections numbered one to twenty.
 * 
 * The score of a dart is determined by the number of the region that the dart
 * lands in. A dart landing outside the red/green outer ring scores zero. The
 * black and cream regions inside this ring represent single scores. However,
 * the red/green outer ring and middle ring score double and treble scores
 * respectively.
 * 
 * At the centre of the board are two concentric circles called the bull region,
 * or bulls-eye. The outer bull is worth 25 points and the inner bull is a
 * double, worth 50 points.
 * 
 * There are many variations of rules but in the most popular game the players
 * will begin with a score 301 or 501 and the first player to reduce their
 * running total to zero is a winner. However, it is normal to play a
 * "doubles out" system, which means that the player must land a double
 * (including the double bulls-eye at the centre of the board) on their final
 * dart to win; any other dart that would reduce their running total to one or
 * lower means the score for that set of three darts is "bust".
 * 
 * When a player is able to finish on their current score it is called a
 * "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s and
 * double bull).
 * 
 * There are exactly eleven distinct ways to checkout on a score of 6:
 * 
 * D3
 * D1 D2
 * S2 D2
 * D2 D1
 * S4 D1
 * S1 S1 D2
 * S1 T1 D1
 * S1 S3 D1
 * D1 D1 D1
 * D1 S2 D1
 * S2 S2 D1
 * 
 * Note that D1 D2 is considered different to D2 D1 as they finish on different
 * doubles. However, the combination S1 T1 D1 is considered the same as T1 S1
 * D1.
 * 
 * In addition we shall not include misses in considering combinations; for
 * example, D3 is the same as 0 D3 and 0 0 D3.
 * 
 * Incredibly there are 42336 distinct ways of checking out in total.
 * 
 * How many distinct ways can a player checkout with a score less than 100?
 * 
 */