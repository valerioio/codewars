function getPINs(observed) {
  let ans = [""];
  let temp = [];
  const adj = [
    "08",
    "124",
    "1235",
    "236",
    "1457",
    "24568",
    "3569",
    "478",
    "05789",
    "689",
  ];
  for (const d of observed) {
    for (const a of adj[d]) for (const p of ans) temp.push(p + a);
    ans = temp;
    temp = [];
  }
  return ans;
}
