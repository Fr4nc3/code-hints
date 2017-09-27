Fr4nc3
==========

ExpressionTree.java
MyStack.java
Problem1.java
AvlTree.java
UnderFlowException.java
Problem2.java
README.txt


Programming Question 1
======================
MyStack was copy from HW2 solutions

how to create inOrder, PostOrder and PreOrder from the lectures
In order
1. Process left child
2. Process root
3. Process right child

Post-order
1. Process left child
2. Process right child
3. Process root

Pre-order
1. Process root
2. Process left child
3. Process right child
I used this link as a reference for my code
http://www.dreamincode.net/forums/topic/88830-prefix-infix-postfix/

This post from Piazza helps me to solve the stack usage and the second example of my test
 /*
    Check the lecture notes, lecture 7, slides starting at 54.
    The algorithm is basically the same as the one to evaluate postfix expressions,
    except that you push trees to the stack instead of integer values.
    When you encounter an operator you pop the top two trees of the stack.
     You then make these trees the left and the right subtree of a new parent node for the operator.
    ---
    From Paul: This is section 4.2.2 in the text book.
 */

Programming Question 2
======================
Problem2 main method receive the name of the file as parameter.
this works only if the file is in the same directory of the class.

I added two methods to AvlTree
AnyType containsAndPop( AnyType x )
AnyType containsAndPop( AnyType x, AvlNode<AnyType> t )
They are similar to contains implementation but instead to return boolean it return the element if exist and null
if the element doesn't exist, also, it remove the element from the tree.

when I implemented the compareTo version of MyElement I compare only the word (i.e string)
So, when I use containsAndPop only check if the word exist and not if the line exist,

So when I use the  method containsAndPop
it find the word, copy the element that contain the word and delete de element from the tree
with the element and it latest linkedlist we
check if the line number exist in the linkedlist and insert it back to the tree
if the word doesn't exist I insert as new element in the tree

I am not so happy with the fact that the element is removed/added if appears many time.

however,

I cannot manipulate the LinkedList on AvlTree bc AvlTree uses generic data.
MyElement is a very simple class with two members, a constructor and  3 methods
I did it static so I can put the code inside Problem2 java.

To read the file I used the same code from hw2

I remove all the characters for example it's now it s and 's' counts as a word same happens they've
they ve and 've' is counted as a word too.


HW CODE ENVIRONMENT
==================
Intel(R) Core(TM) i7-48070HQ CPU @ 2.50 GHz
RAM 16GB
Windows 10 Pro
Java 1.8.0_72
IntelliJ IDEA 15.0.3



