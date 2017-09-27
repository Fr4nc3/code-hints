/* 
* @Fr4nc3
* Programing Q1
*/
public class Problem1 {
    public static final int ARRAY_SIZE = 5;

    public static <AnyType extends Comparable<AnyType>> AnyType findMax(AnyType[] arr) {
        int maxIndex = 0;
        for (int i = 0; i < arr.length; ++i) {
            if (arr[i].compareTo(arr[maxIndex]) > 0) {
                maxIndex = i;
            }
        }
        return arr[maxIndex];
    }

    public static void main(String[] args) {
        /*
         * First test of findMax with a simple Array
		*/

        Rectangle[] a = new Rectangle[ARRAY_SIZE];
        a[0] = new Rectangle(1, 2);
        a[1] = new Rectangle(2, 2);
        a[2] = new Rectangle(2, 3);
        a[3] = new Rectangle(3, 3);
        a[4] = new Rectangle(3, 4);

        Rectangle maxRectangle = findMax(a);
        System.out.println("Found max Rectangle" + maxRectangle.toString());

		/*
		 * second test creating the dimensions of the array dynamically.
		*/
        System.out.println("\n\n\nSecond test with random Rectangles:\n");

        Rectangle[] a2 = new Rectangle[ARRAY_SIZE];

        for (int i = 0; i < ARRAY_SIZE; ++i) {
            int width = (int) (Math.random() * 50 + 1);  //from1,50
            int length = (int) (Math.random() * 50 + 1);
            a2[i] = new Rectangle(length, width);

        }

        System.out.println("New Array Rectangles Dimensions:\n");

        for (int i = 0; i < ARRAY_SIZE; ++i) {
            System.out.println("Rectangle " + i);
            System.out.println(a2[i].toString() + "\n");
        }

        Rectangle newMaxRectangle = findMax(a2);
        System.out.println("Found max Rectangle" + newMaxRectangle.toString());
    }
}