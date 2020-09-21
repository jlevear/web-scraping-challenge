# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd

def scrape():
    # URL of page to be scraped
    url1 = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url1)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Navigate through the page to find the latest news title and paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='rollover_description_inner').text

    # Activate the chromedriver
    executable_path = {'executable_path': 'chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Open the url in chrome
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    # Activate BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Locate the featured image url
    find_featured_image_url = soup.find('footer').find('a').get('data-fancybox-href')
    featured_image_url = f'https://www.jpl.nasa.gov{find_featured_image_url}'
    featured_image_url

    # Close the browser
    browser.quit()

    # Use pandas to read the tables in the url
    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)

    # Find the relevant table 
    first_table = tables[0]

    # Convert the table to html
    table_html = first_table.to_html(index=False, header=False)
    table_html

    # Activate the chromedriver
    executable_path = {'executable_path': 'chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Open the url in chrome
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)

    # Activate BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Locate the div containing the Mars hemisphere urls
    items = soup.find_all('div', class_='item')

    # Create a list of the hemisphere urls using a for loop 
    url_list = []

    for item in items:
        url = item.find('a').get('href')
        url_list.append(url)

    # Format the urls correctly
    hemisphere_url_list = ['https://astrogeology.usgs.gov' + url for url in url_list]

    # Close the browser
    browser.quit()

    # Activate the chromedriver
    executable_path = {'executable_path': 'chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Create a list of dictionaries for the hemisphere titles and image urls using a for loop 
    hemisphere_image_urls = []

    for url in hemisphere_url_list:
   
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        hemisphere_title = soup.find('div', class_='content').find('h2').text
        hemisphere_image = soup.find('div', class_='downloads').find('ul').find('li').find('a').get('href')
    
        hemisphere_image_urls.append({"title": hemisphere_title, "image": hemisphere_image})

    # Close the browser
    browser.quit()

    # Create a dictionary of the items that were scraped
    mars_dictionary = {
        "title": news_title,
        "paragraph": news_p,
        "image": featured_image_url,
        "table": table_html,
        "hemispheres": hemisphere_image_urls
    }
       
    return mars_dictionary