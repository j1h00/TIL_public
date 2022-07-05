// https://leetcode.com/problems/valid-palindrome/

/**
 * @param {string} s
 * @return {boolean}
 */
function isPalindrome(s) {
  const regex = /[^a-z0-9]/gi;
  const newString = s.replace(regex, "").toLowerCase();

  let i = 0;
  let j = newString.length - 1;

  while (i <= j) {
    if (newString[i] !== newString[j]) {
      return false;
    }
    i++;
    j--;
  }

  return true;
}
