import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;

/* 
* @Fr4nc3
* TopSort class
* Programing Q1
*/
public class TopSort {

    Hashtable<Integer, ArrayList<TopVert>> adjacentList = new Hashtable<>();
    ArrayList<TopVert> topVerts = new ArrayList<>();
    LinkedList<TopVert> topoSorted;

    public TopSort() {

    }

    public void add(TopVert topVert) {
        if (!adjacentList.contains(topVert)) {
            adjacentList.put(topVert.name.hashCode(), new ArrayList<>());
            topVerts.add(topVert);
        }
    }

    public void addNeighbor(TopVert from, TopVert to) {
        if (!adjacentList.containsKey(from.name.hashCode())) {
            add(from);
        }
        if (!adjacentList.containsKey(to.name.hashCode())) {
            add(to);
        }
        adjacentList.get(from.name.hashCode()).add(to);
        to.inDegree++;
        to.inTopVerts.add(from);
    }

    public void resetVisited() {
        for (TopVert TopVert : topVerts) {
            TopVert.visited = false;
        }
    }

    public boolean hasEdge(TopVert from, TopVert to) {
        return adjacentList.get(from).contains(to) ? true : false;
    }

    public void topologicalSort() throws Exception {
        topoSorted = new LinkedList<>();
        HashSet<TopVert> visited = new HashSet<>();
        for (TopVert n : topVerts) {
            if (!visited.contains(n)) {
                visit(n, visited);
            }
        }
    }

    public void visit(TopVert topVert, HashSet<TopVert> set) throws Exception {

        if (topVert.visited) {
            throw new Exception("cyclic");
        } else {

            topVert.visited = true;

            for (TopVert m : adjacentList.get(topVert)) {
                if (!set.contains(m)) {
                    visit(m, set);
                }
            }

            set.add(topVert);
            topVert.visited = false;
            topoSorted.addFirst(topVert);
        }
    }

    public void printTopSort() {

        //System.out.print(topVerts.size() +" size \n");

        for (TopVert topVert : topVerts) {
            if (topVert.visited) {
                // System.out.print(topVert.name +" visited \n");
            } else {
                System.out.print(topVert.name + " ");
                topVert.visited = true;
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        File inFile;
        if (0 < args.length) {
            inFile = new File(args[0] + (args[0].contains(".txt") ? "" : ".txt"));
        } else {
            System.out.println("Missing file to test");
            inFile = new File("csmajor.txt");
        }

        try {
            TopSort ts = new TopSort();
            BufferedReader br = new BufferedReader(new FileReader(inFile));
            for (String line; (line = br.readLine()) != null; ) {
                String[] stringArray = line.split(" ");
                if (stringArray.length == 1) {
                    ts.add(new TopVert(stringArray[0]));
                } else {
                    TopVert tmp = new TopVert(stringArray[stringArray.length - 1]);
                    for (int i = stringArray.length - 2; i > -1; --i) {
                        TopVert tmp1 = new TopVert(stringArray[i]);
                        ts.addNeighbor(tmp, tmp1);
                    }
                }

            }

            try {
                ts.topologicalSort();
            } catch (Exception e) {
                System.err.println(e.getMessage()); // print the exception
            }

            ts.printTopSort(); // print the topsort

        } catch (Exception e) {
            System.err.println(e.getMessage()); // print the exception
        }
    }
}