const isIsogram = (word) => new Set(word.toLowerCase()).size === word.length;

module.exports = function isAnIsogram(word) {
  const getValue = isIsogram(word);

  return getValue;
};
