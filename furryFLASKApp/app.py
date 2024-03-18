# Citation Scope: Sample Flask application for database connection and CRUD operation for each page
# Date: 3/18/2024
# Team Member: Yushu Sun and Tomomi Watanabe Hudspath
# Originality: Adopted
# Source: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# database connection info
app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_'  #osu username
app.config['MYSQL_PASSWORD'] = ''        #last 4 of db pass   
app.config['MYSQL_DB'] = 'cs340_'    #osu username
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes
# have homepage route to /people by default for convenience, generally this will be your home route with its own template
# @app.route("/")
# def home():
#     return redirect("/dogs")
@app.route("/")
def home():
    return redirect("/index")

# route to home page index
@app.route("/index", methods=["POST", "GET"])
def index():
    return render_template("index.j2")

# route for adopters page
@app.route("/adopters", methods=["POST", "GET"])
def adopters():
    # Separate out the request methods, in this case this is for a POST
    # insert a adopter into the Adopters entity
    if request.method == "POST":
        # fire off if user presses the Add Adopter button
        if request.form.get("Add_Adopter"):
            # grab user form inputs
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            street_address = request.form["street_address"]
            apt_suite_other = request.form["apt_suite_other"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            phone = request.form["phone"]
            email = request.form["email"]

            #run query getting the attributed from the data dictionary
            query = "INSERT INTO Adopters(first_name, last_name, street_address, apt_suite_other, city, state, zip, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, street_address, apt_suite_other, city, state, zip, phone, email))
            mysql.connection.commit()  

            # redirect back to adopters page
            return redirect("/adopters")
        

    # Grab Adopters table data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the adopers in Adopters table
        ###################################################
        query = "SELECT * FROM Adopters"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_adopters page passing our query data and adopter_data to the edit_adopters template
        return render_template("adopters.j2", data=data)

# route for delete functionality, deleting a dog from Dogs table,
# we want to pass the 'id' value of that dog on button click (see HTML) via the route
# @app.route("/delete_adopters/<int:adopter_id>")
# def delete_adopters(adopter_id):
#     # mySQL query to delete the adopter with our passed id
#     #query = "DELETE FROM bsg_people WHERE id = '%s';"
#     query = "DELETE FROM Adopters WHERE adopter_id = '%s';"
#     cur = mysql.connection.cursor()
#     cur.execute(query, (adopter_id,))
#     mysql.connection.commit()

#     # redirect back to dog page
#     return redirect("/adopters")


# # route for edit functionality, updating the attributes of a adopter in Adopters table
# # similar to our delete route, we want to the pass the 'id' value of that dog on button click (see HTML) via the route
# @app.route("/edit_adopters/<int:adopter_id>", methods=["POST", "GET"])
# def edit_adopters(adopter_id):
#     if request.method == "GET":
#         # mySQL query to grab the info of the adopter with our passed id
#         query = "SELECT * FROM Adopters WHERE adopter_id = %s" % (adopter_id)
#         cur = mysql.connection.cursor()
#         cur.execute(query)
#         data = cur.fetchall()

#         # render edit_adopters page passing our query data and adopter data to the edit_adopters template
#         return render_template("edit_adopters.j2", data=data)

#     # meat and potatoes of our update functionality
#     if request.method == "POST":
#         # fire off if user clicks the 'Edit Adopter' button
#         if request.form.get("Edit_Adopter"):
#             # grab user form inputs
#             adopter_id = request.form["adopter_id"]
#             first_name = request.form["first_name"]
#             last_name = request.form["last_name"]
#             street_address = request.form["street_address"]
#             apt_suite_other = request.form["apt_suite_other"]
#             city = request.form["city"]
#             state = request.form["state"]
#             zip = request.form["zip"]
#             phone = request.form["phone"]
#             email = request.form["email"]

#             # null values input for these fields

#             query = "UPDATE Adopters SET first_name=%s,  last_name=%s, street_address=%s, apt_suite_other=%s, city=%s, state=%s, zip=%s, phone=%s, email=%s WHERE adopter_id =%s"
#             cur = mysql.connection.cursor()
#             cur.execute(query, (first_name, last_name, street_address, apt_suite_other, city, state, zip, phone, email, adopter_id))
#             mysql.connection.commit()
            
#             # redirect back to dogs page after we execute the update query
#             return redirect("/adopters")



@app.route("/breeds", methods=["POST", "GET"])
def breeds():
    # Separate out the request methods, in this case this is for a POST
    # insert a breed into the Breeds entity
    if request.method == "POST":
        print("add breed working")
        # fire off if user presses the Add Breed button
        if request.form.get("Add_Breed"):
            # grab user form inputs
            breed_name = request.form["breed_name"]
            
            #run query getting the attributed from the data dictionary
            query = "INSERT INTO Breeds(breed_name) VALUES (%s)"
            print("insert working")
            cur = mysql.connection.cursor()
            cur.execute(query, (breed_name,))
            mysql.connection.commit()  

            # redirect back to breeds page
            return redirect("/breeds")
        

    # Grab Breeds table data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the adopers in Breeds table
        ###################################################
        query = "SELECT * FROM Breeds"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("breeds.j2", data=data)


# route for dogs page
@app.route("/dogs", methods=["POST", "GET"])
def dogs():
    # Separate out the request methods, in this case this is for a POST
    # insert a dog into the Dogs entity
    if request.method == "POST":
        # fire off if user presses the Add Dog button
        if request.form.get("Add_Dog"):
            # grab user form inputs
            dog_name = request.form["dog_name"]
            age_years = request.form["age_years"]
            weight_lb = request.form["weight_lb"]
            sex = request.form["sex"]
            posted_date = request.form["posted_date"]
            date_vaccinated = request.form["date_vaccinated"]
            date_neutered = request.form["date_neutered"]
            date_microchipped = request.form["date_microchipped"]
            adopter_id = request.form["adopter_id"]
            date_adopted = request.form["date_adopted"]

            # # # null values input for these fields
            if date_adopted=="" and adopter_id=="0" and date_microchipped=="" and date_neutered=="" and date_vaccinated=="" and posted_date=="":

                # mySQL query to insert a new dog into Dogs with form inputs
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex))
                mysql.connection.commit()    

            elif date_adopted=="" and adopter_id=="0" and date_microchipped=="" and date_neutered=="" and date_vaccinated=="":  

                # mySQL query to insert a new dog into Dogs with form inputs
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date))
                mysql.connection.commit()

            elif date_adopted=="" and adopter_id=="0" and date_microchipped=="" and date_neutered=="":    

                # mySQL query to insert a new dog into Dogs with form inputs
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated) VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated))
                mysql.connection.commit()           


            elif date_adopted=="" and adopter_id=="0" and date_microchipped=="":           
                # mySQL query to insert a new dog into Dogs with form inputs
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered))
                mysql.connection.commit()  

            elif date_adopted=="" and adopter_id=="0": 
                # there would not be a case only date_adopted is null or adopter_id is null,  those 2 are together          
                # mySQL query to insert a new dog into Dogs with form inputs
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped))
                mysql.connection.commit()  

            # nullable adopter_id  
            elif adopter_id=="0":
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, date_adopted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, date_adopted))
                mysql.connection.commit()                  
           
            else:
            # example as no null inputs
                query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted) VALUES (%s, %s,%s,%s, %s, %s,%s,%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted))
                mysql.connection.commit()          


            #run query getting the attributed from the data dictionary
            # query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted) VALUES (%s, %s,%s,%s, %s, %s,%s,%s, %s, %s)"
            # cur = mysql.connection.cursor()
            # cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted))
            # mysql.connection.commit()  


            # redirect back to dogs page
            return redirect("/dogs")

    # Grab Dogs table data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the dogs in Dogs table
        ###################################################
        ####### Needs o work on using Adopter's name ######
        #query1 = "SELECT dog_id, dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, Adopters.adopter_id, date_adopted FROM Dogs LEFT JOIN Adopters ON Adopters.adopter_id = Dogs.adopter_id"
        query = "SELECT dog_id, dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, CONCAT(Adopters.first_name, ' ', Adopters.last_name) AS adopter_id, date_adopted FROM Dogs LEFT JOIN Adopters ON Adopters.adopter_id = Dogs.adopter_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab adopter_id/name data for our dropdown
        # query2 = "SELECT id, name FROM bsg_planets"
        query2 = "SELECT adopter_id, CONCAT(Adopters.first_name, ' ', Adopters.last_name) AS adopterName FROM Adopters"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        adopter_data = cur.fetchall()

        # render edit_dogs page passing our query data and adopter_data to the edit_dogs template
        return render_template("dogs.j2", data=data, adopter_ids=adopter_data)


# route for delete functionality, deleting a dog from Dogs table,
# we want to pass the 'id' value of that dog  on button click (see HTML) via the route
@app.route("/delete_dogs/<int:dog_id>")
def delete_dogs(dog_id):
    # mySQL query to delete the dog with our passed id
    #query = "DELETE FROM bsg_people WHERE id = '%s';"
    query = "DELETE FROM Dogs WHERE dog_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (dog_id,))
    mysql.connection.commit()

    # redirect back to dog page
    return redirect("/dogs")


# route for edit functionality, updating the attributes of a dog in Dogs table
# similar to our delete route, we want to the pass the 'id' value of that dog on button click (see HTML) via the route
@app.route("/edit_dogs/<int:dog_id>", methods=["POST", "GET"])
def edit_dogs(dog_id):
    if request.method == "GET":
        # mySQL query to grab the info of the dog with our passed id
        query = "SELECT * FROM Dogs WHERE dog_id = %s" % (dog_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab dog id/name data for our dropdown
        #query2 = "SELECT adopter_id, first_name FROM Adopters"
        query2 = "SELECT adopter_id, CONCAT(Adopters.first_name, ' ', Adopters.last_name) AS adopterName FROM Adopters"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        adopter_data = cur.fetchall()

        # render edit_dogs page passing our query data and adopter data to the edit_dogs template
        return render_template("edit_dogs.j2", data=data, adopter_ids=adopter_data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Dog' button
        if request.form.get("Edit_Dog"):
            # grab user form inputs
            dog_id = request.form["dog_id"]
            dog_name = request.form["dog_name"]
            age_years = request.form["age_years"]
            weight_lb = request.form["weight_lb"]
            sex = request.form["sex"]
            posted_date = request.form["posted_date"]
            date_vaccinated = request.form["date_vaccinated"]
            date_neutered = request.form["date_neutered"]
            date_microchipped = request.form["date_microchipped"]
            adopter_id = request.form["adopter_id"]
            date_adopted = request.form["date_adopted"]

            # null values input for these fields
            if (date_adopted=="" or date_adopted==None) and adopter_id=="0": 
                # there would not be a case only date_adopted is null or adopter_id is null,  those 2 are together          
                # mySQL query to insert a new dog into Dogs with form inputs
                query = "UPDATE Dogs SET dog_name=%s,  age_years=%s, weight_lb=%s, sex=%s, posted_date=%s, date_vaccinated=%s, date_neutered=%s, date_microchipped=%s, adopter_id=NULL, date_adopted=NULL WHERE dog_id =%s"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, dog_id))
                mysql.connection.commit()    

            elif adopter_id=="0":
                query = "UPDATE Dogs SET dog_name=%s,  age_years=%s, weight_lb=%s, sex=%s, posted_date=%s, date_vaccinated=%s, date_neutered=%s, date_microchipped=%s, adopter_id=NULL, date_adopted=%s WHERE dog_id =%s"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, date_adopted, dog_id))
                mysql.connection.commit() 

            else:
            # example as no null inputs
                query = "UPDATE Dogs SET dog_name=%s,  age_years=%s, weight_lb=%s, sex=%s, posted_date=%s, date_vaccinated=%s, date_neutered=%s, date_microchipped=%s, adopter_id=%s, date_adopted=%s WHERE dog_id =%s"
                cur = mysql.connection.cursor()
                cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted, dog_id))
                mysql.connection.commit()        
            
            # redirect back to dogs page after we execute the update query
            return redirect("/dogs")


# route for dogs_breed_records page
@app.route("/dogs_breed_records", methods=["POST", "GET"])
def dogs_breed_records():
    # Separate out the request methods, in this case this is for a POST
    # insert a dogs breed records into the Dogs Breed Records entity
    if request.method == "POST":
        # fire off if user presses the Add_Dogs_Breed_Records button
        if request.form.get("Add_Dogs_Breed_Records"):
            # grab user form inputs
            breed_id = request.form["breed_id"]
            dog_id = request.form["dog_id"]

            #run query getting the attributed from the data dictionary
            query = "INSERT INTO Dogs_Breed_Records(breed_id, dog_id) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (breed_id, dog_id))
            mysql.connection.commit()  

            # redirect back to dogs_breed_records page
            return redirect("/dogs_breed_records")
        

    # Grab Dogs_Breed_Records table data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the dog breed in Dogs_Breed_Records table
        ###################################################
        query = "SELECT Dogs_Breed_Records.dog_breed_record_id,  Breeds.breed_name AS breedName, Dogs.dog_name AS dogName FROM Dogs_Breed_Records INNER JOIN Breeds ON Breeds.breed_id = Dogs_Breed_Records.breed_id INNER JOIN Dogs ON Dogs.dog_id = Dogs_Breed_Records.dog_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab breed_id/breed_name data for our dropdown
        #query2 = "SELECT DISTINCT Breeds.breed_id, breed_name AS breedName FROM Breeds INNER JOIN Dogs_Breed_Records ON Dogs_Breed_Records.breed_id =  Breeds.breed_id INNER JOIN Dogs ON Dogs.dog_id = Dogs_Breed_Records.dog_id"
        query2 = "SELECT Breeds.breed_id, breed_name AS breedName FROM Breeds"    # shwo all Breeds 
        cur = mysql.connection.cursor()
        cur.execute(query2)
        breed_data = cur.fetchall()

        # mySQL query to grab dog_id/dog_name data for our dropdown
        query3 = "SELECT dog_id, dog_name AS dogName FROM Dogs"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        dog_data = cur.fetchall()

        # render edit_dogs page passing our query data and adopter_data to the edit_dogs template
        return render_template("dogs_breed_records.j2", data=data, breed_ids=breed_data, dog_ids=dog_data)

# route for delete functionality, deleting a person from dogs breed records table
# pass the 'id' value of that dog breed record id on button click (see HTML) vi the route
@app.route("/delete_dogs_breed_records/<int:dog_breed_record_id>")
def delete_dogs_breed_records(dog_breed_record_id):
    # mySQL query to delete the dog breed record with passed in id
    query = "DELETE FROM Dogs_Breed_Records WHERE Dogs_Breed_Records.dog_breed_record_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (dog_breed_record_id,))
    mysql.connection.commit()

    # redirect back to dogs_breed_records page
    return redirect("/dogs_breed_records")

# rounte for edit dogs breed records functionality, updating the attributes of a dog breed in Dogs_Breed_Records table
# similar to delete route, pass the 'id' value of that dog breed record on button click 
@app.route("/edit_dogs_breed_records/<int:dog_breed_record_id>", methods=["POST", "GET"])
def edit_dogs_breed_records(dog_breed_record_id):
    if request.method == "GET":
        # mySQL query to grab the infor of the dog breed record with passed in id
        # query = "SELECT * FROM Dogs_Breed_Records WHERE Dogs_Breed_Records.dog_breed_record_id = %s" % (dog_breed_record_id)
        query = "SELECT Dogs_Breed_Records.dog_breed_record_id, breed_name, dog_name FROM Dogs_Breed_Records INNER JOIN Breeds ON Dogs_Breed_Records.breed_id = Breeds.breed_id INNER JOIN Dogs ON Dogs_Breed_Records.dog_id = Dogs.dog_id WHERE Dogs_Breed_Records.dog_breed_record_id= %s" % (dog_breed_record_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        ## breed_id and dog_ied to pass for dropdown to be selected 
        queryDD = "SELECT Dogs_Breed_Records.dog_breed_record_id, Breeds.breed_id, Dogs.dog_id FROM Dogs_Breed_Records INNER JOIN Breeds ON Dogs_Breed_Records.breed_id = Breeds.breed_id INNER JOIN Dogs ON Dogs_Breed_Records.dog_id = Dogs.dog_id WHERE Dogs_Breed_Records.dog_breed_record_id= %s" % (dog_breed_record_id)
        cur = mysql.connection.cursor() 
        cur.execute(queryDD)
        breed_dog_id = cur.fetchall()

        # mySQL query to grab dog breed record id and name data for dropdown
        #query2 = "SELECT DISTINCT Breeds.breed_id, breed_name AS breedName FROM Breeds INNER JOIN Dogs_Breed_Records ON Dogs_Breed_Records.breed_id =  Breeds.breed_id INNER JOIN Dogs ON Dogs.dog_id = Dogs_Breed_Records.dog_id"
        query2 = "SELECT DISTINCT Breeds.breed_id, breed_name AS breedName FROM Breeds"   ## Show All Breeds
        cur = mysql.connection.cursor() 
        cur.execute(query2)
        breed_data = cur.fetchall()

        # mySQL query to grab dog breed record id and name data for dropdown
        query3 = "SELECT dog_id, dog_name AS dogName FROM Dogs"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        dog_data = cur.fetchall() 

        # render edit_dogs page passing our query data and adopter data to the edit_dogs template
        return render_template("edit_dogs_breed_records.j2", data=data, breed_dog_id=breed_dog_id, breed_ids=breed_data, dog_ids=dog_data)


    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Dog Breed Record' button 
        if request.form.get("Edit_Dog_Breed_Record"):
            # grab user form inputs
            dog_breed_record_id = request.form["dog_breed_record_id"]
            breed_id = request.form["breed_id"]
            dog_id = request.form["dog_id"]
            
            query = "UPDATE Dogs_Breed_Records SET breed_id=%s, dog_id=%s WHERE dog_breed_record_id =%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (breed_id, dog_id, dog_breed_record_id))
            mysql.connection.commit() 

            return redirect("/dogs_breed_records")



#################################################################################################

# route for Cats page
@app.route("/cats", methods=["POST", "GET"])
def cats():
    # Separate out the request methods, in this case this is for a POST
    # insert a person into the bsg_people entity
    if request.method == "POST":
        # fire off if user presses the Add Cat button
        if request.form.get("Add_Cat"):
            # grab user form inputs
            cat_name = request.form["cat_name"]
            age_years = request.form["age_years"]
            weight_lb = request.form["weight_lb"]
            sex = request.form["sex"]
            posted_date = request.form["posted_date"]
            date_vaccinated = request.form["date_vaccinated"]
            date_neutered = request.form["date_neutered"]
            date_microchipped = request.form["date_microchipped"]
            adopter_id = request.form["adopter_id"]
            date_adopted = request.form["date_adopted"]


        if date_adopted=="" and adopter_id=="0" and date_microchipped=="" and date_neutered=="" and date_vaccinated=="" and posted_date=="":

            # mySQL query to insert a new cat into Cats with form inputs
            query = "INSERT INTO Cats (cat_name, age_years, weight_lb, sex) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex))
            mysql.connection.commit()    

        elif date_adopted=="" and adopter_id=="0" and date_microchipped=="" and date_neutered=="" and date_vaccinated=="":  

            # mySQL query to insert a new cat into Cats with form inputs
            query = "INSERT INTO Cats (cat_name, age_years, weight_lb, sex, posted_date) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date))
            mysql.connection.commit()

        elif date_adopted=="" and adopter_id=="0" and date_microchipped=="" and date_neutered=="":    

            # mySQL query to insert a new cat into Cats with form inputs
            query = "INSERT INTO Cats (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated) VALUES (%s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated))
            mysql.connection.commit()           


        elif date_adopted=="" and adopter_id=="0" and date_microchipped=="":           
            # mySQL query to insert a new cat into Cats with form inputs
            query = "INSERT INTO Cats (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered))
            mysql.connection.commit()  

        elif date_adopted=="" and adopter_id=="0": 
            # there would not be a case only date_adopted is null or adopter_id is null,  those 2 are together          
            # mySQL query to insert a new cat into Cats with form inputs
            query = "INSERT INTO Cats (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped))
            mysql.connection.commit()  

        # nullable adopter_id  
        elif adopter_id=="0":
            query = "INSERT INTO Cats(cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, date_adopted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, date_adopted))
            mysql.connection.commit()   

        else:
            query = "INSERT INTO Cats (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted) VALUES (%s, %s,%s,%s, %s, %s,%s,%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted))
            mysql.connection.commit()       

        # redirect back to people page
        return redirect("/cats")

    # Grab bsg_people data so we send it to our template to display
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query = "SELECT cat_id, cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, CONCAT(Adopters.first_name, ' ', Adopters.last_name) AS adopter_id, date_adopted FROM Cats LEFT JOIN Adopters ON Adopters.adopter_id =Cats.adopter_id"
        cur.execute(query)
        data = cur.fetchall()  # Fetch all cat data

        # mySQL query to grab adopter_id/name data for our dropdown
        # query2 = "SELECT id, name FROM bsg_planets"
        query2 = "SELECT adopter_id, CONCAT(Adopters.first_name, ' ', Adopters.last_name) AS adopterName FROM Adopters"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        adopter_data = cur.fetchall()

        return render_template("cats.j2", data=data, adopter_ids=adopter_data)

# route for delete functionality, deleting a cat from Cats,
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_cats/<int:cat_id>")
def delete_cats(cat_id):
    # mySQL query to delete the person with our passed id
    #query = "DELETE FROM bsg_people WHERE id = '%s';"
    query = "DELETE FROM Cats WHERE cat_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (cat_id,))
    mysql.connection.commit()

    # redirect back to cats page
    return redirect("/cats")
        
# route for edit functionality, updating the attributes of a person in bsg_people
# similar to our delete route, we want to the pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/edit_cats/<int:cat_id>", methods=["POST", "GET"])
def edit_cats(cat_id):
    if request.method == "GET":
        # mySQL query to grab the info of the cat with our passed id
        query = "SELECT * FROM Cats WHERE cat_id = %s" % (cat_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab cat id/name data for our dropdown
        #query2 = "SELECT adopter_id, first_name FROM Adopters"
        query2 = "SELECT adopter_id, CONCAT(Adopters.first_name, ' ', Adopters.last_name) AS adopterName FROM Adopters"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        adopter_data = cur.fetchall()

        # render edit_cats page passing our query data and adopter data to the edit_cats template
        return render_template("edit_cats.j2", data=data, adopter_ids=adopter_data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Cat' button
        if request.form.get("Edit_Cat"):
            # grab user form inputs
            cat_id = request.form["cat_id"]
            cat_name = request.form["cat_name"]
            age_years = request.form["age_years"]
            weight_lb = request.form["weight_lb"]
            sex = request.form["sex"]
            posted_date = request.form["posted_date"]
            date_vaccinated = request.form["date_vaccinated"]
            date_neutered = request.form["date_neutered"]
            date_microchipped = request.form["date_microchipped"]
            adopter_id = request.form["adopter_id"]
            date_adopted = request.form["date_adopted"]

            #querye = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = %s WHERE bsg_people.id = %s"
            query = "UPDATE Cats SET cat_name=%s,  age_years=%s, weight_lb=%s, sex=%s, posted_date=%s, date_vaccinated=%s, date_neutered=%s, date_microchipped=%s, adopter_id=%s, date_adopted=%s WHERE cat_id =%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (cat_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted, cat_id))
            mysql.connection.commit()
            

            # redirect back to cats page after we execute the update query
            return redirect("/cats")

# route for cats_breed_records page
@app.route("/cats_breed_records", methods=["POST", "GET"])
def cats_breed_records():
    # Separate out the request methods, in this case this is for a POST
    # insert a cats breed records into the Cats Breed Records entity
    if request.method == "POST":
        # fire off if user presses the Add_Cats_Breed_Records button
        if request.form.get("Add_Cats_Breed_Records"):
            # grab user form inputs
            breed_id = request.form["breed_id"]
            cat_id = request.form["cat_id"]

            #run query getting the attributed from the data dictionary
            query = "INSERT INTO Cats_Breed_Records(breed_id, cat_id) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (breed_id, cat_id))
            mysql.connection.commit()  

            # redirect back to cats_breed_records page
            return redirect("/cats_breed_records")
        

    # Grab Cats_Breed_Records table data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the cat breed in Cats_Breed_Records table
        ###################################################
        query = "SELECT Cats_Breed_Records.cat_breed_record_id, Breeds.breed_name AS breedName, Cats.cat_name AS catName FROM Cats_Breed_Records INNER JOIN Breeds ON Breeds.breed_id = Cats_Breed_Records.breed_id INNER JOIN Cats ON Cats.cat_id = Cats_Breed_Records.cat_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab breed_id/breed_name data for our dropdown
        # query2 = "SELECT Breeds.breed_name AS breedName FROM Breeds INNER JOIN Cats_Breed_Records ON Cats_Breed_Records.breed_id =  Breeds.breed_id INNER JOIN Cats ON Cats.cat_id = Cats_Breed_Records.cat_id"
        query2 = "SELECT Breeds.breed_id, breed_name AS breedName FROM Breeds"    # show all Breeds
        cur = mysql.connection.cursor()
        cur.execute(query2)
        breed_data = cur.fetchall()

        # mySQL query to grab cat_id/cat_name data for our dropdown
        query3 = "SELECT cat_id, cat_name AS catName FROM Cats"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        cat_data = cur.fetchall()

        query4 = "SELECT breed_name from Breeds"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        breeds = cur.fetchall()

        # render edit_cats page passing our query data and adopter_data to the edit_cats template
        return render_template("cats_breed_records.j2", data=data, breed_ids=breed_data, cat_ids=cat_data, breeds=breeds)

# route for delete functionality, deleting a person from cats breed records table
# pass the 'id' value of that cat breed record id on button click (see HTML) vi the route
@app.route("/delete_cats_breed_records/<int:cat_breed_record_id>")
def delete_cats_breed_records(cat_breed_record_id):
    # mySQL query to delete the cat breed record with passed in id
    query = "DELETE FROM Cats_Breed_Records WHERE Cats_Breed_Records.cat_breed_record_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (cat_breed_record_id,))
    mysql.connection.commit()

    # redirect back to cats_breed_records page
    return redirect("/cats_breed_records")

# rounte for edit cats breed records functionality, updating the attributes of a cat breed in Cats_Breed_Records table
# similar to delete route, pass the 'id' value of that cat breed record on button click 
@app.route("/edit_cats_breed_records/<int:cat_breed_record_id>", methods=["POST", "GET"])
def edit_cats_breed_records(cat_breed_record_id):
    if request.method == "GET":
        # mySQL query to grab the infor of the cat breed record with passed in id
        query = "SELECT Cats_Breed_Records.cat_breed_record_id, breed_name, cat_name FROM Cats_Breed_Records INNER JOIN Breeds ON Cats_Breed_Records.breed_id = Breeds.breed_id INNER JOIN Cats ON Cats_Breed_Records.cat_id = Cats.cat_id WHERE Cats_Breed_Records.cat_breed_record_id = %s" % (cat_breed_record_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        ## breed_id and cat_ied to pass for dropdown to be selected 
        queryDD = "SELECT Cats_Breed_Records.cat_breed_record_id, Breeds.breed_id, Cats.cat_id FROM Cats_Breed_Records INNER JOIN Breeds ON Cats_Breed_Records.breed_id = Breeds.breed_id INNER JOIN Cats ON Cats_Breed_Records.cat_id = Cats.cat_id WHERE Cats_Breed_Records.cat_breed_record_id= %s" % (cat_breed_record_id)
        cur = mysql.connection.cursor() 
        cur.execute(queryDD)
        breed_cat_id = cur.fetchall()

        # mySQL query to grab cat breed record id and name data for dropdown
        # query2 = "SELECT DISTINCT Breeds.breed_id, breed_name AS breedName FROM Breeds INNER JOIN Cats_Breed_Records ON Cats_Breed_Records.breed_id =  Breeds.breed_id INNER JOIN Cats ON Cats.cat_id = Cats_Breed_Records.cat_id"
        query2 = "SELECT DISTINCT Breeds.breed_id, breed_name AS breedName FROM Breeds"   # Show All Breeds
        cur = mysql.connection.cursor()
        cur.execute(query2)
        breed_data = cur.fetchall()

        # mySQL query to grab cat breed record id and name data for dropdown
        query3 = "SELECT cat_id, cat_name AS catName FROM Cats"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        cat_data = cur.fetchall() 

        # render edit_cats page passing our query data and adopter data to the edit_cats template
        return render_template("edit_cats_breed_records.j2", data=data, breed_ids=breed_data, cat_ids=cat_data, breed_cat_id=breed_cat_id)


    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Cat Breed Record' button 
        if request.form.get("Edit_Cat_Breed_Record"):
            # grab user form inputs
            cat_breed_record_id = request.form["cat_breed_record_id"]
            breed_id = request.form["breed_id"]
            cat_id = request.form["cat_id"]

            # # null values input for these fields or Edit Cat Breed Record dropdowns
            ################
   
             
            query = "UPDATE Cats_Breed_Records SET breed_id=%s, cat_id=%s WHERE cat_breed_record_id =%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (breed_id, cat_id, cat_breed_record_id))
            mysql.connection.commit() 

            return redirect("/cats_breed_records")



#################################################################################################


# Listener 
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=65326, debug=True)

#host="flip2.engr.oregonstate.edu"