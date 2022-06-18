// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  N = A.length;

  let answer = 10 ** 9;
  for (let i = 0; i < N - K + 1; i++) {
    const curArray = [...A.slice(0, i), ...A.slice(i + K, N)];
    const amplitude = Math.max(...curArray) - Math.min(...curArray);
    if (answer > amplitude) answer = amplitude;
  }
  return answer;
}
