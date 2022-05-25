/**
 * @param {string} s
 * @return {boolean}
 O(n) time complexity
 */
var checkValidString = function(s) {
    let leftParens = 0;
    let varience = 0;
    for(let i = 0; i < s.length; i++) {
        let c = s[i];
        if(c == '(')
            leftParens++;
        else if(c == ')')
            leftParens--;
        else if(c == '*') 
            varience++;
        
        if(leftParens < 0) {
            if(varience > 0) {
                leftParens++;
                varience--;
            }
            else
                return false;
        }
    }
    
    console.log(leftParens, varience)
    
    return leftParens == 0 || leftParens - varience <= 0;
};
