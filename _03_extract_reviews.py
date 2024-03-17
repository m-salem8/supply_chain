import requests
from bs4 import BeautifulSoup
import csv 
from _01_extract_data import extract_main_data
from _01_extract_data import extract_company_links
from _02_convert_date import convert_to_date
from itertools import zip_longest
import pandas as pd


base_url = "https://www.trustpilot.com"

def extract_reviews(link):
    reviews_per_company = [] 
    dates_posted = []        
    review_rates = []        
    replied = []
    
    page_number = 1
    
    absolute_link = f"{base_url}{link}?page={page_number}"
    results = requests.get(absolute_link)
    src = results.content
    soup = BeautifulSoup(src, 'lxml')
    total_pages = int(soup.find_all("span", {"class":"typography_heading-xxs__QKBS8 typography_appearance-inherit__D7XqR typography_disableResponsiveSizing__OuNP7"})[-2].text)
    
    while True:
        absolute_link = f"{base_url}{link}?page={page_number}"
        results = requests.get(absolute_link)
        src = results.content
        soup = BeautifulSoup(src, 'lxml')
        reviews = soup.find_all("p", {"class":"typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn"})
        dates = soup.find_all("div", {"class": "typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_datesWrapper__RCEKH"})
        review_rate = soup.find_all("div", {"class", "star-rating_starRating__4rrcf star-rating_medium__iN6Ty"})
        review_block = soup.find_all("div", {"class":"styles_reviewCardInner__EwDq2"})

        for j in range(len(reviews)):
            reviews_per_company.append(reviews[j].text)
            dates_posted.append(convert_to_date(dates[j].text))
            review_rates.append(review_rate[j].find("img").get("alt").split()[1])
            has_replies = review_block[j].find("div", {"class": "paper_paper__1PY90 paper_outline__lwsUX paper_subtle__lwJpX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__ib2L5"}) is not None
            replied.append(has_replies)
            
        if page_number == total_pages:
            break
        else:
            page_number += 1
        print(f" Page switched to {page_number}")
    
    unpack_list = [review_rates, dates_posted, replied, reviews_per_company]
    reviews_data = zip_longest(*unpack_list)
    print(f"Reviews Extracted Successfully !")
    col_names = ["rate", "date_posted", "replied", "review_text"]
    df = pd.DataFrame(reviews_data, columns = col_names)
    return df


if __name__ == "__main__":
    link = "/review/usacea.org"
    reviews_data = extract_reviews(link)
    csv_file_path = "/mnt/c/Users/PC/Documents/supply_chain/usacae.csv"
    reviews_data.to_csv(csv_file_path, index=False, mode='w+')


"""if __name__ == "__main__":
    #link = "/review/electricityrates.com"
    link = extract_company_links()
    reviews_data = extract_reviews(link[0])
    csv_file_path = "/mnt/c/Users/PC/Documents/supply_chain/electricityRatecom.csv"
    with open(csv_file_path, "w", newline='') as file:
        wr = csv.writer(file)
        wr.writerow(["rate", "date_posted", "replied", "review_text"])
        wr.writerows(reviews_data)"""