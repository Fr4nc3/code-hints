/* 
* @Fr4nc3
* Rectangle class 
* Programing Q1
*/
public class Rectangle implements Comparable<Rectangle> {
    private int width;
    private int length;

    public Rectangle(int length, int width) {
        this.length = length;
        this.width = width;
    }

    public int getLength() {
        return length;
    }

    public int getWidth() {
        return width;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    @Override
    public String toString() {
        return "\nlength: " + getLength() + "\nwidth: " + getWidth() + "\nperimeter: " + getPerimeter();
    }

    public int getPerimeter() {
        return 2 * (width + length);
    }

    @Override
    public int compareTo(Rectangle other) {
        if (this.getPerimeter() > other.getPerimeter()) {
            return 1;
        } else if (this.getPerimeter() < other.getPerimeter()) {
            return -1;
        } else {
            return 0;
        }
    }
}