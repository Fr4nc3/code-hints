import java.util.LinkedList;
/* 
* @Fr4nc3
* MyStack class
* Programing Q1
*/
public class MyStack<AnyType> {
    // using linkedlist
    private LinkedList<AnyType> ll = new LinkedList<>();

    public void push(AnyType el) {
        ll.addFirst(el);
    }

    public AnyType pop() {
        return ll.removeFirst();
    }

    public AnyType peek() {
        return ll.getFirst();
    }

    public int size() {
        return ll.size();
    }

    public boolean isEmpty() {
        return ll.isEmpty();
    }
}