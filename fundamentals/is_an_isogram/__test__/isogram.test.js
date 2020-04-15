const isAnIsogram = require('../src/isogram');

describe('isogram', () => {
  it('should return true if the word is an isogram', () => {
    expect.assertions(1);

    const word = 'ab';

    expect(isAnIsogram(word)).toBe(true);
  });
});
