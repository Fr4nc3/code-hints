import java.util.ArrayList;

/* 
* @Fr4nc3
* TopVert class
* Programing Q1
*/
public class TopVert {
    String name;
    boolean visited = false;
    int inDegree = 0;
    ArrayList<TopVert> inTopVerts = new ArrayList<>();

    public TopVert (String value) {
        this.name = value;
    }
}