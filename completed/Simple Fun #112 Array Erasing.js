function arrayErasing(arr) {
  let str = arr
    .reduce(
      (acc, cur) => {
        cur === acc[acc.length - 1][0]
          ? acc[acc.length - 1][1]++
          : acc.push([cur, 1]);
        return acc;
      },
      [[arr[0], 0]]
    )
    .map((i) => (i[1] > 1 ? 1 : 0))
    .join("");
  let left = str.slice(0, Math.ceil(str.length / 2)).lastIndexOf(1);
  let right = str.slice(Math.floor(str.length / 2)).indexOf(1);
  let b;
  if (left === -1 && right === -1) b = 0;
  else if (left === -1 || right === -1) {
    b = 1;
    if (
      str.length % 2 === 0 &&
      ((left === -1 && right === 0) ||
        (right === -1 && left === str.length / 2 - 1))
    )
      b = 0;
  } else {
    right += Math.floor(str.length / 2);
    b = Boolean(2 * right - 2 * left > str.length);
  }
  return Math.floor(str.length / 2) + 1 + b;
}
