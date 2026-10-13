class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer,Integer> hash = new HashMap<>();
        for(int i = 0;i<arr.length;i++){
            if(hash.containsKey(arr[i])){
                hash.put(arr[i],hash.get(arr[i])+1);
            }else{
                hash.put(arr[i],1);
            }
        }
        for(int i = 0;i<arr.length-1;i++){
        for(int j = i+1;j<arr.length;j++){
            if(arr[i]!=arr[j] && hash.get(arr[i])==hash.get(arr[j])){
                return false;
            }
        }
    }
      return true;
        
    }
}