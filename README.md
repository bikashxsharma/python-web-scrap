## Web Scrap v1
- This is a desktop app built with python. It automates the process of getting data from the [Published Entries Search](https://virre.prh.fi/novus/publishedEntriesSearch?execution=e2s1) website.
- You can read more about open data from [PRH's website](https://avoindata.prh.fi/index_en.html)
- This project is for personal practice and not intended to violate any regulation. 
<img src="/screenshots/open_data.png" height="250px" />

## How it works?
- User needs to enter the from and to date and select the city. 
- The application will then open the chromium.
- Goes to the [link](https://virre.prh.fi/novus/publishedEntriesSearch?execution=e2s1)
- Automatically enters the date, selects the city and application type. 
- Automatically goes one by one to the company's info. 
- If there is an email address it automatically grabs the company name and email address. 
- All the information will be stored in a .csv file.

## Tech stack
- Python
- Selenium
- Tkinter


## Screenshots

##### Home Screen
<img src="/screenshots/home.png" height="400px" />

##### Search Page
<img src="/screenshots/search_page.png" height="400px" />

##### Results table
<img src="/screenshots/result_table.png" height="400px" />

##### Company info
<img src="/screenshots/result_page.png" height="400px" />

### CSV file

<img src="/screenshots/result_page.png" height="400px" />
