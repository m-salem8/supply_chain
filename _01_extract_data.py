# 1 Import and install the required libraries

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest

def extract_company_links():
    """
    Extracts links to company profiles from the Trustpilot website.
    
    Returns:
        list: A list of company profile links.
    """
    page_number = 1
    company_links = []

    while True:
        main_data = requests.get(f"https://www.trustpilot.com/categories/energy_supplier?page={page_number}")
        src = main_data.content
        soup = BeautifulSoup(src, "lxml")
        number_of_results = soup.find("p", {"class":"typography_body-m__xgxZ_ typography_appearance-default__AAY17"})
        total_results = int(number_of_results.text.strip().split()[-2])
        results_per_page = int(number_of_results.text.strip().split()[-4].split("-")[1])
        max_pages = total_results // results_per_page

        links = soup.find_all("div", {"class":"paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2"})

        for link in links:
            company_links.append(link.find("a").attrs["href"])

        if page_number > max_pages:
            print("Company Links Extracted Successfully !")
            break
        
        page_number += 1

    return company_links

def extract_main_data():
    """
    Extracts main data (company name, trust score, number of reviews, domain)
    from the Trustpilot website related to energy suppliers.
    
    Returns:
        zip: A zip object containing main data columns (ID, company name, trust score,
             number of reviews, domain).
    """
    page_number = 1
    company_name = []
    trust_score = []
    no_reviews = []
    domains = []

    while True:
        main_data = requests.get(f"https://www.trustpilot.com/categories/energy_supplier?page={page_number}")
        src = main_data.content
        soup = BeautifulSoup(src, "lxml")
        number_of_results = soup.find("p", {"class":"typography_body-m__xgxZ_ typography_appearance-default__AAY17"})
        total_results = int(number_of_results.text.strip().split()[-2])
        results_per_page = int(number_of_results.text.strip().split()[-4].split("-")[1])
        max_pages = total_results // results_per_page

        names = soup.find_all("p", {"class":"typography_heading-xs__jSwUz typography_appearance-default__AAY17 styles_displayName__GOhL2"})
        trust_scores = soup.find_all("span", {"class": "typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_trustScore__8emxJ"})
        number_of_reviews = soup.find_all("p", {"class":"typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7"})
        domain = soup.find_all("div", {"class":"styles_wrapper___E6__ styles_categoriesLabels__FiWQ4 styles_desktop__U5iWw"})

        for i in range(len(names)):
            company_name.append((names[i].text).replace("/", "_").replace(" ","").replace(".com","").lower())
            if len(trust_score) <= len(trust_scores):
                trust_score.append(trust_scores[i].text.split(" ")[1])
            else:
                trust_score.append(None)
            if len(no_reviews) <= len(number_of_reviews):
                no_reviews.append(number_of_reviews[i].text.split("|")[1].split(" ")[0])
            else:
                no_reviews.append(None)
            domains.append(domain[i].text)

        if page_number > max_pages:
            print("Main Data Extracted Successfully !")
            break
        
        page_number += 1

    ids = range(1, len(names)+1)
    unpack_list = [ids, company_name, trust_score, no_reviews, domains]
    company_data = zip_longest(*unpack_list)

    return company_data



if __name__=="__main__":

    company_links = extract_company_links()
    print(company_links)


    data = extract_main_data()

    with open("/mnt/c/Users/PC/Documents/supply_chain/companies_data.csv", "w") as file:
        wr = csv.writer(file)
        wr.writerow(["id","company_name", "trust score", "No of reviews", "domain"])
        wr.writerows(data)
