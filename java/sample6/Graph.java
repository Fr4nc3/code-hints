import java.util.*;

public class Graph {

    // Keep a fast index to nodes in the map
    private Map<Integer, Vertex> vertexNames;

    //for bruteforce
    private double minDistance = Double.MAX_VALUE;
    private List<Edge> edgesForBruceForce;
    List<Integer> brunceForceFinalList;

    /**
     * Construct an empty Graph with a map. The map's key is the name of a vertex
     * and the map's value is the vertex object.
     */
    public Graph() {
        vertexNames = new HashMap<>();
    }

    /**
     * Adds a vertex to the graph. Throws IllegalArgumentException if two vertices
     * with the same name are added.
     *
     * @param v (Vertex) vertex to be added to the graph
     */
    public void addVertex(Vertex v) {
        if (vertexNames.containsKey(v.name))
            throw new IllegalArgumentException("Cannot create new vertex with existing name.");
        vertexNames.put(v.name, v);
    }

    /**
     * Gets a collection of all the vertices in the graph
     *
     * @return (Collection<Vertex>) collection of all the vertices in the graph
     */
    public Collection<Vertex> getVertices() {
        return vertexNames.values();
    }

    /**
     * Gets the vertex object with the given name
     *
     * @param name (String) name of the vertex object requested
     * @return (Vertex) vertex object associated with the name
     */
    public Vertex getVertex(int name) {
        return vertexNames.get(name);
    }

    /**
     * Adds a directed edge from vertex u to vertex v
     *
     * @param nameU (String) name of vertex u
     * @param nameV (String) name of vertex v
     * @param cost  (double) cost of the edge between vertex u and v
     */
    public void addEdge(int nameU, int nameV, Double cost) {
        if (!vertexNames.containsKey(nameU))
            throw new IllegalArgumentException(nameU + " does not exist. Cannot create edge.");
        if (!vertexNames.containsKey(nameV))
            throw new IllegalArgumentException(nameV + " does not exist. Cannot create edge.");
        Vertex sourceVertex = vertexNames.get(nameU);
        Vertex targetVertex = vertexNames.get(nameV);
        Edge newEdge = new Edge(sourceVertex, targetVertex, cost);
        sourceVertex.addEdge(newEdge);
    }

    /**
     * Adds an undirected edge between vertex u and vertex v by adding a directed
     * edge from u to v, then a directed edge from v to u
     *
     * @param name  (String) name of vertex u
     * @param name2 (String) name of vertex v
     * @param cost  (double) cost of the edge between vertex u and v
     */
    public void addUndirectedEdge(int name, int name2, double cost) {
        addEdge(name, name2, cost);
        addEdge(name2, name, cost);
    }


    /**
     * Computes the euclidean distance between two points as described by their
     * coordinates
     *
     * @param ux (double) x coordinate of point u
     * @param uy (double) y coordinate of point u
     * @param vx (double) x coordinate of point v
     * @param vy (double) y coordinate of point v
     * @return (double) distance between the two points
     */
    public double computeEuclideanDistance(double ux, double uy, double vx, double vy) {
        return Math.sqrt(Math.pow(ux - vx, 2) + Math.pow(uy - vy, 2));
    }

    /**
     * Computes euclidean distance between two vertices as described by their
     * coordinates
     *
     * @param u (Vertex) vertex u
     * @param v (Vertex) vertex v
     * @return (double) distance between two vertices
     */
    public double computeEuclideanDistance(Vertex u, Vertex v) {
        return computeEuclideanDistance(u.x, u.y, v.x, v.y);
    }

    /**
     * Calculates the euclidean distance for all edges in the map using the
     * computeEuclideanCost method.
     */
    public void computeAllEuclideanDistances() {
        for (Vertex u : getVertices())
            for (Edge uv : u.adjacentEdges) {
                Vertex v = uv.target;
                uv.distance = computeEuclideanDistance(u.x, u.y, v.x, v.y);
            }
    }


    // @Fr4nc3

    public void generateRandomVertices(int n) {
        vertexNames = new HashMap<>(); // reset the vertex hashmap

        Random r = new Random();
        int low = 0;
        int high = 100;
        for (int i = 0; i < n; ++i) {
            int x = r.nextInt(high - low) + low;
            int y = r.nextInt(high - low) + low;
            Vertex v = new Vertex(i, x, y);
            addVertex(v);
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                Vertex v1 = getVertex(i);
                Vertex v2 = getVertex(j);
                addEdge(i, j, computeEuclideanDistance(v1, v2));
            }
        }

        computeAllEuclideanDistances(); // compute distances
    }

    public List<Edge> nearestNeighborTsp() {
        for (int u : vertexNames.keySet()) {
            vertexNames.get(u).known = false; //reset visited cities;
        }
        List<Edge> list = new LinkedList<>();
        List<Integer> arr = new ArrayList<>();
        Vertex step = getVertex(0); //from the first one

        while (!step.known) {
            step.known = true;
            arr.add(step.name);

            double dist = Double.MAX_VALUE;
            Vertex tmp = new Vertex(0, 0, 0);
            tmp.known = true; // make brake the loop
            for (Edge e : step.adjacentEdges) {
                if (e.distance < dist && !e.target.known) {
                    dist = e.distance;
                    tmp = e.target;
                }
            }
            step = tmp;

        }
        System.out.println(java.util.Arrays.toString(arr.toArray()));

        Vertex v1;
        Vertex v2;
        double dist;
        Edge newEdge;

        // last point back home
        v1 = getVertex(arr.get(0));
        v2 = getVertex(arr.get(arr.size() - 1));
        dist = computeEuclideanDistance(v1, v2);
        newEdge = new Edge(v1, v2, dist);
        list.add(newEdge);
        for (int j = 0; j < arr.size() - 1; ++j) {
            v1 = getVertex(arr.get(j));
            v2 = getVertex(arr.get(j + 1));
            dist = computeEuclideanDistance(v1, v2);
            newEdge = new Edge(v1, v2, dist);
            // System.out.println(arr.get(j) + "" + arr.get(j+1));
            list.add(newEdge);
        }

        return list;
    }

    public List<Edge> bruteForceTsp() {
        minDistance = Double.MAX_VALUE;
        List<Integer> arr = new ArrayList<>();
        for (int u : vertexNames.keySet()) {
            arr.add(u);
        }
        allPossiblePermute(arr, 0);

        System.out.println(java.util.Arrays.toString(brunceForceFinalList.toArray()));
        return edgesForBruceForce;
    }

    public void allPossiblePermute(List<Integer> arr, int k) {
        for (int i = k; i < arr.size(); ++i) {
            Collections.swap(arr, i, k);
            allPossiblePermute(arr, k + 1);
            Collections.swap(arr, k, i);
        }

        if (k == arr.size() - 1) {
            List<Edge> resultList = new LinkedList<>();
            //System.out.println(java.util.Arrays.toString(arr.toArray()));
            double cost = 0.0;
            Vertex v1;
            Vertex v2;
            double dist = 0.0;
            Edge newEdge;
            // last point back home
            v1 = getVertex(arr.get(0));
            v2 = getVertex(arr.get(arr.size() - 1));
            dist = computeEuclideanDistance(v1, v2);
            newEdge = new Edge(v1, v2, dist);
            cost += dist;
            resultList.add(newEdge);
            for (int j = 0; j < arr.size() - 1; ++j) {
                v1 = getVertex(arr.get(j));
                v2 = getVertex(arr.get(j + 1));
                dist = computeEuclideanDistance(v1, v2);
                newEdge = new Edge(v1, v2, dist);
                cost += dist;
                // System.out.println(arr.get(j) + "" + arr.get(j+1));
                resultList.add(newEdge);
            }

            if (cost < minDistance) {
                minDistance = cost;
                edgesForBruceForce = resultList;
                brunceForceFinalList = arr;
                //System.out.println("new cost:"+ cost);
                //System.out.println(java.util.Arrays.toString(arr.toArray()));
            } else {
                //System.out.println(" no update cost:"+ cost);
            }

        }
    }

    // @Fr4nc3


    /**
     * Prints out the adjacency list of the graph for debugging
     */
    public void printAdjacencyList() {
        for (int u : vertexNames.keySet()) {
            StringBuilder sb = new StringBuilder();
            sb.append(u);
            sb.append(" -> [ ");
            for (Edge e : vertexNames.get(u).adjacentEdges) {
                sb.append(e.target.name);
                sb.append("(");
                sb.append(e.distance);
                sb.append(") ");
            }
            sb.append("]");
            System.out.println(sb.toString());
        }
    }
}
