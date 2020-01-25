import * as utils from './utils';

describe('utils', (): void => {
  test('formatDate', (): void => {
    const result: string = utils.formatDate('2000-01-01T16:52:33.97Z');
    expect(result).toBe('2000-01-01');
  });

  test('formatDate', (): void => {
    expect(utils.isDateKey('enabledDate')).toBe(true);
    expect(utils.isDateKey('deadline')).toBe(true);
    expect(utils.isDateKey('title')).toBe(false);
  });

  test('basename', (): void => {
    expect(utils.basename('dir/test.js')).toBe('test.js');
    expect(utils.basename('dir\\test.js')).toBe('test.js');
    expect(utils.basename('test.js')).toBe('test.js');
  });
});
