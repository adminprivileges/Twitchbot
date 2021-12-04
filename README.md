# Twitchbot
A bot that i made to get twitch drops, for it to work youre gonna need to do a few things 
1. Create a twitchbot_vars.py and set your twitch_username and twitch_password to string variables. I plan on automating this and a few other things in an init script soon. 
2. register [a gmail application](https://developers.google.com/gmail/api/quickstart/python/) 
3. Also make sure to go the following to initialize your ezgmail instance, if you choose desktop application when you register your app, do this step on your desktop machine and move the initialization token to your server's folder along with your credentials.json file
```
import ezgmail, os
os.chdir(r'C:\path\to\credentials_json_file')
ezgmail.init()
```