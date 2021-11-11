function validateBattlefield(field) {
  const ships = [0, 4, 3, 2, 1];
  for (let i in field) {
    for (let j in field) {
      if (field[i][j]) {
        i = parseInt(i);
        j = parseInt(j);
        let count = 1;
        let x;
        let y;
        if (field[i + 1] && field[i + 1][j] && field[i][j + 1]) return false;
        else if (field[i + 1] && field[i + 1][j]) [x, y] = [1, 0];
        else if (field[i][j + 1]) [x, y] = [0, 1];
        field[i][j] = 0;
        if (field[i + 1] && (field[i + 1][j - 1] || field[i + 1][j + 1]))
          return false;
        while (field[i + x] && field[i + x][j + y]) {
          count++;
          field[i + x][j + y] = 0;
          if (
            field[i + x + 1] &&
            (field[i + x + 1][j + y - 1] || field[i + x + 1][j + y + 1])
          )
            return false;
          if (field[i + x + +!x] && field[i + x + +!x][j + y + +!y])
            return false;
          x ? x++ : y++;
        }
        ships[count]--;
      }
    }
  }
  return ships.join("") === "00000";
}
