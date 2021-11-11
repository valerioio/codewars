function solution(input, markers) {
  let stripped = [];
  input = input.split("\n");
  for (const i in input) {
    for (const j in input[i]) {
      if (markers.includes(input[i][j])) {
        stripped.push(input[i].slice(0, j).trimEnd());
        break;
      }
    }
    if (stripped.length == i) stripped.push(input[i].trimEnd());
  }
  return stripped.join("\n");
}
