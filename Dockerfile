FROM python

RUN mkdir /app && \
apt-get update && apt-get upgrade -y && \
apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 \
libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libnss3 lsb-release xdg-utils

#download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install && \
rm google-chrome-stable_current_amd64.deb && \
pip install --upgrade pip

WORKDIR /app 
#install python dependencies
COPY requirements.txt requirements.txt 
RUN pip install -r ./requirements.txt 


#RUN apt-get install chromium-chromedriver


#copy local files
COPY app . 

ENTRYPOINT python3 main.py
