import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.LinkedList;

/* 
* @Fr4nc3
* Problem2 class
* Programing Q2
*/
public class Problem2 {
    public static class MyElement implements Comparable<MyElement> {
        private String word;
        private LinkedList<Integer> ll = new LinkedList<>();

        public MyElement(String word, int number) {
            this.word = word;
            ll.add(number);
        }

        public void contains(int number) {
            if (!ll.contains(number)) {
                ll.add(number);
            }
        }

        @Override
        public int compareTo(MyElement e) {
            if (e == null) {
                return 0;
            }
            // use the string compareTo instead comprateToIgnoreCase because I know the words comes already lowercase
            return word.compareTo(e.word);
        }

        @Override
        public String toString() {
            //convert the linkedlist first in a simple array
            int[] arr = ll.stream().filter(i -> i != null).mapToInt(i -> i).toArray();
            String result = word + ": " + Arrays.toString(arr);
            //for (int s : ll)
            //result += s + ", ";
            return result;
        }
    }

    public static void main(String[] args) {

        File inFile;
        if (0 < args.length) {
            inFile = new File(args[0] + (args[0].contains(".txt") ? "" : ".txt"));
        } else {
            System.out.println("Missing file to test");
            inFile = new File("2016su.txt");
        }

        try {
            BufferedReader br = new BufferedReader(new FileReader(inFile));
            AvlTree<MyElement> tree = new AvlTree<>();
            int lineCounter = 1; // first line

            for (String line; (line = br.readLine()) != null; ) {
                line = line.replaceAll("[^\\w-]", "").toLowerCase(); // clean line
                String[] stringArray = line.split("\\s+"); // split the line

                for (String word : stringArray) {
                    word = word.toLowerCase(); // word by word
                    //System.out.println(line);
                    MyElement tempElement = new MyElement(word, lineCounter);
                    MyElement tempElementPop = tree.containsAndPop(tempElement);
                    if (tempElementPop != null) { // word exist and we just removed it to update linkedlist
                        tempElementPop.contains(lineCounter);
                        tree.insert(tempElementPop); // insert again
                    } else {
                        tree.insert(tempElement); // insert word inisert
                    }
                }
                //System.out.println(line);
                ++lineCounter; // next line
            }
            tree.printTree(); // print the tree

        } catch (Exception e) {
            System.err.println(e.getMessage()); // print the exception
        }

    }
}
