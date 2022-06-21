function solution(N, bus_stop) {
  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  let city = Array.from(Array(N), () => Array(N).fill(0));
  let visited = Array.from(Array(N), () => Array(N).fill(0));

  let q = [];
  bus_stop.forEach(([r, c]) => {
    q.push([r - 1, c - 1]);
    visited[r - 1][c - 1] = 1;
  });

  while (q.length) {
    let [x, y] = q.shift();
    directions.forEach(([dx, dy]) => {
      let nx = x + dx;
      let ny = y + dy;

      if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
        city[nx][ny] = city[x][y] + 1;
        visited[nx][ny] = 1;
        q.push([nx, ny]);
      }
    });
  }

  return city;
}

const answer1 = solution(3, [[1, 2]]);
console.log(answer1);

const answer2 = solution(3, [
  [1, 2],
  [3, 3],
]);
console.log(answer2);
