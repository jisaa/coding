class P94 {
	public static void main(String... args) {
		new P94();
	}

	P94() {
		long total = 0;
		for (long i = 3; 3 * i + 1 < 1000000000L; i += 2) {
			// lados i, i, i+1
			if (areaEntera(i + 1, i)) {
				total += 3 * i + 1;
				// System.out.println(i+" "+(i+1));
			}
			// lados i, i, i-1
			if (areaEntera(i - 1, i)) {
				total += 3 * i - 1;
				// System.out.println(i+" "+(i-1));
			}
		}
		System.out.println(total);
	}

	double a;
	long x;

	boolean areaEntera(long base, long ladoRepetido) {
		a = Math.sqrt(ladoRepetido * ladoRepetido - base * base / 4);
		x = (long) a;
		return x * x == ladoRepetido * ladoRepetido - base * base / 4 && (x % 2 == 0 || base % 4 == 0);
	}

	double area(double base, double ladoRepetido) {
		return (base / 2) * Math.sqrt(ladoRepetido * ladoRepetido - base * base / 4);
	}
}

/*
 * It is easily proved that no equilateral triangle exists with integral length
 * sides and integral area. However, the almost equilateral triangle 5-5-6 has
 * an area of 12 square units.
 * 
 * We shall define an almost equilateral triangle to be a triangle for which two
 * sides are equal and the third differs by no more than one unit.
 * 
 * Find the sum of the perimeters of all almost equilateral triangles with
 * integral side lengths and area and whose perimeters do not exceed one billion
 * (1,000,000,000).
 */