class Solution {
    public boolean hasSameDigits(String s) {
        int n=s.length();
       int arr[] = new int[n];
       for(int i=0;i<arr.length;i++){
        arr[i]=s.charAt(i)-'0';
               } 
    while(n>2){
        for(int i=0;i<n-1;i++){
            arr[i]=(arr[i]+arr[i+1])%10;

        }
        n--;
    }
    if(arr[0]==arr[1]){
        return true;
    }
    return false;
    }
}