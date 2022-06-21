var symbolDict = {
  0: ["O", "()"],
  1: ["I"],
  2: ["Z", "S", "7_"],
  3: ["E", "B"],
  4: ["A"],
  5: ["Z", "S"],
  6: ["b", "G"],
  7: ["T", "Y"],
  8: ["B", "E3"],
  9: ["g", "q"],
};

var result = [];

function DFS(word, replaced, used, count) {
  if ( count >= word.length ) {
    result.push(replaced);
  }

  const nowChr = word[count];
  const candidates = symbolDict[nowChr];

  for (let i = 0; i < candidates.length)
}