import java.util.Arrays;
import java.util.List;

public class TestKBest {

    public static void main(String[] args) {
        int k = 5;
        KBestCounter<Integer> counter = new KBestCounter<>(k);

        System.out.println("Inserting 1,2,3.");
        for (int i = 1; i <= 3; i++){
            counter.count(i);
        }

        System.out.println("5-best should be [3,2,1]: " + counter.kbest());
        counter.count(2);

        System.out.println("Inserting another 2.");
        System.out.println("5-best should be [3,2,2,1]: " + counter.kbest());

        System.out.println("Inserting 4..99.");
        for (int i = 4; i < 100; i++){
            counter.count(i);
        }

        System.out.println("5-best should be [99,98,97,96,95]: " + counter.kbest());

        System.out.println("Inserting 100, 20, 101.");
        counter.count(100);
        counter.count(20);
        counter.count(101);

        System.out.println("5-best should be [101,100,99,98,97]: " + counter.kbest());
    }
}

