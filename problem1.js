/**
 * @param {number[]} flowerbed
 * @param {number} n
 O(n) time complexity
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    
    let counter = 0;
    
    for (let i = 0; i < flowerbed.length; i++) {
        if(counter == n)
            break;
        if((i-1 < 0 || flowerbed[i-1] == 0) &&
          (i+1 == flowerbed.length || flowerbed[i+1] == 0) &&
          flowerbed[i] == 0) {
            counter = counter+1;
            flowerbed[i] = 1;
        }
    }
    return counter>=n;

};
