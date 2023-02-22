import java.util.ArrayList;

public class P50 {
	public static void main(String... args) {
		new P50();
	}

	public P50() {
		generarPrimos(1000000);
		int largoSuma = 0, primo = 0;
		for (int i = 0; i < primos.size(); ++i) {
			int suma = 0, largoTemp = 0;
			for (int j = i; j < primos.size(); ++j) {
				suma += primos.get(j);
				++largoTemp;
				if (suma > 1000000)
					break;
				if (largoTemp > largoSuma && primos.contains(suma)) {
					largoSuma = largoTemp;
					primo = suma;
				}
			}
		}
		System.out.println("El primo " + primo + " se obtiene sumando " + largoSuma + " primos.");
	}

	ArrayList<Integer> primos = new ArrayList<Integer>();

	private void generarPrimos(int max) {
		primos.add(2);
		for (int i = 3; i < max; i += 2) {
			boolean esPrimo = true;
			for (int j = 0; primos.get(j) * primos.get(j) <= i; ++j)
				if (i % primos.get(j) == 0) {
					esPrimo = false;
					break;
				}
			if (esPrimo)
				primos.add(i);
		}
	}

}
/*
 * The prime 41, can be written as the sum of six consecutive primes:
 * 41 = 2 + 3 + 5 + 7 + 11 + 13
 * 
 * This is the longest sum of consecutive primes that adds to a prime below
 * one-hundred.
 * 
 * The longest sum of consecutive primes below one-thousand that adds to a
 * prime, contains 21 terms, and is equal to 953.
 * 
 * Which prime, below one-million, can be written as the sum of the most
 * consecutive primes?
 */
