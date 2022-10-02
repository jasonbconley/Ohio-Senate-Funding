# Ohio-Senate-Funding
This repository visualizes the campaign funding for the Ohio Senate race between Tim Ryan and J.D. Vance. 

# Documentation of the project, end-to-end
- Need to scrape data from FEC and possibly opensecrets.
  - Need to establish *where* the money is coming from
  - Assign zipcode / county to contribution, *out-of-state* for others
    - Might be easy to extend and break down the *out-of-state* category

- Once GEOJson file is created, pipe into Svelte frontend and javascript backend?
  - Nodejs for backend
  - Need to learn svelte for frontend presentation
  - The notebooks will ETL the data, but what JS packages will show the visualizations?
  - Github pages?

- Create meaningful context, this might be difficult, need to learn some about journalistic writing / ethics.

# The journey

I started out trying to code the scraper following the "iris site" tutorial. I wanted to define a pipeline for the CSV files to be gathered from the FEC, and then updated if there is new data available. That way, once the dashboard is created and the github actions were set up, it would be dynamic as the candidates submitted new info.

I know of one way *in python* to collect data / html from a website using code. Beautiful soup! Beautiful soup allows one to essentially download a website's html source code into a variable, and then had some packages that allows the code to traverse this tree and access the data you're looking for. This was exactly what I needed, so I dove right in to downloading the html source code and began poking around the site @ feclink

I knew I was searching for a the first dropdown box in the table on the screen in front of me. Then, I would need to access the element within this list, grab the CSV link, and download the data and begin visualizing! The problem was, I couldn't seem to find the dropdown box I was looking for. I printed the variable using prettyify() and manually searched through the html code to find this dropdown list. After checking a few times, and after changing my soup from page.text to page.content and back again a few times with no dropdown box, I knew I had to be doing something wrong. I revisited the site look again at what I was trying to do.
I inspected the source code of the site through the browser, and in this code I saw the dropdown box! Sweet! However, I could not understand why these elements were not appearing in my soup. After some question googling, I decided to search for something along the lines of "beautiful soup not loading javascript," and I was given my answer. 
The page I was soupifying was a static html page, the code I was writing was not able to *compile* any of the javascript present on the page. So, as stackoverflow suggested, I needed to use a browser in order to be able to execute the javascript and see my desired dropdown menu.
This was new to me, but I had to use Selenium and an accompanied webdriver to allow my code to create a browser, and execute javascript. 
