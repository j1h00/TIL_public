function solution(A) {
  var n = A.length;
  var i = n - 1;
  var result = -1;
  var maximal = 0,
    k = 0;
  while (i > 0) {
    if (A[i] == 1) {
      k = k + 1;
      if (k >= maximal) {
        maximal = k;
        result = i;
      }
    } else k = 0;
    i = i - 1;
  }
  if (A[i] == 1 && k + 1 >= maximal) result = 0;
  return result;
}
