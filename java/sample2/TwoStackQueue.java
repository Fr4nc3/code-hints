/* 
* @Fr4nc3
* TwoStackQueue class
* Programing Q2
*/
public class TwoStackQueue<AnyType> {
    private MyStack<AnyType> s1 = new MyStack<>();
    private MyStack<AnyType> s2 = new MyStack<>();

    public boolean isEmpty() {
        return s1.isEmpty() && s2.isEmpty();
    }

    private void transferS1ToS2() {
        /* moving all element from s1 to S2
        using a while-loop
        */
        while (!s1.isEmpty()) {
            s2.push(s1.pop());
        }
    }

    public void enqueue(AnyType el) {
        // this push is the push method in the mystack
        // which is a linkedlist addFirst
        s1.push(el);
    }

    public AnyType dequeue() {
        /* before popping the element
        from s2 we check if it is not empty
         this happens all the time in the dequeue
        */
        if (s2.isEmpty()) {
            transferS1ToS2();
        }
        return s2.pop();
    }
}
