CREATE DATABASE rwid_scraper_source;
CREATE DATABASE rwid_scraper_source_test;

--CREATE USER amazinguser WITH password 'amazingPassword';
GRANT ALL PRIVILEGES ON database rwid_scraper_source to amazinguser;
ALTER USER amazinguser SUPERUSER;
