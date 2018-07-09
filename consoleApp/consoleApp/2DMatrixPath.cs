using System;
namespace consoleApp
{
    public class _DMatrixPath
    {
        // to find the path from
        // top left to bottom right
        static bool isPath(int[,] arr)
        {
            // set arr[0][0] = 1
            arr[0, 0] = 1;

            // Mark reachable (from top left) nodes
            // in first row and first column.
            for (int i = 1; i < 5; i++)
                if (arr[0, i] != -1)
                    arr[0, i] = arr[0, i - 1];
            
            for (int k = 0; k < 5; ++k){
                for (int t = 0; t < 5; ++t)
                { 
                    Console.Write(arr[k,t]);
                }
                Console.WriteLine("");
            }
            Console.WriteLine("change");
            for (int j = 1; j < 5; j++)
                if (arr[j, 0] != -1)
                    arr[j, 0] = arr[j - 1, 0];

            for (int k = 0; k < 5; ++k)
            {
                for (int t = 0; t < 5; ++t)
                {
                    Console.Write(arr[k, t]);
                }
                Console.WriteLine("");
            }
            // Mark reachable nodes in
            // remaining matrix.
            for (int i = 1; i < 5; i++)
                for (int j = 1; j < 5; j++)
                    if (arr[i, j] != -1)
                        arr[i, j] = Math.Max(arr[i, j - 1],
                                            arr[i - 1, j]);
            Console.WriteLine("change");
            for (int k = 0; k < 5; ++k)
            {
                for (int t = 0; t < 5; ++t)
                {
                    Console.Write(arr[k, t]);
                }
                Console.WriteLine("");
            }
            // return yes if right 
            // bottom index is 1
            return (arr[5 - 1, 5 - 1] == 1);
        }

        //Driver code 
        public static void Main()
        {
            // Given array
            //int[,] arr = { { 0, 0, 0, -1, 0 },
                        //{ -1, 0, 0, -1, -1 },
                        //{ 0, 0, 0, -1, 0 },
                        //{ -1, 0, -1, 0, -1 },
                        //{ 0, 0, -1, 0, 0 } };
           int[,] arr = { { 0, 0, 0, -1, 0},
                  { -1, 0, 0, -1, -1},
                  { 0, 0, 0, -1, 0},
                  { -1, 0, 0,  0, 0},
                  { 0, 0, -1,  0, 0}
            };

            // path from arr[0][0] 
            // to arr[row][col]
            if (isPath(arr))
                Console.WriteLine("Yes");
            else
                Console.WriteLine("No");
        }
    
    }
}
