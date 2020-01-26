module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:prettier/recommended',
    // 'prettier/@typescript-eslint'
  ],
  plugins: ['@typescript-eslint'],
  env: { node: true, es6: true },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
    project: './tsconfig.json',
  },
  ignorePatterns: ['src/serviceWorker.ts', 'node_modules/'],
  rules: {
    'no-console': 2,
  },
};
