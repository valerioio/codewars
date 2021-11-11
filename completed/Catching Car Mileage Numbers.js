function isInteresting(number, awesomePhrases) {
  const isADigitAndAll0s = (n) => parseInt(n.toString().slice(1)) === 0;
  const hasSameDigit = (n) => new Set(n.toString()).size === 1;
  const isSequence = (n, increment) =>
    Array.from(n.toString()).every(
      (d, i, n) =>
        i === n.length - 1 ||
        (parseInt(d) === (parseInt(n[i + 1]) + increment + 10) % 10 &&
          d !== "0")
    );
  const isIncrementing = (n) => isSequence(n, 1);
  const isDecrementing = (n) => isSequence(n, -1);
  const isPalindrome = (n) => {
    const sNumber = n.toString();
    const lastIndex = sNumber.length - 1;
    for (let i = 0; i < lastIndex / 2; i++)
      if (sNumber[i] !== sNumber[lastIndex - i]) return false;
    return true;
  };
  const isAwesome = (n) => awesomePhrases.includes(n);
  const criterion = [
    isADigitAndAll0s,
    hasSameDigit,
    isIncrementing,
    isDecrementing,
    isPalindrome,
    isAwesome,
  ];
  for (const n of [0, 1, 2])
    for (const criteria of criterion)
      if (number + n >= 100 && criteria(number + n)) return n ? 1 : 2;
  return 0;
}
