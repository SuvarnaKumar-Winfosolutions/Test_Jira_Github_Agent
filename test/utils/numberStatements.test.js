import { getPositiveStatementFor15 } from '../../src/utils';

describe('numberStatements', () => {
  it('should return the correct positive statement for 15', () => {
    const result = getPositiveStatementFor15();
    expect(result).toBe('15 is a positive number');
  });
});
