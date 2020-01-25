/**
 * Extract yyyy-mm-dd.
 * @param  {string} dateString date string to format.
 * @return {string} Formatted date string.
 */
export const formatDate = (dateString: string): string => dateString.slice(0, 10);

/**
 * Return true if the given key is 'deadline' or 'enabledDate'.
 * @param  {string} key key to check.
 * @return {boolean}
 */
export const isDateKey = (key: string): boolean => ['deadline', 'enabledDate'].includes(key);

/**
 * Return the base name of the given path or url.
 * @param  {string} s File path or URL.
 * @return {string} Base name.
 */
export const basename = (s: string): string | undefined => s.split(/[\\/]/).pop();

/**
 * Check if the given date time is over.
 * @param {string} dateString Date string to check.
 * @return {boolean} True if the given date time is over.
 */

export const isDateOver = (dateString: string): boolean => Date.now() >= Date.parse(dateString);
