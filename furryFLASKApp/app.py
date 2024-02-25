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
app.config['MYSQL_USER'] = 'cs340_watantom'  #osu username
app.config['MYSQL_PASSWORD'] = '1710'        #last 4 of db pass   
app.config['MYSQL_DB'] = 'cs340_watantom'    #osu username 
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

            ###################################
            ##########Some conditional for null values ##############
            ###################################
            # # account for null age AND homeworld
            # if age == "" and homeworld == "0":
            #     # mySQL query to insert a new person into bsg_people with our form inputs
            #     query = "INSERT INTO bsg_people (fname, lname) VALUES (%s, %s)"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname))
            #     mysql.connection.commit()

            # # account for null homeworld
            # elif homeworld == "0":
            #     query = "INSERT INTO bsg_people (fname, lname, age) VALUES (%s, %s,%s)"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, age))
            #     mysql.connection.commit()

            # # account for null age
            # elif age == "":
            #     query = "INSERT INTO bsg_people (fname, lname, homeworld) VALUES (%s, %s,%s)"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, homeworld))
            #     mysql.connection.commit()

            # # no null inputs
            # else:
            #     query = "INSERT INTO bsg_people (fname, lname, homeworld, age) VALUES (%s, %s,%s,%s)"
            #     cur = mysql.connection.cursor()
            #     cur.execute(query, (fname, lname, homeworld, age))
            #     mysql.connection.commit()

            # example as no null inputs
            query = "INSERT INTO Dogs (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted) VALUES (%s, %s,%s,%s, %s, %s,%s,%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted))
            mysql.connection.commit()          


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
            query = "UPDATE Dogs SET dog_name=%s,  age_years=%s, weight_lb=%s, sex=%s, posted_date=%s, date_vaccinated=%s, date_neutered=%s, date_microchipped=%s, adopter_id=%s, date_adopted=%s WHERE dog_id =%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (dog_name, age_years, weight_lb, sex, posted_date, date_vaccinated, date_neutered, date_microchipped, adopter_id, date_adopted, dog_id))
            mysql.connection.commit()
            

            # redirect back to dogs page after we execute the update query
            return redirect("/dogs")


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=65329, debug=True)