#!/usr/bin/env python
# coding: utf-8

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

    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='rollover_description_inner').text

    # print(news_title)
    # print(news_p)

    executable_path = {'executable_path': 'chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    find_featured_image_url = soup.find('footer').find('a').get('data-fancybox-href')
    featured_image_url = f'https://www.jpl.nasa.gov{find_featured_image_url}'
    featured_image_url

    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)
    first_table = tables[0]
    table_html = first_table.to_html()
    table_html

    executable_path = {'executable_path': 'chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('div', class_='item')

    url_list = []

    for item in items:
        url = item.find('a').get('href')
        url_list.append(url)

    hemisphere_url_list = ['https://astrogeology.usgs.gov' + url for url in url_list]

    hemisphere_url_list

    hemisphere1_url = hemisphere_url_list[0]
    browser.visit(hemisphere1_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere1_image = soup.find('div', class_='downloads').find('ul').find('li').find('a').get('href')
    # print(hemisphere1_image)
    hemisphere1_title = soup.find('div', class_='content').find('h2').text
    # print(hemisphere1_title)

    hemisphere2_url = hemisphere_url_list[1]
    browser.visit(hemisphere2_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere2_image = soup.find('div', class_='downloads').find('ul').find('li').find('a').get('href')
    # print(hemisphere2_image)
    hemisphere2_title = soup.find('div', class_='content').find('h2').text
    # print(hemisphere2_title)

    hemisphere3_url = hemisphere_url_list[2]
    browser.visit(hemisphere3_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere3_image = soup.find('div', class_='downloads').find('ul').find('li').find('a').get('href')
    # print(hemisphere3_image)
    hemisphere3_title = soup.find('div', class_='content').find('h2').text
    # print(hemisphere3_title)

    hemisphere4_url = hemisphere_url_list[3]
    browser.visit(hemisphere4_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere4_image = soup.find('div', class_='downloads').find('ul').find('li').find('a').get('href')
    # print(hemisphere4_image)
    hemisphere4_title = soup.find('div', class_='content').find('h2').text
    # print(hemisphere4_title)

    

    hemisphere_image_urls = [
        {"title": hemisphere1_title, "img_url": hemisphere1_image},
        {"title": hemisphere2_title, "img_url": hemisphere2_image},
        {"title": hemisphere3_title, "img_url": hemisphere3_image},
        {"title": hemisphere4_title, "img_url": hemisphere4_image}
    ]

    mars_dictionary = {
        "title": news_title,
        "paragraph": news_p,
        "image": featured_image_url,
        "table": table_html,
        "hemispheres": hemisphere_image_urls
    }
   
    browser.quit()
    
    return mars_dictionary

# print(scrape())