using System;
using System.Linq;


namespace Question1
{

    /// <summary>
    /// Question 1. Write the In and Pos methods to:
    //a.	Check if an object of any type is included in a list of values provided
    //ie: var myFruitFound = myFruit.In(MyFruitEnum.Orange, MyFruitEnum.Banana)
    //OR var myStringFound = myString.In(“foo”, “bar”, “baz”, “qux”)
    //a.Check the position of an object in a list of values provided
    //ie: var indexOfMyInt = myInt.Pos(3, 8, 11, 9)
    //OR var indexOfMyChar = myChar.Pos(‘x’,’y’,’z’)

    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            var numList = new int[] { 3, 8, 11, 9 };
            var stringList = new string[] { "foo", "bar", "baz", "qux" };

            int myInt = 11;
            string myString = "Bar";

            //Checking a string which exists in the list
            Console.WriteLine(string.Format("Found string '{0}' : {1}", myString, myString.In(stringList).ToString()));

            //Checking a string which does not exists in the list
            Console.WriteLine(string.Format("Found string '{0}' : {1}", "star", "star".In(stringList).ToString()));

            //Checking a number which exists in the list
            Console.WriteLine(string.Format("Position of number '{0}' in the list is '{1}'", myInt, myInt.Pos(numList)));

            //Checking a number which does not exists in the list
            Console.WriteLine(string.Format("Position of number '{0}' in the list is '{1}'", 1, 1.Pos(numList)));

            Console.ReadLine();         
        } 
    }


    public static class ExtensionHelper
    {
        /// <summary>
        /// Return the position if the number exists in the list
        /// </summary>
        /// <param name="num"></param>
        /// <param name="numList"></param>
        /// <returns></returns>
        public static int Pos(this int num, int[] numList)
        {
            return Array.FindIndex(numList, i => i == num);
        }

        /// <summary>
        /// Checks if the string exists in the list or not
        /// </summary>
        /// <param name="str"></param>
        /// <param name="stringList"></param>
        /// <returns></returns>
        public static bool In(this string str, string[] stringList)
        {
            return stringList.Any(s => s.ToLower() == str.ToLower());
        }
    }
}
