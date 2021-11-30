#!/bin/bash

apt update -y
apt install unzip xvfb libxi6 libgconf-2-4 default-jdk python3-pip python3-virtualenv -y
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt update -y
sudo apt install google-chrome-stable -y
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
git clone https://1b6227dec34006f493aa2286a178a0b722f232dd:x-oauth-basic@github.com/adminprivileges/ytbot.git
python3 -m virtualenv ytbot
source ./ytbot/bin/activate
cd ./ytbot
chmod +x chromedriver
pip3 install -r requirements.txt
python3 ./twitchbot.py
