public class P31 {
	public static void main(String... args) {
		new P31();
	}

	public P31() {
		int cantidad = 0;
		for (int a = 0; a < 201; ++a) { // 1
			for (int b = 0; b < 101; ++b) { // 2
				if (a + 2 * b > 200)
					break;
				for (int c = 0; c < 41; ++c) { // 5
					if (a + 2 * b + 5 * c > 200)
						break;
					for (int d = 0; d < 21; ++d) { // 10
						if (a + 2 * b + 5 * c + 10 * d > 200)
							break;
						for (int e = 0; e < 11; ++e) { // 20
							if (a + 2 * b + 5 * c + 10 * d + 20 * e > 200)
								break;
							for (int f = 0; f < 5; ++f) { // 50
								if (a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f > 200)
									break;
								for (int g = 0; g < 3; ++g) { // 100
									if (a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g > 200)
										break;
									for (int h = 0; h < 2; ++h) { // 200
										if (a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h == 200) {
											++cantidad;
										}
									}
								}
							}
						}
					}
				}
			}
		}
		System.out.println(cantidad);
	}
}
/*
 * In England the currency is made up of pound, £, and pence, p, and there are
 * eight coins in general circulation:
 * 
 * 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
 * 
 * It is possible to make £2 in the following way:
 * 
 * 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
 * 
 * How many different ways can £2 be made using any number of coins?
 */
