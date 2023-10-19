import csv
filename = 'Hunger Prevention Center Food Request.csv'
with open (filename, 'r', encoding = 'utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    family_id = []
    acts_program = []
    caseworker_name = []
    caseworker_phone_number = []
    caseworker_email = []
    client_program = []
    adults = []
    children = []
    seniors = []
    canned_goods = []
    dry_goods = []
    frozen_items = []
    fresh_produce = []


    for row in reader:
        family_id.append( "Family #"  + row['ID'])
        acts_program.append("Acts Program: " + row['ACTS Program'])
        caseworker_name.append("Caseworker Name: " + row['Caseworker Name'])
        caseworker_phone_number.append("Caseworker Phone Number: " + row['Caseworker Phone Number'])
        caseworker_email.append("Caseworker Email: " + row['Caseworker Email'])
        client_program.append("Client Program: " + row['My Client(s) Require: '])
        adults.append("Number of Adults:(age 18-64) " + row["Number Adults (age 18-64) in household"])
        children.append("Number of Adults:(Under 18) " + row["Number Children (age 0-17) in household"])
        seniors.append("Number Seniors (age 65 and up)" + row["Number Seniors (age 65 and up) in household"])
        canned_goods.append("Number of Canned Goods" + row["Number of Canned Goods"])
        dry_goods.append("Number of Dry Goods" + row["Dry Goods"])
with open('hpcfoodrequest.csv', mode='w', newline='') as hpcfile:
      hpc_writer = csv.writer(hpcfile)
      hpc_writer.writerow(family_id)
      hpc_writer.writerow(acts_program)
      hpc_writer.writerow(caseworker_name)
      hpc_writer.writerow(caseworker_phone_number)
      hpc_writer.writerow(caseworker_email)
      hpc_writer.writerow(client_program)


      #for value in range (len(family_id)):
           #hpc_writer.writerow([family_id[value],acts_program[value],caseworker_name[value],caseworker_phone_number[value],caseworker_email[value],client_program[value]])
           

                    