# Adopted from Sample Flask application for a BSG database, snapshot of BSG_people design
# souce: https://github.com/osu-cs340-ecampus/flask-starter-app

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
@app.route("/")
def home():
    return redirect("/dogs")
# @app.route("/")
# def home():
#     return redirect("/index")

# route to home page index
@app.route("/index", methods=["POST", "GET"])
def index():
    return render_template("index.j2")

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

            #########################################################################################
            # data_dogs = {}   # holds dogs data 

            # # request.form.items will get all the values from the form and reurns to dictionary
            # for key, value in request.form.items():  
            #     if value == '' or value == 0:
            #         data_dogs[key] = None
            #     else: 
            #         data_dogs[key] = value

            # # insertin values to Dogs table  
            # add_dogs = ("INSERT INTO Dogs "
            #   "(dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted) "
            #   "VALUES (%(dog_name)s, %(age_years)s,%(weight_lb)s,%(sex)s, %(posted_date)s, %(date_vaccinated)s,%(date_neutered)s,%(date_microchipped)s, %(adopter_id)s, %(date_adopted)s)")  
            # cur = mysql.connection.cursor()
            # cur.execute(add_dogs, data_dogs)
            # mysql.connection.commit()   
            ##########################################################################################


            # # null values input for these fields
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


            # redirect back to people page
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


# route for delete functionality, deleting a person from bsg_people,
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_dogs/<int:dog_id>")
def delete_dogs(dog_id):
    # mySQL query to delete the person with our passed id
    #query = "DELETE FROM bsg_people WHERE id = '%s';"
    query = "DELETE FROM Dogs WHERE dog_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (dog_id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/dogs")


# route for edit functionality, updating the attributes of a person in bsg_people
# similar to our delete route, we want to the pass the 'id' value of that person on button click (see HTML) via the route
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


            # # account for null age AND homeworld
            # if (age == "" or age == "None") and homeworld == "0":
            #     # mySQL query to update the attributes of person with our passed id value
            #     query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = NULL WHERE bsg_people.id = %s"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, id))
            #     mysql.connection.commit()

            # # account for null homeworld
            # elif homeworld == "0":
            #     query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = %s WHERE bsg_people.id = %s"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, age, id))
            #     mysql.connection.commit()

            # # account for null age
            # elif age == "" or age == "None":
            #     query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = NULL WHERE bsg_people.id = %s"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, homeworld, id))
            #     mysql.connection.commit()

            # # no null inputs
            # else:
            #     query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = %s WHERE bsg_people.id = %s"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, homeworld, age, id))
            #     mysql.connection.commit()


            #querye = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = %s WHERE bsg_people.id = %s"
            # query = "UPDATE Dogs SET dog_name=%s,  age_years=%s, weight_lb=%s, sex=%s, posted_date=%s, date_vaccinated=%s, date_neutered=%s, date_microchipped=%s, adopter_id=%s, date_adopted=%s WHERE dog_id =%s"
            # cur = mysql.connection.cursor()
            # cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted, dog_id))
            # mysql.connection.commit()
            

            # redirect back to dogs page after we execute the update query
            return redirect("/dogs")



# route for  page
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
        query = "SELECT * FROM Cats"
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


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=65327, debug=True)