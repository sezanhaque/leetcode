/**
 * Using hashmap with recursion
 * @param {Array} nums 
 * @param {int} target 
 * @returns {Array}
 * Solution : HashMap

    We need to find 2 numbers REMAINING, VALUE so that REMAINING + VALUE = TARGET.
    We need a HashMap data structure to store elements in the past, let name it seen.
    The idea is that we iterate b as each element in nums, we check if we found a (where REMAINING = TARGET - VALUE) in the past.
    If a exists in seen then we already found 2 numbers REMAINING and VALUE, so that REMAINING + VALUE = TARGET, just output their indices.
    Else add b to the seen.
 */

let remaining = 0;
let seen = {};

var twoSum = (nums, target) => {
    remaining = 0;
    seen = {};
    return myRecursion(nums, target, 0);
};

// Recursion function
var myRecursion = (nums, target, length) => {
    if (length < nums.length) {
        remaining = target - nums[length];
        if (remaining in seen) {
            return [seen[remaining], length];
        }
        seen[nums[length]] = length;
        return myRecursion(nums, target, length + 1);
    } else {
        return [];
    }
};

const start = performance.now();
console.log(twoSum([2, 11, 15, 4, 7, 1, 8], 9));
console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
console.log(twoSum([0, 4, 3, 0], 0));
console.log(twoSum([-3, 4, 3, 90], 0));
console.log(twoSum([-3, 4, 2, 90], 0));
const end = performance.now();
console.log(`Time took ${end - start} milliseconds.`);
                                                                                                                                                                         