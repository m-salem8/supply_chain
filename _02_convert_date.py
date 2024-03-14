from datetime import datetime, timedelta

def parse_date_string(date_str):
    # Define a list of expected date formats
    date_formats = ["%b %d, %Y", "%b %d %Y", "%d, %Y", "%d %Y"]
    
    # Iterate over each format and try to parse the date string
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.strftime("%d-%m-%Y")
        except ValueError:
            print("unparsed string !!", date_str)
            pass  # If parsing fails for this format, try the next one
    
    # If none of the formats match, return the original date string
    return date_str

def convert_to_date(date_str):
    if "days ago" in date_str:
        try:
            days_ago = int(date_str.split()[0])
            current_date = datetime.now()
            target_date = current_date - timedelta(days=days_ago)
            return target_date.strftime("%d-%m-%Y")
        except ValueError:
            days_ago = int(date_str.split()[1])
            current_date = datetime.now()
            target_date = current_date - timedelta(days=days_ago)
            return target_date.strftime("%d-%m-%Y")
    elif "A day ago" in date_str:
        current_date = datetime.now()
        target_date = current_date - timedelta(days=1)
        return target_date.strftime("%d-%m-%Y")
    elif "hours ago" in date_str:
        try:
            hours_ago = int(date_str.split()[0])
            current_date = datetime.now()
            target_date = current_date - timedelta(hours=hours_ago)
            return target_date.strftime("%d-%m-%Y")
        except ValueError:
            hours_ago = 2
            current_date = datetime.now()
            target_date = current_date - timedelta(hours=hours_ago)
            return target_date.strftime("%d-%m-%Y")
    elif "An hour ago" in date_str:
        hours_ago=1
        current_date=datetime.now()
        target_date= current_date - timedelta(hours=hours_ago)
        return target_date.strftime("%d-%m-%Y")
    elif "Updated" in date_str:
        formatted_date = date_str.split()[-2] + " " + date_str.split()[-1]
        return parse_date_string(formatted_date)
    elif "," in date_str:
        return parse_date_string(date_str)
    else:
        return parse_date_string(date_str)
    
#print(convert_to_date("Updated hours ago"))