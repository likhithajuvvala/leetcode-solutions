class Solution {
    public void rotate(int[][] matrix) {
        //reverse
        int n=matrix.length;
        for(int i=0;i<n;i++){
            int a=0;
            int b=n-1;
            while(a<=b){
               int temp=matrix[a][i];
                matrix[a][i]=matrix[b][i];
                matrix[b][i]=temp;
                a++;
                b--;
            }
        }

        //transpose
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                int temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
            }
        }
    }
}