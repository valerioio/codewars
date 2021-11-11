function balancedParens(n) {
  const result = [];
  const stack = [["", n, 0]];
  while (stack.length) {
    const [str, open, close] = stack.pop();
    if (open) stack.push([str + "(", open - 1, close + 1]);
    if (close) stack.push([str + ")", open, close - 1]);
    if (!(open || close)) result.push(str);
  }
  return result;
}
