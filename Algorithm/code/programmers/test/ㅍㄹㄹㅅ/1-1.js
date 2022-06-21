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

function add(a, b) {
  return parseInt(a) + parseInt(b);
}

function solution(arr, k, t) {
  n = arr.length;
  let combs = [];
  for (let i = k; i < n; i++) {
    combs.push(...getCombinations(arr, i));
  }
  let filteredCombs = combs.filter((subset) => subset.reduce(add, 0) <= t);

  let numDict = {};
  arr.forEach((num) => {
    if (num in numDict) {
      numDict[num] += 1;
    } else {
      numDict[num] = 1;
    }
  });

  let param = 1;
  Object.values(numDict).forEach((count) => {
    if (count > 1) {
      param *= count;
    }
  });

  return filteredCombs.length * param;
}

const answer1 = solution([2, 5, 3, 8, 1], 3, 11);
console.log(answer1);
