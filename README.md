# Kaggle Solutions

https://harupy.github.io/kaggle-solutions/

## Setup

```bash
# This step is optional.
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
npm install
npm start
```

## License

MIT
