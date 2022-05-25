class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> stack = new Stack<>(); int stars=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                stack.push(0);
            }else if (s.charAt(i)==')')
                if(stack.size()==0 && stars>=1){
                    stars--;
                    
                } else{
                    
                    stack.pop();
                }
                else if(stack.size()==0 && stars==0)return false;
            if(s.charAt(i)=='*') stars++;
        }
        if (stack.size() != 0) {
            return false;
        }
        return true;
    }
}
