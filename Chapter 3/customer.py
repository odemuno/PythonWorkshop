''' a customer relationship management CRM system to display names'''

def format_customer(first_name, last_name, location=None):
    # format the full name using string notation
    full_name = '%s %s' % (first_name, last_name)
    
    # if location is provided: John Smith (California)
    if location:
        return '%s (%s)' % (full_name, location)
    
    # if no location: John Smith
    else:
        return full_name
    