var findMedianSortedArrays = function (nums1, nums2) {
    const arr = [...nums1, ...nums2].sort((a, b) => a - b);

    if (arr.length % 2 === 0) {
        return (arr[arr.length / 2 - 1] + arr[arr.length / 2]) / 2;
    }

    return arr[Math.floor(arr.length / 2)];
};

console.log(findMedianSortedArrays([3], [-2, -1]));
console.log(findMedianSortedArrays([2, 4, 6], [1, 3, 5]));