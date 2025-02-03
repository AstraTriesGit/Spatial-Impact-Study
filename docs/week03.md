# Week 03
We have found a different site from where we can get the coordinate data for each station. 
The required class handling this functionality is `webscraping.fetch.CoordFetcher`. 
#### Simulated Workflow
- Open the [Geoviewer](https://indiawris.gov.in/wris/#/Geoviewer) website.
- Open the layer list.
- Check the box `Groundwater_Stations`.
- Check the box `Groundwater_Station` within the dropdown of `Groundwater_Stations` (this will most probably be 
done automatically, the work is to select the key to open the dropdown menu).
- Select the kebab menu.
- Select `View in Attribute Table`.
- (!) Looks like the table does not open up in a reliable manner.
- Extract the data in the table.
- ?
- Profit!

### Achievements
We have managed to click a button inside the embedded ArcGIS application
on the website!
- Selenium's webdriver handles _iframes_ differently. 
### Difficulties
It's not a simple website to scrape. Here are the steps you 
have to take to download just one dataset.

### Future Goals and Foreseen Issues