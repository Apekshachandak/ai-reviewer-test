def clean_user_input(text_string):
    text_string = text_string.strip() #hello
    text_string = text_string.lower()
    return text_string.replace(" ", "_")

def format_database_record(raw_data):
    raw_data = raw_data.strip()
    raw_data = raw_data.lower()
    return raw_data.replace(" ", "_")
