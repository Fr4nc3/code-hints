public class Test {
    public static void main(String[] args) {

        System.out.println(3%9);
        System.out.println(foo(3, 9));

    }

    public static int  foo(int a, int b){
        if(a%b == 0 ){
            return b;
        }
        else return foo(b,a%b);


    }
}
