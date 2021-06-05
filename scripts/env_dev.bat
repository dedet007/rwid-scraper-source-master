@echo off
set FLASK_APP=manage
set FLASK_ENV=development
set DATABASE_URL=postgres://amazinguser:amazingPassword@localhost/rwid_scraper_source
set DATABASE_TEST_URL=postgres://amazinguser:amazingPassword@localhost/rwid_scraper_source_test
set APP_SETTINGS=project.config.DevelopmentConfig