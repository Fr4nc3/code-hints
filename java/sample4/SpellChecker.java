import com.sun.deploy.util.StringUtils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.text.Normalizer;
import java.util.*;

/* 
* @Fr4nc3
* SpellChecker class
* Programing Q1
*/
public class SpellChecker {
    public static class MyDictionary {
        public static Hashtable<Integer, String> dictionary = new Hashtable<>();
        public static String alphabet = "abcdefghijklmnopqrstuvwxyz";

        public static void put(int hash, String word) {
            dictionary.put(hash, word);
        }

        public static boolean exist(String word) {
            return (dictionary.contains(word)); // true or false!
        }

        public static List<String> getSuggestion(String word) {

            Set<String> set = new HashSet<>();
            /*
            * each method return a set of word or an empty set
            * So, we can use addAll
            * and it wont have repeated suggestions
            * */
            set.addAll(byRemoveCharacter(word));
            set.addAll(byAddCharacter(word));
            set.addAll(byAdjacentSwap(word));
            return new ArrayList<>(set); //a list so it is easy to join and string
        }

        //a. Add one character.
        public static Set<String> byAddCharacter(String word) {
            Set<String> set = new HashSet<>();
            for (int i = 0; i <= word.length(); ++i) {
                for (int j = 0; j < alphabet.length(); ++j) {
                    char c = alphabet.charAt(i);
                    String test = word.substring(0, i) + c + word.substring(i);
                    if (exist(test)) {
                        set.add(test);
                    }
                }
            }
            return set;
        }

        //b. Remove one character.
        public static Set<String> byRemoveCharacter(String word) {
            Set<String> set = new HashSet<>();
            for (int i = 0; i < word.length(); ++i) {
                String test = word.substring(0, i) + word.substring(i + 1);
                if (exist(test)) {
                    set.add(test);
                }
            }
            return set; // if nothing got added, return empty set
        }

        // c. Exchange adjacent characters.
        public static Set<String> byAdjacentSwap(String word) {
            Set<String> set = new HashSet<>();
            for (int i = 0; i < word.length() - 1; ++i) {
                String test = word.substring(0, i) +
                        word.substring(i + 1, i + 2) +
                        word.substring(i, i + 1) +
                        word.substring(i + 2);
                if (exist(test)) {
                    set.add(test);
                }
            }
            return set;
        }

    }

    public static void main(String[] args) {

        File wordsList;
        File textList;
        if (1 < args.length) {
            wordsList = new File(args[0] + (args[0].contains(".txt") ? "" : ".txt"));
            textList = new File(args[1] + (args[1].contains(".txt") ? "" : ".txt"));

        } else {
            System.out.println("Missing files to test");
            wordsList = new File("words.txt");
            textList = new File("filetospellcheck.txt");
        }

        try {
            BufferedReader br = new BufferedReader(new FileReader(wordsList));
            MyDictionary dictionary = new MyDictionary();
            int counter = 0;
            // load the dictionary
            for (String line; (line = br.readLine()) != null; ) {
                // clean the dictionary word
                /*
                This can be used if I want to compare two words
                like orčpžsíáýd ==  orcpzsiayd
                line = Normalizer.normalize(line, Normalizer.Form.NFD);
                line = line.replaceAll("[^\\p{ASCII}]", "");
                line = line.replaceAll("\\p{M}", "");
                */
                //System.out.println(line);
                dictionary.put(counter, line.toLowerCase());
                ++counter;
            }
            int lineCounter = 1; // first line
            br = new BufferedReader(new FileReader(textList));
            for (String line; (line = br.readLine()) != null; ) {
                String[] stringArray = line.split("\\s+"); // split the line

                for (String word : stringArray) {
                    word = word.replaceAll("[^\\w'-]", "").toLowerCase(); // word by word
                    if (!dictionary.exist(word)) {
                        List<String> suggestions = dictionary.getSuggestion(word);
                        if (suggestions.size() > 0) {
                            //String sugges = StringUtils.join(suggestions, ",");
                            /*StringBuilder sb = new StringBuilder();
                            for (String s : suggestions) {
                                sb.append(s);
                                sb.append(", ");
                            }
                            String suggestionList = sb.toString();*/
                            // System.out.printf("\"%s\" in line %d is misspelled some suggestions: %s\n",
                            //     word, lineCounter, suggestionList.substring(0, suggestionList.length() - 2));
                            System.out.printf("\"" + word + "\" in line " + lineCounter
                                    + " is misspelled some suggestions: " + suggestions + "\n");
                        } else {
                            System.out.printf("\"%s\" in line %d is misspelled no suggestions.\n",
                                    word, lineCounter);
                        }
                    }
                }
                ++lineCounter;
            }
        } catch (Exception e) {
            System.err.println(e.getMessage()); // print the exception
        }
    }
}
