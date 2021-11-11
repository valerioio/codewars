function formatDuration(seconds) {
  if (seconds === 0) return "now";
  let ans = [];
  const units = [
    ["year", 86400 * 365],
    ["day", 86400],
    ["hour", 3600],
    ["minute", 60],
    ["second", 1],
  ];
  for (const [u, s] of units) {
    const a = Math.floor(seconds / s);
    if (a) {
      ans.push(a + " " + u + (a === 1 ? "" : "s"));
      ans.push(", ");
    }
    seconds %= s;
  }
  ans.pop();
  ans[ans.length - 2] = " and ";
  return ans.join("");
}
