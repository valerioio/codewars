var spiralize = function (size) {
  const row = Array(size).fill(0);
  const spiral = [];
  for (const _ in row) spiral.push([...row]);
  spiral[0] = Array(size).fill(1);
  const increment = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let direction = 1;
  let [x, y] = [0, size - 1];
  let steps = size - 1;
  while (steps > 0) {
    for (let _k1 = 0; _k1 < 2; _k1++) {
      const [i, j] = increment[direction];
      for (let _k2 = 0; _k2 < steps; _k2++) {
        spiral[x][y] = 1;
        x += i;
        y += j;
      }
      direction = (direction + 1) % 4;
    }
    steps -= 2;
  }
  if (size % 2) spiral[x][y] = 1;
  return spiral;
};
