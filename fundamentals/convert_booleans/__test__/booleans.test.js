const isYesOrNey = require('../src/boolean');

describe('boolean', () => {
  it('should return yes if the boolean is true', () => {
    expect.assertions(1);

    const bool = true;

    expect(isYesOrNey(bool)).toBe('Yes');
  });

  it('should return no if the boolean is false', () => {
    expect.assertions(1);

    const bool = false;

    expect(isYesOrNey(bool)).toBe('No');
  });
});
