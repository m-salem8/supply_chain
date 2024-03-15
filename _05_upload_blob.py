from azure.storage.blob import BlobServiceClient
from _06_config_reader import read_storage_config


def upload_blob(csv_buffer, blob_name):
    storage_connection_string, container_name = read_storage_config('config.json')

    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
        
        # Get a client to interact with the container
        container_client = blob_service_client.get_container_client(container_name)
        
        # Upload the file to blob
        container_client.upload_blob(name=blob_name, data=csv_buffer.getvalue(), overwrite=True)

        """# Upload the file to blob
        with open(file, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite = True)"""
            
        print(f"File '{csv_buffer}' uploaded as '{blob_name}' to container '{container_name}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")



        

if __name__=="__main__":

    # Provide the local path of the file you want to upload
    source_file_path = "/mnt/c/Users/PC/Documents/supply_chain/electricityRatecom.csv"

    # Provide the name you want to give to the blob
    blob_name = "electricityRatecom.csv"

    # Call the function to upload the file to Azure Blob Storage
    upload_blob(source_file_path, blob_name)