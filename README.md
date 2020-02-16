# Kaggle Solutions

![Deploy](https://github.com/harupy/kaggle-solutions/workflows/Deploy/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

https://harupy.github.io/kaggle-solutions/

![kaggle-solutions-demo](https://user-images.githubusercontent.com/17039389/73281626-9b085000-4233-11ea-8025-01213b91c3d1.gif)

## Setup

```bash
# Anaconda
./dev/create-dev-env.sh

# Docker
docker-compose build
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
python tools/fetch_discussion.py \
  -u https://www.kaggle.com/c/titanic/discussion/1234  # Discussion url
  -t "1st place solution"  # Title to display on the UI.
```

## How to run the UI

```bash
cd client
npm install
npm start

# Open localhost:3000 on your browser.
```

## Test

### Tools

```bash
# Lint
./dev/lint.sh

# Tests
./dev/test.sh
```

### UI

```bash
# Lint
npm run lint

# Tests
npm run test
```

## License

MIT
