export FLASK_APP=manage
export FLASK_ENV=production
export DATABASE_URL='postgres://amazinguser:amazingPassword@localhost/rwid_scraper_source'
export DATABASE_TEST_URL='postgres://amazinguser:amazingPassword@localhost/rwid_scraper_source_test'
export APP_SETTINGS='project.config.ProductionConfig'