class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        
        //sort by end time asc order and start time desc order
        Arrays.sort(intervals, (a, b) -> {
            if (a[1] != b[1]) {     // end time ascending
                return a[1] - b[1];
            }
            return b[0] - a[0];      // start time descending
            });

        int p1=-1,p2=-1; //default value
        int result=0;
        
        for(int[] interval: intervals){
            int start = interval[0];
            int end = interval[1];
            if(p2 < start){
                result = result+2;
                p1 = end-1;
                p2 = end;
            }
            else if(p1 < start){
                result++;
                p1=p2;
                p2=end;
            }
        }
        return result;

    }
} 

