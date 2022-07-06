// https://leetcode.com/problems/largest-number/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function (nums) {
  if (nums.reduce((total, cur) => total + cur) === 0) return "0";

  const strs = nums.map((num) => "" + num);
  return strs
    .sort((a, b) => (a + b > b + a ? 1 : -1))
    .reverse()
    .join("");
};

/*
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#
*/

// replace starts with 0
function largestNumber(num) {
  return (
    num
      .sort(function (a, b) {
        return b + "" + a - (a + "" + b);
      })
      .join("")
      .replace(/^0*/, "") || "0"
  );
}
