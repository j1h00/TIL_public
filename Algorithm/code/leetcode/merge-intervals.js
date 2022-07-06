// https://leetcode.com/problems/merge-intervals/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => {
    if (a[0] > b[0]) return 1;
    else if (a[0] == b[0]) {
      if (a[1] > b[1]) return 1;
      return -1;
    }
    return -1;
  });

  let [start, end] = [intervals[0][0], intervals[0][1]];

  const mergedIntervals = [];

  for (let [a, b] of intervals) {
    if (a > end) {
      mergedIntervals.push([start, end]);
      start = a;
    }

    if (b > end) end = b;
  }

  mergedIntervals.push([start, end]);

  return mergedIntervals;
};

/*
#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#
*/

// most viewed
function merge(intervals) {
  if (!intervals.length) return intervals;
  intervals.sort((a, b) => a.start - b.start);
  var prev = intervals[0];
  var res = [prev];
  for (var curr of intervals) {
    if (curr[0] <= prev[1]) {
      prev[1] = Math.max(prev[1], curr[1]);
    } else {
      res.push(curr);
      prev = curr;
    }
  }
  return res;
}
