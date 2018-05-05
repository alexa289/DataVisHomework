#Import Dependencies
import pandas as pd
import time
from bs4 import BeautifulSoup as bs
import requests as req
from splinter import Browser
from selenium import webdriver


#Boiler plate code to init browser..define path
def init_browser():
    executable_path = {"executable_path": "chrome/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

#Define a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
def scrape():
    browser = init_browser()

    #Create an empty dict to append scraped data in step 1
    mars_data_dict = {}


    #Copy all the code from the jupyter notebook and append all data scraped into the dictionary
    #-------NASA MARS NEWS-------
    mars_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_url)

    html_browser = browser.html
    news_from_mars = bs(html_browser, 'html.parser')

    #Check the elements to know where to find the div element that contains title
    news_title = news_from_mars.find('div', class_='content_title').text

    #Check the elements to know where to find the div element that contains paragraph
    news_paragraph = news_from_mars.find('div', class_="rollover_description_inner").text

   # Add the title and paragraph to the data dictionary
    mars_data_dict['title'] = news_title
    mars_data_dict["paragraph"] = news_paragraph

    # -------JPL Mars Space Images - Featured Image-------
    # Point to JPL's Featured Space Images page.
    jpl_mars_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_mars_url)

    # Scrape the browser to navigate the site and find the image url for the current Featured Mars Image
    html_browser = browser.html
    jpl_mars = bs(html_browser, 'html.parser')

    #find the url of the img
    img_url = jpl_mars.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
    #get the base url from the href of the webpage (jpl_logo class)
    #base_jpl_href = jpl_mars.find_all('div', class_='jpl_logo')
    #use BS to create obkect, parse with lxml
    jpl_logo_soup = bs(html_browser, 'lxml')
    #loop through all the href of the url

    # Get all the hrefs of the url
    href_list = []
    for href in jpl_logo_soup.find_all('a'):
        href_list.append(href.get('href'))

    #retrieve the path for jpl.nasa
    jpl_nasa_path = href_list[1].strip('/')

    # Assign the url string to a variable called featured_image_url
    featured_image_url = "https://"+jpl_nasa_path+img_url

    # Add the featured image to the data dictionary
    mars_data_dict["featured_image_url"] = featured_image_url

    #-------Mars Weather-------
    # Point to Mars weather twitter page.
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    # Scrape the browser to navigate the site and get the latest Mars weather tweet from the page.
    html_browser = browser.html
    mars_twitter = bs(html_browser, 'html.parser')

    #inspect the weather tweet
    weather_tweet = mars_twitter.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    #Save the tweet text for the weather report as a variable called mars_weather.
    mars_weather = weather_tweet.text

    # Add mars weather to the data dictionary
    mars_data_dict["mars_weather"] = mars_weather


    #-------Mars Facts------
    # Point to Mars Facts webpage.
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

    # Scrape the browser to navigate the site and get the Mars facts
    html_browser = browser.html
    #mars_facts = bs(html_browser, 'html.parser')

    # Convert the url to a pandas df
    mars_facts_pd = pd.read_html(mars_facts_url)
    mars_facts_df = pd.DataFrame(mars_facts_pd[0])

    # Define column names
    mars_facts_df.columns = ['Parameters', 'Data']
    #Set the index
    mars_facts_df2 = mars_facts_df.set_index("Parameters")

    #Convert the dataframe to an html object and remove unnecesary \n
    mars_facts_html = mars_facts_df2.to_html(classes='mars-facts')
    mars_facts_html_table = mars_facts_html.replace('\n', '')

    # Add the mars facts to the data dictionary
    mars_data_dict["mars_facts"] = mars_facts_html_table


    #------Mars Hemispheres------
    # Point to USGS Astrology webpage.
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    # Scrape the browser to navigate the site and get high resolution images for each Mars hemisphere
    html_browser = browser.html
    mars_hemisphere = bs(html_browser, 'html.parser')

    #Get the element "div" with the imgs
    div_images = mars_hemisphere.find('div', class_='collapsible results')

    #Loop through the class="item" by clicking the h3 tag and getting the image title and its url.
    hemispheres_img_url_list = []

    for img in range(len(div_images.find_all("div", class_="item"))):
        time.sleep(2)
        img_header = browser.find_by_tag('h3')
        img_header[img].click()
        html_b = browser.html
        html_soup = bs(html_b, 'html.parser')
        h2_title = html_soup.find("h2", class_="title").text
        div = html_soup.find("div", class_="downloads")
        #for li in div:
        a = div.find('a')
        href_url = a.attrs['href']
        hemispheres = {
            'img_title': h2_title,
            'img_url': href_url
        }
        hemispheres_img_url_list.append(hemispheres)
        browser.back()
        
    # Add the hemispheres data to the  dictionary
    mars_data_dict["hemisphere_images"] = hemispheres_img_url_list
    print(mars_data_dict)
    # Return the dictionary
    return mars_data_dict
    
