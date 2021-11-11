function solution(numbers) {
  const gcd = (a, b) => (b ? gcd(b, a % b) : a);
  return numbers.length * numbers.reduce(gcd);
}
