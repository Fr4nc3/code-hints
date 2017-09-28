using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace code1
{
  
    public static class MyExtensions
    {
        public static bool In(this string str, params string[] strings)
        {
            List<string> strList=new List<string>();
            foreach (var VARIABLE in strings)
            {
                strList.Add(VARIABLE);
            }

            return strList.Contains(str);
        }

        public static int Pos(this char c, params char[] chars)
        {
            List<char> charList = new List<char>();
            foreach (var VARIABLE in chars)
            {
                charList.Add(VARIABLE);
            }

            return charList.IndexOf(c);
        }    
    }
}
