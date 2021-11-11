function permutations(string) {
  return recPermutations(
    Array.from(string).reduce((s, c) => {
      s[c] ? s[c]++ : (s[c] = 1);
      return s;
    }, {})
  );
}

function recPermutations(letterCounter) {
  let permutations = [];
  for (const letter in letterCounter) {
    const nextCounter = {
      ...letterCounter,
      [letter]: letterCounter[letter] - 1,
    };
    if (!nextCounter[letter]) delete nextCounter[letter];
    const asdf = recPermutations(nextCounter);
    permutations = permutations.concat(asdf.map((p) => letter + p));
  }
  return permutations.length > 0 ? permutations : [""];
}
