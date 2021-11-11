snail = function (array) {
  const res = [];
  let [x, y] = [0, 0];
  let k = 0;
  const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const edg = [array.length - 1, array.length - 1, 0, 1];
  for (let n = array[0].length ** 2; n > 0; n--) {
    res.push(array[x][y]);
    if ([y, x][k % 2] === edg[k]) {
      edg[k] -= dir[k][0] + dir[k][1];
      k = (k + 1) % 4;
    }
    x += dir[k][0];
    y += dir[k][1];
  }
  return res;
};
