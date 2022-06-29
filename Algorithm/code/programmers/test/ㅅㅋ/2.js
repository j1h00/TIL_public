function solution(numbers, K) {
  var len = numbers.length;
  var minCount = len * (len - 1);
  var visited = Array.from(Array(len), () => Array(len).fill(0));

  function check(numbers, K) {
    for (let i = 0; i < len - 1; i++) {
      const diff = numbers[i] - numbers[i + 1];
      if ((diff >= 0 ? diff : -diff) > K) {
        return false;
      }
    }
    return true;
  }

  function swap(numbers, i, j) {
    const newNumbers = numbers;
    [newNumbers[i], newNumbers[j]] = [newNumbers[j], newNumbers[i]];
    return newNumbers;
  }

  function dfs(currentNumbers, count, K) {
    if (count > minCount) {
      return;
    }

    const isValid = check(currentNumbers, K);
    if (isValid) {
      console.log("here", currentNumbers, count, minCount);
      minCount = minCount > count ? count : minCount;
      return;
    }

    for (let i = 0; i < len; i++) {
      for (let j = 0; j < len; j++) {
        if (i == j || visited[i][j]) {
          continue;
        }

        visited[i][j] = 1;
        dfs(swap(currentNumbers, i, j), count + 1, K);
        visited[i][j] = 0;
      }
    }
  }

  dfs(numbers, 0, K);
  console.log(minCount);
  return minCount;
}

// solution([10, 40, 30, 20], 20);
console.log("@@@@@@@@@@@@@@");
solution([3, 7, 2, 8, 6, 4, 5, 1], 3);
