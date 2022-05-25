class Solution {
    public boolean checkValidString(String s) {
        int lcount = 0;
        int rcount = 0;
        int wildcard = 0;
        
        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            if(curChar == '('){
                lcount++;
            }
            else if(curChar == ')'){
                rcount++;
            }
            else{
                wildcard++;
            }
            if(rcount > lcount){
                if(wildcard>0){
                    lcount++;
                    wildcard--;
                }
                else{
                    return false;
                }
            }
            
        }
        //System.out.println(lcount);
        //System.out.println(rcount);
        if(lcount > rcount){
            return false;
        }
        return true;
    }