# main.py
# Test file for the project

import dbaccess
#import psycopg2
from psycopg2 import Error as psycopgError

# Test the database connection
try:
    app = dbaccess.DBAccess()
    app.addVehicle( "Ford", "Fiesta", "2019", "Red", "19000", "25.25", "Economy", True, "Atlanta, GA")
    print(app.getVehicles())
    app.deleteVehicle(1)
    print(app.getVehicles())
    #db = conn = psycopg.connect("dbname='projdb' user='postgres' host='ec2-54-237-205-175.compute-1.amazonaws.com' password='FSd0\\0*K<PTNEwhg^SUaM6&6' port='5433'")
    #db = conn = psycopg2.connect(host="ec2-54-237-205-175.compute-1.amazonaws.com", database="projdb", user="postgres", password="FSd0\\0*K<PTNEwhg^SUaM6&6", port="5433")
except (Exception, psycopgError) as error:
    print("Error while connecting to PostgreSQL: ", error)