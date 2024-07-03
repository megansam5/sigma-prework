from datetime import datetime
current = datetime.now()
while True:
    date_string = input("Please enter a date in the format dd/mm/yyyy: ")
    try:
        date_object = datetime.strptime(date_string, '%d/%m/%Y')
        break
    except:
        print('Please use the correct format.')
        continue
difference = current - date_object
years = difference.days // 365
print(f'A person born on that date is {years} years old.')