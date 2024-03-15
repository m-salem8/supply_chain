from _01_extract_data import extract_main_data, extract_company_links
from _03_extract_reviews import extract_reviews
from _05_upload_blob import upload_blob
from _07_buffer_csv import write_to_csv_buffer
import time


if __name__=="__main__":

    company_data = extract_main_data()
    company_cols = ["id","company_name", "trust score", "No of reviews", "domain"]
    blob_name = "companies_data.csv"
    file = write_to_csv_buffer(company_data, company_cols)
    upload_blob(file, blob_name)


    review_cols = ["rate", "date_posted", "replied", "review_text"]
    company_links = extract_company_links()
    for i, link in enumerate(company_links[:4]):
        reviews_data = extract_reviews(link)
        file = write_to_csv_buffer(reviews_data, review_cols)
        blob_name = link.split('/')[2].split(".")[0] + '.csv'
        upload_blob(file, blob_name)
        if i < len(company_links[:4]) -1:
            time.sleep(300)



