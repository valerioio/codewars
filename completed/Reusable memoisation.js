function memo(fn) {
  const cache = {};
  return function (n) {
    const m = typeof n === "object" ? JSON.stringify(n) : n;
    return cache.hasOwnProperty(m) ? cache[m] : (cache[m] = fn(n));
  };
}
