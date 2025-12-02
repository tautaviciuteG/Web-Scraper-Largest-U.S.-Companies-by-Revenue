📘 **Web-Scraper-Largest-U.S.-Companies-by-Revenue**

This project is a lightweight Python scraper that automatically collects the latest list of the largest U.S. companies by revenue from Wikipedia.
With BeautifulSoup, Requests, and Pandas, the script fetches the data, parses the HTML table, and exports a clean CSV ready for analysis.

<br/>
<br/>

✨ Features

🔍 Scrapes the Wikipedia table of top U.S. companies by revenue

🧠 Automatically detects headers and row structure

🧹 Cleans extracted text

🗂️ Converts raw HTML into a structured Pandas DataFrame

💾 Saves results as a CSV file

⚡ Simple, readable, fully customizable

<br/>

**⚡ Powered By**
* Python 3
* BeautifulSoup (bs4)
* Requests
* Pandas
  
<br/>

📁 **Project Workflow**

1. Request page data from Wikipedia

2. Parse HTML with BeautifulSoup

3. Locate the main company table

4. Extract column headers

5. Loop through rows and extract cell data

6. Store everything in a Pandas DataFrame

7. Export the DataFrame as Companies.csv
