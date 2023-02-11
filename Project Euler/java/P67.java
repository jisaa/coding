import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;

public class P67 {
	public static void main(String... args) {
		// Tratar de leer desde archivo.
		// Si no se puede, leer desde la entrada estándar.
		Scanner s;
		try {
			s = new Scanner(new File("Project Euler/inputs/p67.in"));
		} catch (Exception e) {
			System.out.println("Leyendo input desde la consola");
			s = new Scanner(System.in);
		}

		// Cargar los datos en memoria.
		ArrayList<int[]> filas = new ArrayList<int[]>();
		int k = 1;
		while (s.hasNext()) {
			int[] fila = new int[k];
			for (int i = 0; i < k; ++i)
				fila[i] = s.nextInt();
			filas.add(fila);
			++k;
		}

		// Calcular "destructivamente" (modificando los datos directamente).
		for (int i = k - 3; i >= 0; --i)
			for (int j = 0; j < i + 1; ++j)
				if (filas.get(i + 1)[j] > filas.get(i + 1)[j + 1])
					filas.get(i)[j] += filas.get(i + 1)[j];
				else
					filas.get(i)[j] += filas.get(i + 1)[j + 1];

		// Imprimir el resultado
		System.out.println(filas.get(0)[0]);
	}
}
