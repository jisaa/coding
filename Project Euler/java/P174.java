public class P174 {
	public static void main(String... args) {
		new P174();
	}

	public P174() {
		int[] L = new int[1000001];

		// int[] l = {32/4};
		// for(int lado : l){
		for (int lado = 2; lado < 1000000 / 4 + 1; ++lado) {
			int lt = lado - 2, usadas = lado * 4;
			++L[usadas];
			while (lt > lado % 2) {
				usadas += lt * 4;
				if (usadas < 1000001)
					++L[usadas];
				else
					break;
				lt -= 2;
			}
		}

		int total = 0;
		for (int i = 0; i < 1000001; ++i) {
			if (0 < L[i] && L[i] < 11)
				++total;
		}
		System.out.println("---> " + total);
	}
}

/*
 * We shall define a square lamina to be a square outline with a square "hole"
 * so that the shape possesses vertical and horizontal symmetry.
 * 
 * Given eight tiles it is possible to form a lamina in only one way: 3x3 square
 * with a 1x1 hole in the middle. However, using thirty-two tiles it is possible
 * to form two distinct laminae.
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
 * 
 * If t represents the number of tiles used, we shall say that t = 8 is type
 * L(1) and t = 32 is type L(2).
 * 
 * Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example,
 * N(15) = 832.
 * 
 * What is ∑ N(n) for 1 ≤ n ≤ 10?
 */
