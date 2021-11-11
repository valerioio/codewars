function regexDivisibleBy(n) {
  if (n === 1) return "^(0*1*)+$";
  if (n === 3) return "^(0*|1(01*0)*1)+$";
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
    let [i, o, k] = [[], [], 0];
    for (let ck = 1; ck <= graph.length - 2; ck++) {
      const [ci, co] = [[], []];
      for (const kk in graph) {
        if (graph[kk][ck] !== null && +kk !== ck) ci.push(kk);
        if (graph[ck][kk] !== null && +kk !== ck) co.push(kk);
      }
      if (ci.length * co.length < i.length * o.length || k === 0)
        [i, o, k] = [ci, co, ck];
    }
    const c = graph[k][k] === null ? "" : `(${graph[k][k]})*`;
    for (const x of i) {
      for (const y of o) {
        const regex = `${graph[x][k]}${c}${graph[k][y]}`;
        graph[x][y] =
          graph[x][y] === null ? regex : `(${graph[x][y]}|${regex})`;
      }
    }
    graph.splice(k, 1);
    for (const a of graph) a.splice(k, 1);
  }
  return "^" + graph[0][1] + z + "$";
}
