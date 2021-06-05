heroku config:set FLASK_ENV=production
heroku config:set DATABASE_URL=''
heroku config:set APP_SETTINGS='project.config.ProductionConfig'