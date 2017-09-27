/* 
* @Fr4nc3
* Problem3 class
* Programing Q3
*/
public class Problem3 {
    public static final int MAX_TEST_POWER = 9;

    public static void methodA(int n) {
        int sum = 0;
        for (int i = 0; i < 23; i++) {
            for (int j = 0; j < n; j++) {
                sum = sum + 1;
            }
        }
    }

    public static void methodB(int n) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int k = i; k < n; k++) {
                sum = sum + 1;
            }
        }
    }

    public static int foo(int n, int k) {
        if (n <= k)
            return 1;
        else
            return foo(n / k, k) + 1;
    }

    public static int getTheN(int n) {
        return (int) Math.pow(10, n);
    }

    public static void main(String[] args) {

        long startTime, endTime;
        /*
        * TEST METHOD A
        * */
        for (int i = 0; i <= MAX_TEST_POWER; ++i) {
            startTime = System.nanoTime();
            int testN = getTheN(i);
            System.out.println("methodA N: " + testN);
            methodA(testN);
            endTime = System.nanoTime();
            System.out.println(endTime - startTime);
        }

        /*
        * TEST METHOD B
        * */
        for (int i = 0; i <= MAX_TEST_POWER; ++i) {
            startTime = System.nanoTime();
            int testN = getTheN(i);
            System.out.println("methodB N: " + testN);
            methodB(testN);
            endTime = System.nanoTime();
            System.out.println(endTime - startTime);
        }

        /*
        * TEST FOO
        * */
        for (int i = 0; i <= MAX_TEST_POWER; ++i) {
            startTime = System.nanoTime();
            int testN = getTheN(i);
            System.out.println("foo N: " + testN);
            int fooTest = foo(testN, 2); // k = 2 as requested in the hw description
            endTime = System.nanoTime();
            System.out.println(endTime - startTime);
        }
    }
}