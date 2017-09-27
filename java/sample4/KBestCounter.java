import java.util.*;

public class KBestCounter<T extends Comparable<? super T>> {

    PriorityQueue<T> heap;
    int k;

    public KBestCounter(int k) {
        this.k = k; // set the size of the heap
        heap = new PriorityQueue<>(k);
    }

    public void count(T x) {
        if (heap.size() < k) {
            heap.add(x); // if the heap is not full
        } else if (x.compareTo(heap.peek()) > 0){ // if the head of this queue. is smaller than x
            heap.poll(); //remove the head
            heap.add(x); // add the new number
        }
    }

    public List<T> kbest() {
        List l = new ArrayList(heap); // convert heap to list
        Collections.reverse(l); // sort reverse
        return l;
    }

}
