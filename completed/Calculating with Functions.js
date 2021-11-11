function num(n, f) {
  return f === undefined ? n : f(n);
}

function op(o, n) {
  return (m) => ~~o(m, n);
}

function zero(o) {
  return num(0, o);
}
function one(o) {
  return num(1, o);
}
function two(o) {
  return num(2, o);
}
function three(o) {
  return num(3, o);
}
function four(o) {
  return num(4, o);
}
function five(o) {
  return num(5, o);
}
function six(o) {
  return num(6, o);
}
function seven(o) {
  return num(7, o);
}
function eight(o) {
  return num(8, o);
}
function nine(o) {
  return num(9, o);
}

function plus(n) {
  return op((a, b) => a + b, n);
}
function minus(n) {
  return op((a, b) => a - b, n);
}
function times(n) {
  return op((a, b) => a * b, n);
}
function dividedBy(n) {
  return op((a, b) => a / b, n);
}
