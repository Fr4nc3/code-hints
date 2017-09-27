import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Desktop;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.RenderingHints;
import java.awt.Stroke;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSeparator;
import javax.swing.JTextField;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;

@SuppressWarnings("serial")
public class Display extends JFrame {

  private JPanel contentPane;
  private GraphPanel panel;
  private Graph graph;
  private JTextField textField;

  /**
   * Launch the application.
   */
  public static void main(String[] args) {
    EventQueue.invokeLater(new Runnable() {
      public void run() {
        try {
          Display frame = new Display();
          frame.setVisible(true);
        } catch (Exception e) {
          e.printStackTrace();
        }
      }
    });
  }

  public static Graph graphFactory() {
    Graph graph = new Graph();
    return graph;
  }

  /**
   * Create the frame.
   */
  public Display() {
    setTitle("Data Structures Graph Visualizer");
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setBounds(50, 50, 900, 700);
    setMinimumSize(new Dimension(800, 600));
    contentPane = new JPanel();
    contentPane.setBorder(new EmptyBorder(10, 10, 10, 10));
    setContentPane(contentPane);
    GridBagLayout gbl_contentPane = new GridBagLayout();
    gbl_contentPane.columnWidths = new int[] { 0, 0, 0, 0 };
    gbl_contentPane.rowHeights = new int[] { 0, 0, 0, 0, 0, 0, 0, 0 };
    gbl_contentPane.columnWeights = new double[] { 0.0, 0.0, 1.0, Double.MIN_VALUE };
    gbl_contentPane.rowWeights = new double[] { 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE };
    contentPane.setLayout(gbl_contentPane);

    graph = graphFactory();

    panel = new GraphPanel(graph);
    GridBagConstraints gbc_panel = new GridBagConstraints();
    gbc_panel.gridwidth = 7;
    gbc_panel.insets = new Insets(0, 0, 7, 0);
    gbc_panel.fill = GridBagConstraints.BOTH;
    gbc_panel.gridx = 0;
    gbc_panel.gridy = 0;
    contentPane.add(panel, gbc_panel);

    JSeparator separator = new JSeparator();
    separator.setBackground(Color.WHITE);
    separator.setForeground(Color.GRAY);
    GridBagConstraints gbc_separator = new GridBagConstraints();
    gbc_separator.fill = GridBagConstraints.BOTH;
    gbc_separator.gridwidth = 4;
    gbc_separator.insets = new Insets(0, 0, 5, 0);
    gbc_separator.gridx = 0;
    gbc_separator.gridy = 1;
    contentPane.add(separator, gbc_separator);

    JLabel lblPanda = new JLabel("Panda 2016 <http://linanqiu.github.io/>");
    lblPanda.setForeground(UIManager.getColor("TextField.light"));
    lblPanda.addMouseListener(new MouseAdapter() {
      @Override
      public void mouseReleased(MouseEvent e) {
        try {
          Desktop.getDesktop().browse(new URI("http://linanqiu.github.io/"));
        } catch (IOException e1) {
          // TODO Auto-generated catch block
          e1.printStackTrace();
        } catch (URISyntaxException e1) {
          // TODO Auto-generated catch block
          e1.printStackTrace();
        }
      }
    });

    JLabel lblGenerateRandomGraph = new JLabel("Generate Random Graph");
    GridBagConstraints gbc_lblGenerateRandomGraph = new GridBagConstraints();
    gbc_lblGenerateRandomGraph.anchor = GridBagConstraints.EAST;
    gbc_lblGenerateRandomGraph.insets = new Insets(0, 0, 5, 5);
    gbc_lblGenerateRandomGraph.gridx = 0;
    gbc_lblGenerateRandomGraph.gridy = 2;
    contentPane.add(lblGenerateRandomGraph, gbc_lblGenerateRandomGraph);

    textField = new JTextField();
    textField.setText("5");
    GridBagConstraints gbc_textField = new GridBagConstraints();
    gbc_textField.insets = new Insets(0, 0, 5, 5);
    gbc_textField.fill = GridBagConstraints.HORIZONTAL;
    gbc_textField.gridx = 1;
    gbc_textField.gridy = 2;
    contentPane.add(textField, gbc_textField);
    textField.setColumns(10);

    JButton btnGenerateRandomGraph = new JButton("Generate Random Graph");

    GridBagConstraints gbc_btnGenerateRandomGraph = new GridBagConstraints();
    gbc_btnGenerateRandomGraph.fill = GridBagConstraints.BOTH;
    gbc_btnGenerateRandomGraph.insets = new Insets(0, 0, 5, 0);
    gbc_btnGenerateRandomGraph.gridx = 3;
    gbc_btnGenerateRandomGraph.gridy = 2;
    contentPane.add(btnGenerateRandomGraph, gbc_btnGenerateRandomGraph);

    JLabel lblNearestNeighbor = new JLabel("Nearest Neighbor");
    GridBagConstraints gbc_lblNearestNeighbor = new GridBagConstraints();
    gbc_lblNearestNeighbor.anchor = GridBagConstraints.EAST;
    gbc_lblNearestNeighbor.insets = new Insets(0, 0, 5, 5);
    gbc_lblNearestNeighbor.gridx = 0;
    gbc_lblNearestNeighbor.gridy = 3;
    contentPane.add(lblNearestNeighbor, gbc_lblNearestNeighbor);

    JLabel lblNearestneighbordistance = new JLabel("");
    GridBagConstraints gbc_lblNearestneighbordistance = new GridBagConstraints();
    gbc_lblNearestneighbordistance.insets = new Insets(0, 0, 5, 5);
    gbc_lblNearestneighbordistance.gridx = 1;
    gbc_lblNearestneighbordistance.gridy = 3;
    contentPane.add(lblNearestneighbordistance, gbc_lblNearestneighbordistance);
    
    JLabel lblNearestneighbortime = new JLabel("");
    GridBagConstraints gbc_lblNearestneighbortime = new GridBagConstraints();
    gbc_lblNearestneighbortime.insets = new Insets(0, 0, 5, 5);
    gbc_lblNearestneighbortime.gridx = 2;
    gbc_lblNearestneighbortime.gridy = 3;
    contentPane.add(lblNearestneighbortime, gbc_lblNearestneighbortime);

    JButton btnNearestNeighbor = new JButton("Nearest Neighbor");
    btnNearestNeighbor.addMouseListener(new MouseAdapter() {
      @Override
      public void mouseReleased(MouseEvent e) {
        long startTime = System.nanoTime();
        System.out.println("Running nearestNeighborTsp() to compute TSP tour.");
        List<Edge> path = panel.graph.nearestNeighborTsp();
        long endTime = System.nanoTime();
        long timeDelta = (endTime - startTime) / 1000000;
        lblNearestneighbortime.setText(String.format("Time: %d ms", timeDelta));
        double distance = 0;
        for (Edge edge : path) {
          distance += edge.distance;
        }
        lblNearestneighbordistance.setText(String.format("Dist: %.2f", distance));
        panel.overlayEdges.put("nearest", path);
        repaint();
      }
    });
    GridBagConstraints gbc_btnNearestNeighbor = new GridBagConstraints();
    gbc_btnNearestNeighbor.fill = GridBagConstraints.BOTH;
    gbc_btnNearestNeighbor.insets = new Insets(0, 0, 5, 0);
    gbc_btnNearestNeighbor.gridx = 3;
    gbc_btnNearestNeighbor.gridy = 3;
    contentPane.add(btnNearestNeighbor, gbc_btnNearestNeighbor);

    JLabel lblBruteForce = new JLabel("Brute Force");
    GridBagConstraints gbc_lblBruteForce = new GridBagConstraints();
    gbc_lblBruteForce.anchor = GridBagConstraints.EAST;
    gbc_lblBruteForce.insets = new Insets(0, 0, 5, 5);
    gbc_lblBruteForce.gridx = 0;
    gbc_lblBruteForce.gridy = 4;
    contentPane.add(lblBruteForce, gbc_lblBruteForce);

    JLabel lblBruteforcedistance = new JLabel("");
    GridBagConstraints gbc_lblBruteforcedistance = new GridBagConstraints();
    gbc_lblBruteforcedistance.insets = new Insets(0, 0, 5, 5);
    gbc_lblBruteforcedistance.gridx = 1;
    gbc_lblBruteforcedistance.gridy = 4;
    contentPane.add(lblBruteforcedistance, gbc_lblBruteforcedistance);

    JLabel lblBruteforcetime = new JLabel("");
    GridBagConstraints gbc_lblBruteforcetime = new GridBagConstraints();
    gbc_lblBruteforcetime.insets = new Insets(0, 0, 5, 5);
    gbc_lblBruteforcetime.gridx = 2;
    gbc_lblBruteforcetime.gridy = 4;
    contentPane.add(lblBruteforcetime, gbc_lblBruteforcetime);

    JButton btnBruteForce = new JButton("Brute Force");
    btnBruteForce.addMouseListener(new MouseAdapter() {
      @Override
      public void mouseReleased(MouseEvent e) {
        long startTime = System.nanoTime();
        System.out.println("Running bruteForceTsp() to compute optimal TSP tour.");
        List<Edge> path = panel.graph.bruteForceTsp();
        long endTime = System.nanoTime();
        long timeDelta = (endTime - startTime) / 1000000;
        lblBruteforcetime.setText(String.format("Time: %d ms", timeDelta));
        double distance = 0;
        for (Edge edge : path) {
          distance += edge.distance;
        }
        lblBruteforcedistance.setText(String.format("Dist: %.2f", distance));
        panel.overlayEdges.put("brute", path);
        repaint();
      }
    });
    GridBagConstraints gbc_btnBruteForce = new GridBagConstraints();
    gbc_btnBruteForce.fill = GridBagConstraints.BOTH;
    gbc_btnBruteForce.insets = new Insets(0, 0, 5, 0);
    gbc_btnBruteForce.gridx = 3;
    gbc_btnBruteForce.gridy = 4;
    contentPane.add(btnBruteForce, gbc_btnBruteForce);

    JSeparator separator_1 = new JSeparator();
    separator_1.setForeground(Color.GRAY);
    separator_1.setBackground(Color.WHITE);
    GridBagConstraints gbc_separator_1 = new GridBagConstraints();
    gbc_separator_1.fill = GridBagConstraints.BOTH;
    gbc_separator_1.gridwidth = 4;
    gbc_separator_1.insets = new Insets(0, 0, 5, 0);
    gbc_separator_1.gridx = 0;
    gbc_separator_1.gridy = 5;
    contentPane.add(separator_1, gbc_separator_1);
    GridBagConstraints gbc_lblPanda = new GridBagConstraints();
    gbc_lblPanda.gridwidth = 3;
    gbc_lblPanda.anchor = GridBagConstraints.EAST;
    gbc_lblPanda.gridx = 1;
    gbc_lblPanda.gridy = 6;
    contentPane.add(lblPanda, gbc_lblPanda);

    btnGenerateRandomGraph.addMouseListener(new MouseAdapter() {
      @Override
      public void mouseReleased(MouseEvent e) {
        int n = 5;
        try {
          n = Integer.valueOf(textField.getText());
        } catch (NumberFormatException exception) {
          textField.setText("5");
          repaint();
        }
        if (n > 8) {
          Object[] options = { "Shut up Linan", "I'll change it" };
          int m = JOptionPane.showOptionDialog(panel,
              "You are about to generate " + n
                  + " vertices.\nDrawing this may slow down your computer. Running brute force algorithms on a graph\n"
                  + "" + "larger than 8 vertices will probably take forever.\nYour computer may flip out on strike."
                  + "\n\nAre you sure you want to do this?",
              "Don't be cruel to your computer", JOptionPane.YES_NO_OPTION, JOptionPane.WARNING_MESSAGE, null, options,
              options[1]);
          if (m == 1) {
            textField.setText("5");
            repaint();
            return;
          }
        }

        System.out.println("Resetting brute force and nearest neighbor paths");
        panel.overlayEdges = new HashMap<>();
        System.out.println("Calling generateRandomVertices(" + n + ")");
        panel.graph.generateRandomVertices(n);
        lblBruteforcedistance.setText("");
        lblNearestneighbordistance.setText("");

        panel.repaint();
      }
    });

    updateGraphPanel();
  }

  private void updateGraphPanel() {
    graph = graphFactory();
    panel.graph = graph;

    panel.overlayEdges.put("brute", new LinkedList<Edge>());
    panel.overlayEdges.put("nearest", new LinkedList<Edge>());

    repaint();
  }

  public class GraphPanel extends JPanel {

    // graph layout parameters
    public static final int VERTEX_RADIUS = 10;
    public static final int SPACE = 3;

    public static final int MARGIN_X = 50;
    public static final int MARGIN_Y = 50;

    public static final int DEFAULT_THICKNESS = 1;

    // scale factors
    public float xFactor, yFactor;

    public Graph graph;

    public HashMap<String, List<Edge>> overlayEdges;

    public GraphPanel(Graph graph) {
      this.graph = graph;
      overlayEdges = new HashMap<>();
      overlayEdges.put("brute", new LinkedList<Edge>());
      overlayEdges.put("nearest", new LinkedList<Edge>());
    }

    public void paintComponent(Graphics g) {
      // make everything smooth like butter
      Graphics2D g2 = (Graphics2D) g;
      g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
      g2.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
      g2.setRenderingHint(RenderingHints.KEY_DITHERING, RenderingHints.VALUE_DITHER_ENABLE);
      g2.setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
      g2.setRenderingHint(RenderingHints.KEY_FRACTIONALMETRICS, RenderingHints.VALUE_FRACTIONALMETRICS_ON);
      g2.setRenderingHint(RenderingHints.KEY_ALPHA_INTERPOLATION, RenderingHints.VALUE_ALPHA_INTERPOLATION_QUALITY);
      g2.setRenderingHint(RenderingHints.KEY_COLOR_RENDERING, RenderingHints.VALUE_COLOR_RENDER_QUALITY);
      g2.setRenderingHint(RenderingHints.KEY_STROKE_CONTROL, RenderingHints.VALUE_STROKE_PURE);

      // scale the graph
      int minX = 0;
      int maxX = 1;
      int minY = 0;
      int maxY = 1;
      for (Vertex v : graph.getVertices()) {
        if (v.x < minX)
          minX = v.x;
        if (v.x > maxX)
          maxX = v.x;
        if (v.y < minY)
          minY = v.y;
        if (v.y > maxY)
          maxY = v.y;
      }
      xFactor = (this.getBounds().width - 2 * MARGIN_X) / (float) (maxX - minX);
      yFactor = (this.getBounds().height - 2 * MARGIN_Y) / (float) (maxY - minY);
      super.paintComponent(g2); // paint the panel
      paintGraph(g2); // paint the graph
    }

    public void paintGraph(Graphics g) {
      for (Vertex v : graph.getVertices()) {
        for (Edge edge : v.adjacentEdges) {
          paintEdge(g, edge.source, edge.target, edge.distance, Color.LIGHT_GRAY, DEFAULT_THICKNESS, 255);
        }
      }
      for (Vertex v : graph.getVertices()) {
        paintVertex(g, v);
      }
      for (String overlayType : overlayEdges.keySet()) {
        if (overlayType.equals("brute")) {
          for (Edge edge : overlayEdges.get(overlayType)) {
            paintEdge(g, edge.source, edge.target, edge.distance, Color.RED, 8, 50);
          }
        }
        if (overlayType.equals("nearest")) {
          for (Edge edge : overlayEdges.get(overlayType)) {
            paintEdge(g, edge.source, edge.target, edge.distance, Color.GREEN, 8, 50);
          }
        }
      }
    }

    public void paintVertex(Graphics g, Vertex v) {
      Graphics2D g2 = (Graphics2D) g;

      int x = Math.round(xFactor * (float) v.x + (float) MARGIN_X);
      int y = Math.round(yFactor * (float) v.y + (float) MARGIN_Y);
      g2.setColor(Color.LIGHT_GRAY);
      Stroke oldStroke = g2.getStroke();
      g2.setStroke(new BasicStroke(4));
      g2.drawOval(x - VERTEX_RADIUS / 2, y - VERTEX_RADIUS / 2, VERTEX_RADIUS, VERTEX_RADIUS);
      g2.setStroke(oldStroke);
      g2.setColor(Color.LIGHT_GRAY);
      g2.fillOval(x - VERTEX_RADIUS / 2, y - VERTEX_RADIUS / 2, VERTEX_RADIUS, VERTEX_RADIUS);
      g2.setColor(Color.DARK_GRAY);
      g2.drawString(Integer.toString(v.name), x - VERTEX_RADIUS / 2, y + VERTEX_RADIUS / 2);
    }

    public void paintEdge(Graphics g, Vertex u, Vertex v, double weight, Color color, int thickness, int alpha) {
      Graphics2D g2 = (Graphics2D) g;
      int x1 = Math.round(xFactor * (float) u.x + (float) MARGIN_X);
      int y1 = Math.round(yFactor * (float) u.y + (float) MARGIN_Y);
      int x2 = Math.round(xFactor * (float) v.x + (float) MARGIN_X);
      int y2 = Math.round(yFactor * (float) v.y + (float) MARGIN_Y);
      g2.setColor(new Color(color.getRed(), color.getGreen(), color.getBlue(), alpha));
      Stroke oldStroke = g2.getStroke();
      g2.setStroke(new BasicStroke(thickness));
      g2.drawLine(x1, y1, x2, y2);
      g2.setStroke(oldStroke);
      Font oldFont = g2.getFont();
      g2.setFont(new Font("Helvetica", Font.PLAIN, 8));
      g2.setColor(Color.GRAY);
      g2.drawString(String.format("%.1f", weight), (x1 + x2) / 2, (y1 + y2) / 2);
      g2.setFont(oldFont);
    }
  }
}
