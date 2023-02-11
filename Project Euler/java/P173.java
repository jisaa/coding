public class P173 {
	public static void main(String... args) {
		new P173();
	}

	public P173() {
		long total = 0;
		for (int lado = 2; lado < 1000000 / 4 + 1; ++lado) {
			++total;
			long lt = lado - 2, usadas = lado * 4;
			while (lt > lado % 2) {
				usadas += lt * 4;
				if (usadas < 1000001)
					++total;
				else
					break;
				lt -= 2;
			}
		}
		System.out.println("---> " + total);
	}
}

/*
 * We shall define a square lamina to be a square outline with a square "hole"
 * so that the shape possesses vertical and horizontal symmetry. For example,
 * using exactly thirty-two square tiles we can form two different square
 * laminae:
 ********* 
 * ******
 * * ******
 * * ** **
 * * ** **
 * * ******
 * * ******
 * *
 * *
 *********
 * With one-hundred tiles, and not necessarily using all of the tiles at one
 * time, it is possible to form forty-one different square laminae.
 * 
 * Using up to one million tiles how many different square laminae can be
 * formed?
 */
