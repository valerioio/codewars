function peelTheOnion(s, d) {
  let result = [];
  let sumInnerLayers = 0;
  for (let i = ((s - 1) % 2) + 1; i <= s; i += 2) {
    let layer = i ** d - sumInnerLayers;
    sumInnerLayers += layer;
    result.push(layer);
  }
  return result.reverse();
}
