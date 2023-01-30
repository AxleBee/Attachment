from  datetime import datetime

date_str = '09-19-2022'

date_object = datetime.strptime(date_str).date()
print(type(date_object))
print(date_object)  # printed in default format