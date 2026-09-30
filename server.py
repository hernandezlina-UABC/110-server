from flask import Flask, jsonify

# __[]__ its an Dunder Method
app = Flask(__name__) # Instance of Flask


# http://127.0.0.1:5000/
@app.get("/")
def index():
    return jsonify("Welcome to Flask Framework")


# always "/" in a path 
# http://127.0.0.1:5000/say-hi
@app.get("/say-hi")
def hi():
        # jsonify transforms whatever its inside the return to json
        return jsonify("Hello Cohort 70")
    
    
# http://127.0.0.1:5000/students-coh-70
@app.get("/students-coh-70")
def get_students():
    students_names = ["Lina", "Khaleel", "Jose", "Leo"]
    return jsonify(students_names)


# http://127.0.0.1:5000/contact
@app.get("/contact")
def get_contact_information():
    contact_information = {
            "email": "lina.hernandez@sdgku.edu",
            "phone": "456-123-3211"
            }
    return jsonify(contact_information)


# http://127.0.0.1:5000/user-information
# MINI-CHALLENGE
# Create a /user-infomation endpoint
# Return a dictionary with: name, role, is_active, favorite_technologies
# Test it by visiting http://127.0.0.1:5000/user-information
@app.get("/user-information")
def get_user_information():
        user_information = {
            "name": "Lina",
            "role": "student",
            "is_active": True,
            "favorite_technologies": ["Bootstrap", "JavaScript"]
        }
        return jsonify(user_information)
    
    

# ---------- Coupons ------------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "WELCOME10", "discount": 10},
    {"_id": 3, "code": "WELCOME10", "discount": 10},
]
# GET /api/coupons endpoint that returns a list of coupons.
@app.get("/api/coupons")
def get_coupons():
        return jsonify(coupons)
# GET /api/coupons/count returns the number of coupons in the system.
# Don't forget to use python len() function
@app.get("/api/coupons/count")
def get_coupons_count():
        coupons_count = {
            "Total Coupons" : len(coupons)
        }
        return jsonify (coupons_count)
    
    
    
# enable Hot reload so turn on the server every single time its not necesary
app.run(debug=True)



