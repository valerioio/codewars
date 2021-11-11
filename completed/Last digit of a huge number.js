function lastDigit(as) {
  as = as.concat([1, 1, 1, 1, 0, 1]);
  const firstZero = as.findIndex((n) => n === 0);
  const zeros = as.slice(firstZero).findIndex((n) => n > 0);
  as.splice(firstZero, zeros, zeros % 2 ? 0 : 1);
  const n = as[0] % 10;
  if (as[0] === 0) return 0;
  else if (as[1] === 0) return 1;
  else if (as[2] === 0) return n;
  else if (as[3] === 0) return n ** (((as[1] - 1) % 4) + 1) % 10;
  else if (as[1] % 4 === 2 && as[2] > 1) return n ** 4 % 10;
  else if (as[1] % 4 === 3 && as[2] % 2 === 0) return n;
  else return n ** (((as[1] - 1) % 4) + 1) % 10;
}
