FROM python:3.7.6

RUN apt-get update && apt-get install -y wget unzip

# Install Chrome.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    cat /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install Chrome Driver.
RUN CHROME_DRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip

# Install Python dependencies.
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements.txt -r requirements-dev.txt

# Add "tools" to "PYTHONPATH" to allow importing modules.
ENV PYTHONPATH $PYTHONPATH:$(pwd)/tools
