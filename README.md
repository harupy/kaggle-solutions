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

# Add the repository root to `PYTHONPATH`.
source dev/setup.sh
```

## How to fetch data

### Competition data

```bash
# Usage
python tools/fetch_one_competition -s <competition_slug>

# Example
python tools/fetch_one_competition -s titanic
```

### Solution data

To fetch solution data, ChromeDriver is required. If you don't have one, download [here](https://chromedriver.chromium.org/downloads) and put it in the repository root.

```bash
# Usage
python tools/fetch_discussion.py -u <discussion_url> -t <title>

# Example
python tools/fetch_discussion \
  -u https://www.kaggle.com/c/titanic/discussion/1234  # discussion url
  -t "1st place solution"  # title to display on the UI.
```

## How to run the UI

```bash
cd client

# Install dependencies.
npm install

# Run the UI.
npm start

# Open localhost:3000 on your browser.
```

## Test

### Tools

```bash
# Lint
./dev/lint.sh

# Test
./dev/test.sh
```

### UI

```bash
# Lint
npm run lint

# Test
npm run test
```

## License

MIT
