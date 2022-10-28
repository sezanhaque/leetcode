/**
 * From Internet, using hashmap
 * @param {Array} numbers 
 * @param {int} target 
 * @returns {Array}
 * Solution : HashMap

    We need to find 2 numbers REMAINING, VALUE so that REMAINING + VALUE = TARGET.
    We need a HashMap data structure to store elements in the past, let name it seen.
    The idea is that we iterate b as each element in nums, we check if we found a (where REMAINING = TARGET - VALUE) in the past.
    If a exists in seen then we already found 2 numbers REMAINING and VALUE, so that REMAINING + VALUE = TARGET, just output their indices.
    Else add b to the seen.
 */
var twoSum = (numbers, target) => {
    let map = {};
    for (let i = 0; i < numbers.length; i++) {
        let remaining = target - numbers[i];
        if (remaining in map) {
            return [map[remaining] + 1, i + 1];
        }
        map[numbers[i]] = i;
    }
    return [];
};

const start = performance.now();
// console.log(twoSum([2, 11, 15, 4, 7, 1, 8], 9));
// console.log(twoSum([2, 7, 11, 15], 9));
// console.log(twoSum([3, 2, 4], 6));
// console.log(twoSum([3, 3], 6));
// console.log(twoSum([0, 4, 3, 0], 0));
// console.log(twoSum([-3, 4, 3, 90], 0));
// console.log(twoSum([-3, 4, 2, 90], 0));
console.log(twoSum([2, 7, 11, 15], 9));
const end = performance.now();
console.log(`Time took ${end - start} milliseconds.`);
