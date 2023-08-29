const reverseArray = require("./reverse-array")

describe('reverse array', () => {
    it('should reverse the array', () => {
        expect(reverseArray([1,2,3,4])).toEqual([4,3,2,1])
    })
})