function add(n) {
  let myNum = n;
  function myAdd(m) {
    myNum += m;
    return myAdd;
  }
  myAdd.toString = function () {
    return myNum;
  };
  return myAdd;
}
