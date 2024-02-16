#!/usr/bin/env python
# coding: utf-8

# In[25]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data_from_links(links):
    # Initialize a list to store scraped data
    scraped_data = []
    
    # Iterate over each link
    for link in links:
        # Send GET request to the link
        response = requests.get(link)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract text content from the page
            text_content = soup.get_text()
            
            # Append scraped data to the list
            scraped_data.append({"Link": link, "Content": text_content})
            print("Scraped data from:", link)
        else:
            print("Error: Unable to scrape data from", link)
    
    return scraped_data

def save_to_csv(data, filename):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    # Define the list of links
    links = [
        "https://en.wikipedia.org/wiki/Canoo",
        "https://www.linkedin.com/pulse/canoe-market-size-growth-trends-report-2024-2030-dj66f",
        "https://www.linkedin.com/pulse/canoe-market-size-2023-share-trends-opportunities",
        "https://www.canoo.com/about/",
        "https://investors.canoo.com/news-presentations/press-releases/detail/5/electric-vehicle-company-canoo-to-list-on-nasdaq-through",
        "https://www.databridgemarketresearch.com/reports/global-canoe-and-kayak-market",
        "https://investors.canoo.com/sec-filings/all-sec-filings/content/0001628280-22-004514/goev-20211231.htm",
        "https://investors.canoo.com/sec-filings/all-sec-filings/content/0001213900-21-004077/f424b30121_canooinc.htm",
        "https://www.statista.com/topics/1721/us-automotive-industry/",
        "https://support.google.com/websearch?p=ws_settings_location&hl=en-IN&opi=89978449",
        "https://dcf.fm/blogs/blog/goev-porters-five-forces-analysis",
        "https://www.lizmotors.com/internship-coding-assignment2024/",
        "https://dcf.fm/blogs/blog/goev-bcg-matrix",
        "https://investors.canoo.com/sec-filings/all-sec-filings/content/0001628280-23-009932/goev-20221231.htm",
        "https://fortune.com/2022/08/27/canoo-electric-vehicles-walmart-struggles-tony-aquila/",
        "https://store.marketline.com/report/canoo-inc-swot-analysis/",
        "https://investors.canoo.com/sec-filings/all-sec-filings/content/0001628280-22-004514/goev-20211231.htm",
        "https://support.google.com/websearch?p=ws_settings_location&hl=en-IN&opi=89978449",
        "https://www.linkedin.com/pulse/evolution-consumer-behavior-marketing-trends-stay-ahead",
        "https://www.thekeenfolks.com/blog-article/the-impact-of-technology-on-consumer-behaviour",
        "https://www.market-xcel.com/blogs/navigating-the-shifting-tides-consumer-behaviour-trends",
        "https://aicontentfy.com/en/blog/power-of-online-sales-research-in-identifying-market-trends",
        "https://blog.hubspot.com/marketing/marketing-trends",
        "https://support.google.com/websearch?p=ws_settings_location&hl=en-IN&opi=89978449",
        "https://investors.canoo.com/financial-information/income-statement",
        "https://www.lizmotors.com/internship-coding-assignment2024/",
        "https://investors.canoo.com/sec-filings/all-sec-filings/content/0001628280-23-009932/0001628280-23-009932.pdf",
        "https://www.prnewswire.com/news-releases/canoo-inc-announces-first-quarter-2023-results-301825198.html",
        "https://www.globaldata.com/company-profile/canoo-inc/financials/",
        "https://support.google.com/websearch?p=ws_settings_location&hl=en-IN&opi=89978449"
    ]
    
    # Scrape data from the links
    data = scrape_data_from_links(links)
    
    # Save all scraped data to a CSV file
    save_to_csv(data, "scraped_data_with_content.csv")

if __name__ == "__main__":
    main()

