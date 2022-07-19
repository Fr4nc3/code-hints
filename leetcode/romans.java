
public class romans {

    public static void integerToRoman(int num) {

        System.out.println("Integer: " + num);
        int[] intValues = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] romanLiterals = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

        StringBuilder roman = new StringBuilder();

        for(int i=0;i<intValues .length;i++) {
            while(num >= intValues [i]) {
                num -= intValues [i];
                roman.append(romanLiterals[i]);
            }
        }
        System.out.println("Roman: " + roman.toString());
        System.out.println("---------------------------------------------------");
    }

    public static void main(String[] args) {
        integerToRoman(25);
        integerToRoman(36);
        integerToRoman(1023);
        integerToRoman(542);
    }
}