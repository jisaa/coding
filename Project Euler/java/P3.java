class P3 {

	public static void main(String... args) {
		long n = 600851475143L;
		long ultimo = 0;
		for (long i = 2L; i < n; ++i) {
			if (n % i == 0) {
				if (esPrimoYMayor(ultim, i)) {
					ultimo = i;
					n /= ultimo;
				}
			}
		}
		System.out.println(n);
	}

	static long ultim = 2;

	private static boolean esPrimoYMayor(long ultimo, long a) {
		for (long i = ultimo; i < Math.sqrt(a); ++i) {
			if (a % i == 0) {
				return false;
			}
			ultim = a;
		}
		return true;
	}
}