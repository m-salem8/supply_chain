from elasticsearch import Elasticsearch, helpers
import csv
import warnings

warnings.filterwarnings("ignore")

# 1. Connection to the cluster 
es = Elasticsearch(hosts="http://localhost:9200")

# 2. Define index setting and mapping 
index_name = "supply_chain"
index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "company_id": {"type": "integer"},
            "company_name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "replied": {"type": "boolean"},
            "review_date": {
                "type": "date",
                "format": "dd-MM-yyyy"
            },
            "review_rate": {"type": "double"},
            "review_text": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
        }
    }
}


# 3. Create the index with settings and mappings

def create_index(index_name):
    csv.field_size_limit(100000000)
    try:
        es.indices.create(index=index_name, body=index_settings)
        print("Index created successfully.")
    except Exception as e:
        if "resource_already_exists_exception" in str(e):
            print("Index already exists.")
        else:
            print(f"An error occurred: {e}")

#4. Bulk indexing with error handling

file_name = "electricityrates"

def upload_doc(file_name):
    try:
        with open(f"/mnt/c/Users/PC/Documents/supply_chain/{file_name}.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            success, failed = helpers.bulk(es, reader, index=index_name, raise_on_error=False)
            print(f"Indexed {success} documents successfully.")
            if failed:
                print(f"{len(failed)} document(s) failed to index:")
                for item in failed:
                    print(f"Failed to index document: {item['index']['_id']}")
    except Exception as e:
        print(f"An error occurred during bulk indexing: {e}")

if __name__ == "__main__":

    companies = ["ambitenergyconsultants_vipconciergeteam", "electricityrates","igsenergy","integrityenergy", "igsenergy"]

    #create_index(index_name)
    for company in companies:
        upload_doc(company)
