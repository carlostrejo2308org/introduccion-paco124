public class fibonacci {
    public static void main(String[] args) {
        int n = 10; // Cambia este valor para obtener el término deseado
        int resultado = calcularFibonacci(n);
        System.out.println("El término " + n + " de la secuencia Fibonacci es: " + resultado);
    }
    
    public static int calcularFibonacci(int n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            int fibPrevio = 0;
            int fibActual = 1;
            for (int i = 2; i <= n; i++) {
                int temp = fibActual;
                fibActual = fibPrevio + fibActual;
                fibPrevio = temp;
            }
            return fibActual;
        }
    }
}