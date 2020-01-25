import * as utils from '../utils';

describe('utils', () => {
  it('formatDate', () => {
    const result: string = utils.formatDate('2000-01-01T16:52:33.97Z');
    expect(result).toBe('2000-01-01');
  });

  it('formatDate', () => {
    expect(utils.isDateKey('enabledDate')).toBe(true);
    expect(utils.isDateKey('deadline')).toBe(true);
    expect(utils.isDateKey('title')).toBe(false);
  });

  it('basename', () => {
    expect(utils.basename('dir/test.js')).toBe('test.js');
    expect(utils.basename('dir\\test.js')).toBe('test.js');
    expect(utils.basename('test.js')).toBe('test.js');
  });
});
