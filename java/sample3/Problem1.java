/* 
* @Fr4nc3
* Problem1 class
* Programing Q1
*/
public class Problem1 {
    public static void main(String[] args) {
        ExpressionTree tree = new ExpressionTree("34 2 - 5 *");
        System.out.println("infix: " + tree.infix());
        System.out.println("prefix: " + tree.prefix());
        System.out.println("postfix: " + tree.postfix());
        System.out.println("eval: " + tree.eval()); // 160 expected result

        ExpressionTree tree1 = new ExpressionTree("5 27 2 3 * / +"); //5 + 27 / (2 * 3) example from lectures
        System.out.println("infix: " + tree1.infix());
        System.out.println("prefix: " + tree1.prefix());
        System.out.println("postfix: " + tree1.postfix());
        System.out.println("eval: " + tree1.eval()); //9 expected result

        ExpressionTree tree3 = new ExpressionTree("jhj 0 *-khk");
        System.out.println(tree3.eval()); // 0 because it is null
    }
}
