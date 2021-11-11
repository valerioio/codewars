function solution(list) {
  let startRange = 0;
  let listRanges = [];
  for (let i = 0; i < list.length + 1; i++) {
    if (list[i] + startRange !== list[startRange] + i) {
      if (i - startRange > 2) {
        listRanges.push(`${list[startRange]}-${list[i - 1]}`);
      } else {
        if (i - startRange > 1) {
          listRanges.push(`${list[i - 2]}`);
        }
        listRanges.push(`${list[i - 1]}`);
      }
      startRange = i;
    }
  }
  return listRanges.join();
}
