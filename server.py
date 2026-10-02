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

# ===========================================================
#  Path parameter
# http://127.0.0.1:5000/greet/lina
@app.get("/greet/<string:student_name>")
def greet(student_name):
        return jsonify({"message": f"Ey hello {student_name}"}), 200 # OK
    
    
# ---------- Products ------------
products = [
        {
            "_id": 1,
            "name": "cake",
            "price": 25
        },
        {
            "_id": 2,
            "name": "ice-cream",
            "price": 5
        },
        {
            "_id": 3,
            "name": "cookie",
            "price": 3
        },
        {
            "_id": 4,
            "name": "chocolate",
            "price": 10
        },
]


# MINI-CHALLENGE
# GET /api/products -> RETURN A LIST OF PRODUCTS
# http://127.0.0.1:5000/api/products
@app.get("/api/products")
def get_products():
        return jsonify(products), 200


@app.get("/api/products/<int:product_id>")
def get_product_by_id(product_id):
        for product in products:
            print(product)
            if product["_id"] == product_id:
                return jsonify(product), 200
    
        return jsonify("Product not found"), 404 #NOT FOUND 
        
    
# ============= ASSIGNMENT 1 =================
# ---------- Coupons ------------
# http://127.0.0.1:5000/api/coupons
# http://127.0.0.1:5000/api/coupons/count
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
        return jsonify(coupons_count)


# ============= ASSIGNMENT 2 ================= 
# Implement the following RESTful endpoints for the coupons resource:
# http://127.0.0.1:5000/api/coupons/3  
# endpoint that returns a coupons that matches the given id.
@app.get("/api/coupons/<int:coupon_id>")
def get_coupon_by_id(coupon_id):
        for coupon in coupons:
            print (coupon)
            if coupon["_id"] == coupon_id:
# implement proper HTTP status codes for each response, including success and error cases.
                return jsonify (coupon), 200
            
# if the coupon is not found, return an appropiate error message.
        return jsonify("Coupon not found"), 404 
   
    
# enable Hot reload so turn on the server every single time its not necesary
app.run(debug=True)



