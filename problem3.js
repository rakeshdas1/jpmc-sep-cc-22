/**
 * @param {number[]} deliciousness
 * @return {number}
 O(n^2) time complexity
 */
var countPairs = function(deliciousness) {    
    let map = deliciousness.reduce((a, c) => {
        let key = c.toString()
        if (a[key]) {
            a[key]++;
        } else {
            a[key] = 1;
        }
        return a;
    }, {})
    

    let result = 0;
    
    let a = Object.entries(map);
    
    if (map['1'] && map['1'] > 1) {
        result += map['1']
    }
    
    for (let i = 0; i < a.length; i++) {
                
        let [ki, vi] = a[i];
    
        
        for (let j = i + 1; j < a.length; j++) {
            
            let [kj, vj] = a[j];
            
            let total = Math.log2(parseInt(kj) + parseInt(ki));

            if (Number.isInteger(total)) {
                
                result += (parseInt(vi) * parseInt(vj))
                
            }
            
        }
        
    }
    
    return result;

};
