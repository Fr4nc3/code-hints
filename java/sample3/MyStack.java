/* 
* @Fr4nc3
* MyStack.java
* Implements a Stack using a Linked List
*/

import java.util.LinkedList;

public class MyStack<T> {

    private LinkedList<T> stack;

    public MyStack(){
        stack = new LinkedList<T>();
    }

    // if stack is empty return null, else remove element from stack
    public T pop(){

        if(stack.size() == 0){
            return null;
        }
        else{
            return stack.remove();
        }
    }

    // displays first elements in stack
    public T peek(){
        return stack.getFirst();
    }

    // adds element to the top of stack
    public void push(T e){
        stack.addFirst(e);
    }

    // only used for TwoStackQueue
    public boolean isEmpty(){
        return stack.isEmpty();
    }
}