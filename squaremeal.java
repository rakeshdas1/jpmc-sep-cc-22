class Solution {
    public int countPairs(int[] deliciousness) {
        int good = 0;
        for (int i = 0; i < deliciousness.length - 1; i++) {
            for (int j = i + 1; j < deliciousness.length; j++) {
                int sum = deliciousness[i] + deliciousness[j];
                if (isFactor(sum)) {
                    good++;
                }
            }
        }
        
        return good;
    }
    
    private boolean isFactor(int n) {
        for(int i=0;;i++){
            if(n==Math.pow(2,i))return true;
            if(n<Math.pow(2,i))return false;
        }
    }
}
