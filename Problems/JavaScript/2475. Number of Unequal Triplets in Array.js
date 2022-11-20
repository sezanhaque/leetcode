/**
 * @param {number[]} nums
 * @return {number}
 */
var unequalTriplets = function (nums) {
    let count = 0,
        prev = 0,
        nxt = nums.length;
    let frequencies = nums.reduce((count, currentValue) => {
        return (count[currentValue] ? ++count[currentValue] : (count[currentValue] = 1), count);
    }, {});

    for (freq of Object.values(frequencies)) {
        nxt -= freq;
        count += (prev * freq * nxt);
        prev += freq
    }
    return count
};

let tmp = [1, 3, 1, 2, 4]
unequalTriplets(tmp)