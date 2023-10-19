#list of dictionaries

import csv
filename = 'Hunger Prevention Center Food Request.csv'

#read csv file
with open (filename, 'r', encoding = 'utf-8-sig') as csvfile:
  # creating a csv reader object
    reader = csv.DictReader(csvfile)
    #for row in reader:
      #print(row)
    for row in reader:
        family_id = row['ID']
        acts_program = row['ACTS Program']
        caseworker_name = row['Caseworker Name']
        caseworker_phone_number = row['Caseworker Phone Number']
        caseworker_email = row['Caseworker Email']
        client_program = row['My Client(s) Require: ']
      
        """caseworkers = {f'Family# :{family_id} ',  
                       f'Acts Program :{caseworker_name}', 
                       f'Caseworker Name :{caseworker_name} ', 
                       f'Caseworker Phone Number: {caseworker_phone_number}',
                       f'Caseworker Email: {caseworker_email}',
                       f'Client Program: {client_program  }'}"""
    print(family_id)

"""print(caseworkers)
with open('hpcfoodrequest.csv', mode='w', newline='') as hpcfile:
      hpc_writer = csv.writer(hpcfile)
      for case in caseworkers:
        hpc_writer.writerows([caseworkers])
    
    #hpc_writer.writerows([caseworkers])"""

"""families = [

{'Family # : , 'Number of Adults': , ' Number of Children': , 'Number of Seniors': , 'Canned Goods': , 	'Dry Goods' : , 'Frozen Items' : , 'Fresh Produce' : , 'Baby Formula - type': ,'Diapers - size(s)' : , 'Dairy and Non Dairy' : ,'Frozen' : , 'Refrigerated Items' : , 'Beverages' : , 'Cooking and Baking' : , 'Snack Foods' :	, 'Toiletries' : , 'Cleaning Supplies' : , 'Pet Supplies' : , 'Frozen' : , 'Other' : , 


]"""
