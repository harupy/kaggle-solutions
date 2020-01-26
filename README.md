# Kaggle Solutions

https://harupy.github.io/kaggle-solutions/

## Setup

```bash
# Install pipenv (optional).
pip install pipenv

# Install dependencies.
pipenv install

# Activate the environment.
pipenv shell
```

## How to fetch data

```bash
# Competition data
python tools/fetch_one_competition -s <competition_slug>

# Solution data
python tools/fetch_discussion.py -u <discussion_url> -t <title>
```

## How to run the UI

```bash
cd client

# Install dependencies.
npm install

# Run the UI.
npm start
```

## Test

Tools

```bash
# Lint
./dev/lint.sh

# Test
./dev/test.sh

```

UI

```bash
# Lint
npm run lint

# Test
npm run test
```

## License

MIT
