# main.py
# Test file for the project

import dbaccess
#import psycopg2
from psycopg2 import Error as psycopgError

# Test the database connection
try:
    app = dbaccess.DBAccess()
    #app.addVehicle( "Ford", "Fiesta", "2019", "Red", "19000", "25.25", "Economy", True, "Atlanta, GA")
    #print(app.getVehicles())
    #app.deleteVehicle(3)
    #print(app.getVehicles())
    #app.addCustomer("John", "Doe", "john.doe@example.com", "478-123-4567", "123456")
    #print(app.getCustomers())
    #print(app.getCustomerByEmailAndHash("john.doe@example.com", "123456"))
    app.addReservation
except (Exception, psycopgError) as error:
    print("Error while connecting to PostgreSQL: ", error)