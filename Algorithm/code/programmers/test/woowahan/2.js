function solution(scores) {
  var answer = [];
  let totalScoreOne = 0;
  let totalScoreTwo = 0;
  const totalScores = [];

  for (let i = 0; i < scores.length; i++) {
    let [one, two] = scores[i];
    totalScoreOne = one;
    totalScoreTwo = two;

    totalScores.push([i + 1, one + two]);
  }

  console.log(totalScores);
}

const answer1 = solution([
  [85, 90],
  [65, 67],
  [88, 87],
  [88, 87],
  [73, 81],
  [65, 89],
  [99, 100],
  [80, 94],
]);
console.log("answer1: ", answer1);
