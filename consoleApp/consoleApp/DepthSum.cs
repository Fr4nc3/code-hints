using System;
namespace consoleApp
{
    public class DepthSum
    {
        public DepthSum()
        {
        }

		/**
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
 * For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
 * Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
 */
        public int depthSum (List<NestedInteger> input)
        {
            //Implementation here

            int level= 1;
                 depthSum(input, level);

        }

        //O(n)? n -> 2^n
        public int depthSum(List<NestedInteger> input, int level){
            int sum = 0;
            ++level;
            for(NestedInteger i: input){
                if(i.isInteger()){
                   sum += (i*level); 
                }else{
                    sum+= depthSum(i, level);
                
                }
            }
            return sum;

        }
    /**
     * This is the interface that represents nested lists.
     * You should not implement it, or speculate about its implementation.
     */
    public interface NestedInteger
    {
        /** @return true if this NestedInteger holds a single integer, rather than a nested list */
        boolean isInteger();
     
        /** @return the single integer that this NestedInteger holds, if it holds a single integer
         * Return null if this NestedInteger holds a nested list */
        Integer getInteger();
     
        /** @return the nested list that this NestedInteger holds, if it holds a nested list
         * Return null if this NestedInteger holds a single integer */
        List<NestedInteger> getList();
    }

    }
}
