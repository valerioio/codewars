function validSolution(board) {
  const range = "012345678";
  const isInvalid = (a) => a.sort().join("") !== "123456789";
  for (const i of range) {
    const [row, column, square] = [[], [], []];
    for (const j of range) {
      row.push(board[i][j]);
      column.push(board[j][i]);
      square.push(board[3 * ~~(i / 3) + ~~(j / 3)][3 * (i % 3) + (j % 3)]);
    }
    if (isInvalid(row) || isInvalid(column) || isInvalid(square)) return false;
  }
  return true;
}
