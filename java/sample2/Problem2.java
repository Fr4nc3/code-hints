/* 
* @Fr4nc3
* Problem2 class
* Programing Q2
*/
public class Problem2 {
    public static void main(String[] args) {
        /*
        * Queue First in, First Out
        * */
        long startTime, endTime;
        int testSize = 100;
        int i = 0;
        startTime = System.nanoTime();
        TwoStackQueue test1 = new TwoStackQueue();
        System.out.println("Enqueueing a Queue of Integers: ");
        for (i = 0; i < testSize; ++i) {
            test1.enqueue(i);
        }

        endTime = System.nanoTime();
        System.out.println("Time for enqueueing ");
        System.out.println(endTime - startTime);

        startTime = System.nanoTime();// time for deque
        System.out.println("Dequeueing a Queue of Integers: ");
        while (!test1.isEmpty()) {
            System.out.print(test1.dequeue());
        }
        endTime = System.nanoTime();
        System.out.println("Time for enqueueing ");
        System.out.println(endTime - startTime);

        System.out.println("Enqueueing a Queue of char: ");
        startTime = System.nanoTime();// time for endeque
        TwoStackQueue test2 = new TwoStackQueue();
        String testLine = "Lorem Ipsum is simply dummy text of the printing " +
                "and typesetting industry. Lorem Ipsum has been the ";
        for (i = 0; i < testSize; ++i) {
            test2.enqueue(testLine.charAt(i));
        }
        endTime = System.nanoTime();
        System.out.println("Time for enqueueing ");
        System.out.println(endTime - startTime);

        startTime = System.nanoTime();// time for deque
        System.out.println("Deueueing a Queue of Integers: ");
        while (!test2.isEmpty()) {
            System.out.print(test2.dequeue());
        }
        endTime = System.nanoTime();
        System.out.println("Time for dequeueing ");
        System.out.println(endTime - startTime);
    }
}
