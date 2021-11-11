function nextSmaller(n) {
  n = n.toString();
  for (let i = n.length - 1; i > 0; i--)
    if (n[i - 1] > n[i])
      for (let j = n.length - 1; j >= i; j--)
        if (n[j] < n[i - 1]) {
          const result =
            n.slice(0, i - 1) +
            n[j] +
            Array.from(n.slice(i - 1, j) + n.slice(j + 1))
              .sort()
              .reverse()
              .join("");
          return result[0] === "0" ? -1 : parseInt(result);
        }
  return -1;
}
