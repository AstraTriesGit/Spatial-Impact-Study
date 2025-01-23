# Week 01
### Achievements
We have managed to click a button inside the embedded ArcGIS application
on the website!
- Selenium's webdriver handles _iframes_ differently. 
### Difficulties
It's not a simple website to scrape. Here are the steps you 
have to take to download just one dataset.

### Future Goals and Foreseen Issues
- Actually achieve **full process automation** with Selenium.
- (!) The `xlsx` files downloaded have headers about WRIS, which will have
to be removed before the files can be compiled to one database. (but even 
before that, just to be able to be read as a `csv`.)
- (!) The stations do not come with latitude and longitude data,
although if one were to use the application, the required coordinate data
is shown along with the station info. Can it be added in some way? 
