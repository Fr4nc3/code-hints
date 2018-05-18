using System;
using consoleApp.Extensions;
using System.Collections.Generic;
using System.Linq;


namespace consoleApp
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var myStatus = Status.EXPIRED;
            var myFruitFound = myStatus.In(Status.NEW, Status.MODIFIED);

            Console.WriteLine("found: " + myFruitFound);

            var myString = "vvv";
            var myStringFound = myString.In("foo", "bar", "baz", "qux");

            Console.WriteLine("found: " + myStringFound);

            var myInt = 8;
            var indexOfMyInt = myInt.Pos(3, 8, 11, 9);

             Console.WriteLine("index: " + indexOfMyInt);

            var myChar = 'v';
            var indexOfMyChar = myChar.Pos('x', 'y', 'z');

            Console.WriteLine("index: " + indexOfMyChar);
            int n = 12340;
            int left = n;
            int rev = 0;
            while (left > 0)
            {
                int r = left % 10;
                Console.WriteLine("r: "+r);
                rev = rev * 10 + r;
                left = left / 10;  //left = Math.floor(left / 10); 
                Console.WriteLine("left: "+left);
            }
            var list = "hello this is nyc".Split(' ').AsEnumerable();
            list.OrderByDescending(x => x.Length).ToList()
                .ForEach(s => Console.WriteLine(s+ " "+s.Length));
            //Console.WriteLine();

            Console.WriteLine(rev);
        }
    }
}
