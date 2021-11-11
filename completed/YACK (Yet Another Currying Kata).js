function yack(fn, ...args) {
  function curriedFn(...args) {
    return fn(...args) || ((...args2) => curriedFn(...args, ...args2));
  }
  return curriedFn(...args);
}
