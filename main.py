from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['assure_db2']  # Replace 'insurance_db' with your desired database name

# Step 2.1: Read the CSV file
import pandas as pd

csv_path = 'assignment_raw_rate.csv'
df = pd.read_csv(csv_path)

# Step 2.2: Load CSV data into MongoDB collection
collection = db['premium_rates']  # Replace 'premium_rates' with your desired collection name

# Convert the DataFrame to a dictionary for easy insertion
data = df.to_dict('records')

# Insert the data into the MongoDB collection
collection.insert_many(data)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

def calculate_premium_logic(adult_1_age, adult_2_age, city_tier, sum_insured, tenure, num_children, child_ages):
    # print(adult_1_age, adult_2_age, city_tier, sum_insured, tenure, num_children, child_ages)
    adult_2_discount = 0
    #Logic of the Assignment
    if(adult_1_age > 0 )or ( adult_2_age > 0 ):
        if(adult_1_age > adult_2_age):
            adult_1_discount = base_rate(adult_1_age,tenure,sum_insured,city_tier)
            if(adult_2_age > 0):
                adult_2_discount = base_rate(adult_2_age,tenure,sum_insured,city_tier) * 0.50
        else:
            adult_2_discount = base_rate(adult_2_age,tenure,sum_insured,city_tier)
            if(adult_1_age > 0):
                adult_1_discount = base_rate(adult_1_age,tenure,sum_insured,city_tier) * 0.50
    adult_premium = adult_1_discount + adult_2_discount

    child_discount = 0
    if(num_children >0):
        for child in child_ages.values():
            child_discount += base_rate(child,tenure,sum_insured,city_tier) * 0.50
    print("Children total discount : ",child_discount)

    print("Final value of adult : ", adult_premium)  

    total_premium = child_discount + adult_premium
    print("The final Premium value for a Family/Individual", total_premium)   

    return total_premium


def base_rate(age,tenure,sum_insured,tier):

    Rate = collection.find_one({
        'TierID': tier,
        'Age': age,
        'Tenure': tenure,
        'SumInsured': sum_insured
        
    }, {'Rate': 1})

    if Rate:
        # (Rate['Rate'])
        return Rate['Rate']
        
    else:
        print("Rate not found.")

# Route for calculating premium
@app.route('/calculate_premium', methods=['POST'])
def calculate_premium():
    adult_1_age = int(request.form['adult_1_age'])
    adult_2_age = int(request.form['adult_2_age']) if request.form['adult_2_age'] else 0
    city_tier = int(request.form['city_tier'])
    sum_insured = int(request.form['sum_insured'])
    tenure = int(request.form['tenure'])
    children_checkbox = request.form.get('children')
    num_children = int(request.form.get('num_children', 0)) if children_checkbox else 0
    print("This pprints the number of children")
    print(num_children)
    child_ages = {}

    #children checkbox is checked
    if num_children > 0:
        for i in range(1, num_children + 1):
            child_ages[f'child_age_{i}'] = int(request.form.get(f'child_age_{i}', 0))
    
    premium = calculate_premium_logic(adult_1_age, adult_2_age, city_tier, sum_insured, tenure, num_children, child_ages)

    # Save premium details to MongoDB
    # premium_data = {
    #     'adult_1_age': adult_1_age,
    #     'adult_2_age': adult_2_age,
    #     'city_tier': city_tier,
    #     'sum_insured': sum_insured,
    #     'tenure': tenure,
    #     'premium': premium
    # }
    # collection.insert_one(premium_data)

    return render_template('result.html', premium=premium)

if __name__ == '__main__':
    app.run()
