import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def clean_and_save_csv():
    # Open a file dialog to select the input CSV file
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not filename:
        messagebox.showerror("Error", "Hello! Please select a CSV file.")
        return

    try:
        # Initialize lists for cleaned data
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
        baby_formula = []
        diaper_size = []
        dairy = []
        frozen = []
        refrigerated_items = []
        beverages = []
        cooking_and_baking = []
        snack_foods = []
        toiletries = []
        cleaning_supplies = []
        pet_supplies = []
        other = []

        # Read the selected CSV file and perform data cleaning
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                family_id.append("Family #" + row['ID'])
                family_id.append( "Family #"  + row['ID'])
                acts_program.append("Acts Program: " + row['ACTS Program'])
                caseworker_name.append("Caseworker Name: " + row['Caseworker Name'])
                caseworker_phone_number.append("Caseworker Phone Number: " + row['Caseworker Phone Number'])
                caseworker_email.append("Caseworker Email: " + row['Caseworker Email'])
                client_program.append("Client Program: " + row['My Client(s) Require: '])
                adults.append("Number of Adults:(age 18-64) " + row["Number Adults (age 18-64) in household"])
                children.append("Number of Adults:(Under 18) " + row["Number Children (age 0-17) in household"])
                seniors.append("Number Seniors (age 65 and up)" + row["Number Seniors (age 65 and up) in household"])
                canned_goods.append("Number of Canned Goods" + row["Canned Goods"])
                dry_goods.append("Number of Dry Goods: " + row["Dry Goods"])
                frozen_items.append("Number of Frozen Items: " + row["Frozen Items"])
                fresh_produce.append("Number of Fresh Produce Items: " + row["Fresh Produce"])
                baby_formula.append("Baby Formula Type: " + row["Baby Formula - type"])
                diaper_size.append("Diaper Size: " + row["Diapers - size(s)"])
                dairy.append("Dairy and Non Dairy: " + row["Dairy and Non Dairy"])
                frozen.append("Frozen: " + row["Frozen"])
                refrigerated_items.append("Refrigerated Items: " + row["Refrigerated Items"])
                beverages.append("Beverages: " + row["Beverages"])
                cooking_and_baking.append("Cooking and Baking: " + row["Cooking and Baking"])
                snack_foods.append("Snack Foods: " + row["Snack Foods"])
                toiletries.append("Toiletries: " + row["Toiletries"])
                cleaning_supplies.append("Cleaning Supplies: " + row["Cleaning Supplies"])
                pet_supplies.append("Pet Supplies: " + row["Pet Supplies"])
                other.append("Other: " + row["Other"])


        # Create a new CSV file and write the cleaned data to it
        output_filename = 'cleaned_output.csv'
        with open(output_filename, mode='w', newline='') as hpcfile:
            hpc_writer = csv.writer(hpcfile)
            hpc_writer.writerow(family_id)
            hpc_writer.writerow(acts_program)
            hpc_writer.writerow(caseworker_name)
            hpc_writer.writerow(caseworker_phone_number)
            hpc_writer.writerow(caseworker_email)
            hpc_writer.writerow(client_program)
            hpc_writer.writerow(adults)
            hpc_writer.writerow(children)
            hpc_writer.writerow(seniors)
            hpc_writer.writerow(canned_goods)
            hpc_writer.writerow(dry_goods)
            hpc_writer.writerow(frozen_items)
            hpc_writer.writerow(fresh_produce)
            hpc_writer.writerow(baby_formula)
            hpc_writer.writerow(diaper_size)
            hpc_writer.writerow(dairy)
            hpc_writer.writerow(frozen)
            hpc_writer.writerow(refrigerated_items)
            hpc_writer.writerow(beverages)
            hpc_writer.writerow(cooking_and_baking)
            hpc_writer.writerow(snack_foods)
            hpc_writer.writerow(toiletries)
            hpc_writer.writerow(cleaning_supplies)
            hpc_writer.writerow(pet_supplies)
            hpc_writer.writerow(other)

        messagebox.showinfo("Success", "Here is your updated HPC Request Form. Output saved as 'hpc_request.csv'")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create a Tkinter window
root = tk.Tk()
root.title("CSV Data Cleaner")

# Create a button to trigger data cleaning and saving
clean_button = tk.Button(root, text="Clean and Save CSV", command=clean_and_save_csv)
clean_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()