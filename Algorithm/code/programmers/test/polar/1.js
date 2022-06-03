// 출처: https://jun-choi-4928.medium.com/javascript%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-21df4b536349
const getCombinations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);

    results.push(...attached);
  });

  return results;
};

function backtrack(arr, k, t, n, idx, selected, count, sum, same) {
  if (sum > t) return;

  if (idx > n) return;

  if (k <= count && count <= n && !same) answer += 1;

  backtrack(
    arr,
    k,
    t,
    n,
    idx + 1,
    [...selected, arr[idx]],
    count + 1,
    sum + arr[idx],
    false
  );
  backtrack(arr, k, t, n, idx + 1, [...selected], count, sum, true);
}

var answer = 0;
function solution(arr, k, t) {
  n = arr.length;

  backtrack(arr, k, t, n, 0, [], 0, 0);

  return answer;
}

const answer1 = solution([2, 5, 3, 8, 1], 3, 11);
console.log(answer1);

// const answer2 = solution([1, 1, 2, 2], 2, 3);
// const answer3 = solution([1, 2, 3, 2], 2, 2);
// console.log(answer2)
// console.log(answer3)
