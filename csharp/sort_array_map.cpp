using System;
using System.Collections.Generic;

// To execute C#, please define "static void Main" on a class
// named Solution.

// C#


class Solution
{
    
    static void Main(string[] args)
    {
        string[] stream = {

         };
        
     var myDic = new Dictionary<string,int>();
        foreach(var s in stream){
           var arr = s.Split('|'); 
           var tags = arr[2].Split(',');
           
           foreach(var t in tags){
                
               if(myDic.ContainsKey(t)){
                 myDic[t]= myDic[t]+1;
               
               } else {
                 myDic.Add(t,1);
               }
            
            
            }
        
        }
        
        //myDic.OrderBy(x=> x.Key).ThenBy(x=> x.Value);
      
        foreach(var d in myDic.OrderBy(x=> x.Key).ThenBy(x=> x.Value)){
            Console.WriteLine(d.Value.ToString() + " " + d.Key);

        }

    }
}
