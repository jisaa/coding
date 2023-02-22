class P19 {
	public static void main(String... args) {
		new P19();
	}

	public P19() {
		// partir del martes 1-1-1901
		// llegar al domingo 31-12-2000
		int dia = 1, mes = 1, año = 1901, diaSemana = 2, total = 0;
		while (año < 2001) {
			while (dia < largoMes(mes, año)) {
				++dia;
				++diaSemana;
				if (diaSemana == 7)
					diaSemana = 0;
			}
			++mes;
			dia = 0;
			if (mes == 13) {
				mes = 1;
				++año;
			}
			if (diaSemana == 6)
				++total;
		}
		System.out.println("El total es: " + total);
	}

	int[] l = { -1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

	private int largoMes(int mes, int año) {
		if (mes == 2 && año % 4 == 0)
			return 29;
		return l[mes];
	}
}