using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using Assignment1;

namespace code1
{
    class Sample
    {
        static void Main(string[] args)
        {
            var myString= "qux";

            //calling string extension method  for Check if an object of any type is included in a list of values provided
            bool myStringFound = myString.In("foo", "bar", "baz", "qux");
            if (myStringFound)
            {
                Console.WriteLine(myString + " found in the array");
            }
            else
            {
                Console.WriteLine(myString + " Not found in the array");
            }


            var myInt = 'z';

            //calling string extension method for Check the position of an object in a list of values provided
            int indexOfMyChar = myInt.Pos('x', 'y', 'z');
            Console.WriteLine("position of " + myInt + "  is " + indexOfMyChar);
            Console.ReadLine();
        }
    }
}
