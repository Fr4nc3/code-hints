/* 
* @Fr4nc3
* ExpressionTree class
* Programing Q1
*/
public class ExpressionTree {
    //nested clasa with 3 members and 1 constructor
    private class ExpressionNode<AnyType> {
        private ExpressionNode left;
        private AnyType data;
        private ExpressionNode right;

        public ExpressionNode(ExpressionNode left, AnyType data, ExpressionNode right) {
            this.left = left;
            this.data = data;
            this.right = right;
        }
    }

    ExpressionNode expressionNode;
    String expression;

    public ExpressionTree(String expression) {

        if (!expression.matches("^[0-9 \\+\\*/\\-]+$")) {  // must contains numbers and -+/*
            // System.out.print("wrong expression");
            expressionNode = null;
            return;
        }
        this.expression = expression;
        MyStack<ExpressionNode> nodes = new MyStack<>();
        String[] stringArray = expression.split("\\s+"); // split the expression
        ExpressionNode node, node1, node2;
        for (String ch : stringArray) {
            if (!isOperator(ch)) { // if it is a number enter to the stack
                node = new ExpressionNode(null, ch, null);
                nodes.push(node);
            } else { // if it is a character (+*/-)
                node1 = nodes.pop();
                node2 = nodes.pop();
                node = new ExpressionNode(node2, ch, node1);

                //System.out.println(node1.data + " " + node2.data);
                nodes.push(node);
            }
        }
        node = nodes.pop();
        //System.out.println(node.data);
        expressionNode = node;
    }

    private boolean isOperator(String op) {
        return "+*-/".contains(op);
    }

    public int eval() {
        return eval(expressionNode);
    }

    private int eval(ExpressionNode node) {
        if (node == null) {
            return 0;
        }
        if (!isOperator(node.data.toString())) { //if it is not a operator convert it to integer
            return Integer.parseInt(node.data.toString());
        }
        // apply the operator
        switch (node.data.toString()) {
            case "*":
                return eval(node.left) * eval(node.right);
            case "+":
                return eval(node.left) + eval(node.right);
            case "-":
                return eval(node.left) - eval(node.right);
            case "/":
                int nodeRight = eval(node.right);// check not divide by zero
                return nodeRight != 0 ? (eval(node.left) / nodeRight) : 0;
            default:
                return 0;
        }
    }

    public String postfix() {
        StringBuffer postfix = new StringBuffer();
        postOrder(expressionNode, postfix);
        return postfix.toString();
    }

    private void postOrder(ExpressionNode node, StringBuffer postfix) {
        if (node != null) {
            preOrder(node.left, postfix);
            preOrder(node.right, postfix);
            postfix.append(node.data.toString());
            postfix.append(" ");
        }
    }

    public String prefix() {
        if (expressionNode == null) {
            return "";
        }

        StringBuffer prefix = new StringBuffer();
        preOrder(expressionNode, prefix);
        return prefix.toString();
    }

    private void preOrder(ExpressionNode node, StringBuffer prefix) {
        if (node != null) {
            prefix.append(node.data.toString());
            prefix.append(" ");
            preOrder(node.left, prefix);
            preOrder(node.right, prefix);
        }
    }

    public String infix() {
        if (expressionNode == null) {
            //System.out.print("null");
            return "";
        }
        StringBuffer infixStr = new StringBuffer();
        inOrder(expressionNode, infixStr);
        //System.out.println(infixStr);
        return infixStr.toString();
    }

    private void inOrder(ExpressionNode node, StringBuffer infix) {
        if (node != null) {
            //System.out.println("enter inorder");
            if (!(node.left == null && node.right == null))// only parentheses when they aren't
                infix.append("(");

            inOrder(node.left, infix);
            infix.append(node.data.toString());
            inOrder(node.right, infix);

            if (!(node.left == null && node.right == null))
                infix.append(")");
        }
    }
}
