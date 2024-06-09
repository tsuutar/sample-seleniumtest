FROM --platform=linux/amd64 python:3.9.16-bullseye

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en_US

# Google Chrome & ChromeDriver
RUN apt-get update -yqq \
    && apt-get install -yqq \
        wget \
        gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -yqq \
    && CHROME_LATEST_VERSION=$(curl -sS "omahaproxy.appspot.com/linux?channel=stable") \
    && apt-get install -yqq google-chrome-stable=$CHROME_LATEST_VERSION-1 \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* \
    && CHROME_LATEST_MAJOR_VERSION=$(echo $CHROME_LATEST_VERSION | cut -d . -f 1) \
    && CHROME_DRIVER_VERSION=$(curl -sS "chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_LATEST_MAJOR_VERSION}") \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Python
WORKDIR /usr/src
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r ./requirements.txt