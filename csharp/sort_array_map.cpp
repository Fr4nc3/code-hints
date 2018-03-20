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
        "system.load.1|1|host:a,role:web,availability-zone:us-east-1a",
        "system.load.15|1|host:b,role:web,availability-zone:us-east-1b",
        "system.cpu.user|20|host:a,role:web,availability-zone:us-east-1a",
        "postgresql.locks|12|host:c,role:db,db_role:master,availability-zone:us-east-1e",
        "postgresql.db.count|2|host:d,role:db,db_role:replica,availability-zone:us-east-1a",
        "kafka.consumer.lag|20000|host:e,role:intake,availability-zone:us-east-1a",
        "kafka.consumer.offset|3000000|host:e,role:intake,availability-zone:us-east-1a",
        "kafka.broker.offset|25000|host:f,role:kafka,availability-zone:us-east-1a"
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
