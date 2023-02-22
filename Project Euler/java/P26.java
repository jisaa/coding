import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;

public class P26 {
	public static void main(String... args) {
		new P26();
	}

	public P26() {
		BigDecimal b = new BigDecimal("1"), t;
		generarPrimos(1000);
		int maxCiclo = -1, c, num = -1;
		for (int i : primos) {
			// instinto
			if (i < 900)
				continue;
			t = b.divide(new BigDecimal(i), 3000, RoundingMode.HALF_UP);

			c = largoCiclo(t.toString());
			if (c > maxCiclo) {
				maxCiclo = c;
				num = i;
			}
		}
		System.out.println("El mejor es " + num + " con un ciclo de largo " + maxCiclo);
	}

	int largoCiclo(String x) {
		// cortar 0.
		x = x.substring(2);
		// cortar ceros al final y al principio
		while (x.charAt(x.length() - 1) == '0')
			x = x.substring(0, x.length() - 1);
		while (x.charAt(0) == '0')
			x = x.substring(1);
		// Decimales finitos
		if (x.length() < 30)
			return 0;

		// Calcular ciclo
		String base = "";
		for (int largo = 1; largo < x.length() / 2; ++largo) {
			for (int i = 0; i < x.length() - 2 * largo; ++i) {
				base = x.substring(i, i + largo);
				if (x.indexOf(base, i + 1) == largo) {
					return largo;
				}
			}
		}

		return -1;
	}

	ArrayList<Integer> primos = new ArrayList<Integer>();

	private void generarPrimos(int max) {
		primos.add(2);
		for (int i = 3; i < max; i += 2) {
			boolean esPrimo = true;
			for (int p : primos)
				if (i % p == 0) {
					esPrimo = false;
					break;
				} else if (p * p > i)
					break;
			if (esPrimo)
				primos.add(i);
		}
	}
}

/*
 * A unit fraction contains 1 in the numerator. The decimal representation of
 * the unit fractions with denominators 2 to 10 are given:
 * 
 * 1/2 = 0.5
 * 1/3 = 0.(3)
 * 1/4 = 0.25
 * 1/5 = 0.2
 * 1/6 = 0.1(6)
 * 1/7 = 0.(142857)
 * 1/8 = 0.125
 * 1/9 = 0.(1)
 * 1/10= 0.1
 * 1/11= 0.(09)
 * 1/12= 0.08(3)
 * 1/13= 0.(076923)
 * 1/14= 0.0(714285)
 * 1/15= 0.0(6)
 * 1/16= 0.0625
 * 
 * Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
 * seen that 1/7 has a 6-digit recurring cycle.
 * 
 * Find the value of d < 1000 for which 1/d contains the longest recurring cycle
 * in its decimal fraction part.
 */