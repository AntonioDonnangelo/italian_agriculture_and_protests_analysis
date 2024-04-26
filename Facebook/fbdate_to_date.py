from datetime import datetime
#import locale

# trasforma una data del tipo "marzo 27 alle ore 3:15 PM", "marzo 4" o "dicembre 6, 2023" in un oggetto date yyyy-mm-dd

def string_to_date(date):
    current_year = datetime.now().year
    #locale.setlocale(locale.LC_TIME, "it_IT.UTF-8")
    date_list = date.split()
    if len(date_list) == 5: # esempio: April 19 at 8:02 AM
        date_list = date_list[0:2]
        # adesso procedo come nel caso len(date_list) == 2
        date_list.extend([str(current_year)])
        new_date = " ".join(date_list)
        string_format = "%B %d %Y"
        return datetime.strptime(new_date, string_format).date()
    if len(date_list) == 2: # esempio: March 3 
        date_list.extend([str(current_year)])
        new_date = " ".join(date_list)
        string_format = "%B %d %Y"
        return datetime.strptime(new_date, string_format).date()
    if len(date_list) == 3: # December 6, 2023
        string_format = "%B %d, %Y"
        return datetime.strptime(date, string_format).date()
    
