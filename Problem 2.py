class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        //while able to place flower, place and remove flower
        //after while, if flower amount is > 0, return false
        //
        int sizeBed = flowerbed.length;
        
        for(int i = 0; i< sizeBed; i++){
            //System.out.println(flowerbed[i]);
            if(flowerbed[i] == 0){
                if(i > 0 && flowerbed[i-1] != 0){
                    continue;
                }
                if(i < sizeBed-1 && flowerbed[i+1] != 0){
                    continue;
                }
                
                //if(flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                    flowerbed[i] = 1;
                    n--;
                
            }
            
        }
        System.out.println(n);
        if(n >0){
            return false;
        }
        return true;
        
    }
}