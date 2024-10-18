def validate_number(number, min, max) :
    try:
        if min <= number <= max:
            return number
        
    except ValueError:
        return None
        

def validate_lenght(str,lenght):
    try:
        if len(str) <= lenght:
            return str
        
    except ValueError:
        return None