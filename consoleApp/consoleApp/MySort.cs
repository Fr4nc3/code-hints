using System;
using consoleApp.Extensions;
using System.Collections.Generic;
using System.Linq;
namespace consoleApp
{
    public class MySort
    {
        public static void Main(string[] args)
        { 
        



        }
        /*
        Given a partially-ordered(*) integer matrix and an integer value, find the coordinates of an instance of the value in the matrix, or a value specifying "not found":
         
        * - The partial ordering in question is: Ordered going down a column and ordered going across a row, but no order 
        ordering structure.
          
        |  1   2   3   4  |
        |  2   4   6   8  |
        |  3   5   7  10  |
        | 12  13  14  15  |
          
        <TResult> FindValue(<T1> matrix, <T2> value)
        {
           //Code
        } 
        */
        static public List<int> binarySearch(int[][] matrix, int v){

            List<int> result = new List<int>();
            if (matrix.Length == 0)
            {
                return result;
            }
            //nlogn 
            for (int i = 0; i < matrix.Length; ++i)
            {

                int l = 0;
                int r = matrix[i].Length - 1;

                while (l < r)
                {
                    int mid = (l + r) / 2;

                    if (matrix[i][mid] < v)
                    {
                        l = mid + 1;


                    }
                    else
                    { 
                        r = mid;

                    }


                }
                if(matrix[i][l]== v){
                    result.Add(i);
                    result.Add(l);
                    return result;
                }
            }
            return result;


        }
        static public List<int> FindValue(int[][] matrix, int v)
        {
            List<int> result = new List<int>();
            if (matrix.Length == 0)
            {
                return result;
            }

            int xLeng = matrix.Length;
            int yLeng = matrix[0].Length;


            //

            // n^2
            for (int i=0; i < xLeng; ++i)
            {
                for (int j=0; j < yLeng; ++j)
                {

                    //if(matrix[i].contains(v))
                    if (matrix[i][j] == v)
                    {
                        result.Add(i);
                        result.Add(j);
                        return result;

                    }
                }


            }


            return result;
        }

 }
