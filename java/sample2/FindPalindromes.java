import java.io.*;
/* 
* @Fr4nc3
* FindPalindromes class
* Programing Q1
*/

public class FindPalindromes {

    public static void main(String[] args) {
        File inFile;
        if (0 < args.length) {
            inFile = new File(args[0] + (args[0].contains(".txt") ? "" : ".txt"));
        } else {
            System.out.println("Missing file to test");
            inFile = new File("palindromes.txt");
        }

        /*
        Stack First In Last Out
        test if was working
        MyStack mystack = new MyStack();
        mystack.push(1);
        mystack.push(2);
        mystack.push(3);
        mystack.push(4);
        while(!mystack.isEmpty()){
            System.out.println(mystack.pop());
        }
        print 4 3 2 1
        */
        try {
            BufferedReader br = new BufferedReader(new FileReader(inFile));
            for (String line; (line = br.readLine()) != null; ) {
                String original = line; // used to print and the end
                line = line.replaceAll("[^\\w]", "").toLowerCase(); // clean line
                MyStack stack = new MyStack();

                for (int i = 0; i < line.length(); ++i) {
                    // entering to the stack the string char by char
                    stack.push(line.charAt(i));
                }

               /* String reverse = "";
                This was my first approach but it is seems not valid
                according to piazza question
                while (!stack.isEmpty()) {
                    reverse += stack.pop();
                }

                if (line.equals(reverse)) {
                    System.out.printf("\"%s\" is a palindrome.\n", original);
                } else {
                    System.out.printf("\"%s\"  is not a palindrome.\n", original);
                }
               */
                boolean isPalindrome = true;
                int i = 0;
                while (!stack.isEmpty()) {
                    //if one character is not equal to the one being pop
                    // it is not palindrome and we stop the while-loop
                    if (!Character.toString(line.charAt(i)).equals(stack.pop().toString())) {
                        isPalindrome = false;
                        break;
                    }
                    ++i;
                }
                // print if the word is palindrome
                if (isPalindrome) {
                    System.out.printf("\"%s\" is a palindrome.\n", original);
                } else {
                    System.out.printf("\"%s\" is not a palindrome.\n", original);
                }

            }
        } catch (Exception e) {
            System.err.println(e.getMessage()); // print the exception
        }
    }
}
