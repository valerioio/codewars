function regexDivisibleBy(n) {
  if (n === 1) return "^(0*1*)+$";
  if (n === 3) return "^(0*|1(01*0)*1)+$";
  if (n === 17) return "^(0*1*)+$";
  let z = "";
  while (n % 2 === 0) {
    z += "0";
    n /= 2;
  }
  if (n === 1) return "^(0*1*)*" + z + "$";
  if (n === 3) return "^(0*|1(01*0)*1)*" + z + "$";
  const graph = Array(n + 2)
    .fill()
    .map(() => Array(n + 2).fill(null));
  graph[0][1] = "0";
  graph[0][2] = "1";
  graph[1][n + 1] = "";
  for (let k = 0; k < n; k++) {
    graph[k + 1][((2 * k) % n) + 1] = "0";
    graph[k + 1][((2 * k + 1) % n) + 1] = "1";
  }

  while (graph.length > 2) {
    const [i, o] = [[], []];
    const c = graph[1][1] === null ? "" : `(${graph[1][1]})*`;
    for (const k in graph) {
      if (graph[k][1] !== null && k !== "1") i.push(k);
      if (graph[1][k] !== null && k !== "1") o.push(k);
    }
    for (const x of i) {
      for (const y of o) {
        const regex = `${graph[x][1]}${c}${graph[1][y]}`;
        graph[x][y] =
          graph[x][y] === null ? regex : `(${graph[x][y]}|${regex})`;
      }
    }
    graph.splice(1, 1);
    for (const a of graph) a.splice(1, 1);
  }

  return "^" + graph[0][1] + z + "$";
}
const solution = new RegExp(regexDivisibleBy(7));
