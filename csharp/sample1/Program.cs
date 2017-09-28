
/*
    1. Write the In and Pos methods to:

        a.  Check if an object of any type is included in a list of values provided

            ie: var myFruitFound = myFruit.In(MyFruitEnum.Orange, MyFruitEnum.Banana)

            OR var myStringFound = myString.In(“foo”, “bar”, “baz”, “qux”)

        a.  Check the position of an object in a list of values provided

            ie: var indexOfMyInt = myInt.Pos(3, 8, 11, 9)

            OR var indexOfMyChar = myChar.Pos(‘x’,’y’,’z’)
*/

namespace Msft
{
    using Extensions;

    public class Program
    {
        // please see GenericExtensionsTests.cs for unit tests
        public static void Main(string[] args)
        {
            var myFruit = MyFruitEnum.Orange;
            var myFruitFound = myFruit.In(MyFruitEnum.Orange, MyFruitEnum.Banana);

            System.Console.WriteLine("found: " + myFruitFound);

            var myString = "vvv";
            var myStringFound = myString.In("foo", "bar", "baz", "qux");

            System.Console.WriteLine("found: " + myStringFound);

            var myInt = 8;
            var indexOfMyInt = myInt.Pos(3, 8, 11, 9);

            System.Console.WriteLine("index: " + indexOfMyInt);

            var myChar = 'v';
            var indexOfMyChar = myChar.Pos('x', 'y', 'z');

            System.Console.WriteLine("index: " + indexOfMyChar);
        }
    }
}
