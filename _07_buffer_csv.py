import csv
import io 

def write_to_csv_buffer(data, col_names):
    csv_buffer = io.StringIO()  # Use io.BytesIO() for binary data
    wr = csv.writer(csv_buffer)
    wr.writerow(col_names)
    wr.writerows(data)
    csv_buffer.seek(0)  # Reset buffer position to beginning
    return csv_buffer  



if __name__=="__main__":

    # Sample data and column names
    data = [
        ['1', 'John', 'Doe'],
        ['2', 'Jane', 'Smith'],
        ['3', 'Alice', 'Johnson']
    ]
    col_names = ['ID', 'First Name', 'Last Name']

    # Test the function
    csv_buffer = write_to_csv_buffer(data, col_names)

    # Read and print the contents of the CSV buffer
    csv_data = csv_buffer.getvalue()
    print(csv_data)




"""
def write_to_csv_buffer(data):
    csv_buffer = io.StringIO()  # Use io.BytesIO() for binary data
    writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    csv_buffer.seek(0)  # Reset buffer position to beginning
    return csv_buffer
"""