/* 
* @Fr4nc3
* Problem2 class
* Programing Q2
*/
import java.util.Arrays;

public class Problem2 {
    public static final int ARRAY_SIZE = 5;

    public static <AnyType extends Comparable<AnyType>> int binarySearch(AnyType[] a, AnyType x) {
        return binarySearch(a, x, 0, a.length - 1);
    }

    public static <AnyType extends Comparable<AnyType>> int binarySearch(AnyType[] a, AnyType x,
                                                                         int low, int high) {
        if (low > high) return -1;
        int mid = (low + high) / 2;
        if (a[mid].compareTo(x) == 0) return mid;
        else if (a[mid].compareTo(x) < 0)
            return binarySearch(a, x, mid + 1, high);
        else // last possibility
            return binarySearch(a, x, low, mid - 1);
    }

    public static void main(String[] args) {

        Rectangle[] a = new Rectangle[ARRAY_SIZE];
        //create an empty rectangle that we will use to find after the sort
        Rectangle findRectangle = new Rectangle(0, 0);
        for (int i = 0; i < ARRAY_SIZE; ++i) {
            // generate dimensions randomly
            int width = (int) (Math.random() * 50 + 1);
            int length = (int) (Math.random() * 50 + 1);

            // we give real dimension to our rectangle
            // this means it always will appear in this test case
            if (findRectangle.getLength() == 0) {
                findRectangle.setLength(length);
                findRectangle.setWidth(width);
            }

            a[i] = new Rectangle(length, width);
        }
        Arrays.sort(a);
        System.out.println("New Array Rectangles Dimensions:\n");

        for (int i = 0; i < ARRAY_SIZE; ++i) {
            System.out.println("Rectangle " + i);
            System.out.println(a[i].toString() + "\n");
        }

        System.out.println("Found Rectangle" + findRectangle.toString());
        System.out.println("Rectangle Index: " + binarySearch(a, findRectangle));

        /*
        * Second test we create a rectangle with random dimensions and
        * it may or may not exist
        * */
        int width = (int) (Math.random() * 50 + 1);
        int length = (int) (Math.random() * 50 + 1);
        Rectangle doExistRectangle = new Rectangle(length, width);

        System.out.println("\n\nNew  Rectangle to find" + doExistRectangle.toString());
        System.out.println("Rectangle Index? " + binarySearch(a, doExistRectangle));

    }
}