// https://leetcode.com/problems/valid-palindrome/

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const regex = /[^a-z0-9]/gi;
  const newString = s.replace(regex, "").toLowerCase();

  i = 0;
  j = newString.length - 1;

  while (i <= j) {
    if (newString[i] !== newString[j]) {
      return false;
    }
    i++;
    j--;
  }

  return true;
};
