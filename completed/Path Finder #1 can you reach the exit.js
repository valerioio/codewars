function pathFinder(maze) {
  maze = maze.split("\n");
  for (const index in maze) {
    maze[index] = [...maze[index]];
  }
  const stack = [[0, 0]];
  maze[0][0] = "W";
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  while (stack.length) {
    const [y, x] = stack.pop();
    if (x === maze[0].length - 1 && y === maze.length - 1) {
      return true;
    }
    for (const index in directions) {
      const newX = x + directions[index][1];
      const newY = y + directions[index][0];
      if (
        newX >= 0 &&
        newY >= 0 &&
        newX < maze[0].length &&
        newY < maze.length
      ) {
        if (maze[newY][newX] === ".") {
          stack.push([newY, newX]);
          maze[newY][newX] = "W";
        }
      }
    }
  }
  return false;
}
