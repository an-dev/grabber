#Looksdigest (LookBook Grabber 2.0)

A simple web app featuring top and new looks from lookbook.nu

*Clone the repo 
*Create a proper virtualenv,

```
$ virtualenv venv
$ source venv/bin/activate
```

*Install dependencies
`$ pip install -r requirements.txt`

*Create a .secret/base.json file containing basic db config
```
{
  "DJANGO_DB_ENGINE":"django.db.backends.xxx",
  "DJANGO_DB_NAME":"xxx.xxx",
  "DJANGO_DB_USER":"",
  "DJANGO_DB_PASSWORD":"",
  "DJANGO_DB_HOST":"",
  "DJANGO_DB_PORT":""
}
```

*To use fabfile shortcuts modify `DEFAULT_ENV` var

*Run migrations
`$ python manage.py migrate`

*Create superuser for admin consulting
`$ python manage.py createsuperuser`

*Create a script to be executed by cron calling the scraper
```
#~/.cron/lookscraper
#!/bin/bash

WD="/home/Documents/"
SPIDER_PATH="looksdigest/lookscraper/lookscraper/spiders/"
VENV_ACTIVATE="venv/bin/activate"


cd $WD
source ./$VENV_ACTIVATE
cd ./$SPIDER_PATH
scrapy crawl lookspider --logfile "/var/log/lookspider.log"
```

*And give it proper permissions
`$ chmod +x ~/.cron/lookscraper.sh`

*and then edit the crontab
`*/5 * * * * ~/.cron/scraper.sh #runs the command every 5 minutes`

*Run the development server 
`$ python manage.py runserver`

====
ToDo

*build a django app to handle apis
*build a decent frontend to display the looks and comments
*more stuff I guess

