import psycopg2
from psycopg2 import Error as psycopgError

class DBAccess():
    conn = None
    cur = None

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(DBAccess, self).__new__(self)

            print("Connecting to PostgreSQL")
            try:
                self.conn = psycopg2.connect(
                    host="ls-49d6abcc0497d5fab44b0cc9d8a9b96ccb8d378b.coequzq2kddp.us-east-1.rds.amazonaws.com", 
                    database="projdb", 
                    user="projectadmin", 
                    password="FSd0\\\\0*K<PTNEwhg^SUaM6&6",
                    port="5432"
                    )
                self.cur = self.conn.cursor()
                print("Connected to PostgreSQL")
            except (Exception, psycopgError) as error:
                print("Error while connecting to PostgreSQL:", error)
        return self.instance

    def __del__(self):
        print("Closing PostgreSQL connection")
        if self.conn:
            self.cur.close()
            self.conn.close()
            print("PostgreSQL connection is closed")
    
    def getCustomers(self):
        self.cur.execute("SELECT * FROM Customers;")
        result = self.cur.fetchall()
        return result

    def getCustomerByEmailAndHash(self, email, pwhash):
        self.cur.execute("SELECT * FROM Customers WHERE email = %s AND pwhash = %s;", (email, pwhash))
        result = self.cur.fetchall()
        return result
    
    def getCustomer(self, customerID):
        self.cur.execute("SELECT * FROM Customers WHERE customerID = %s;", (customerID,))
        result = self.cur.fetchall()
        return result

    def addCustomer(self, firstName, lastName, email, phone, pwhash):
        self.cur.execute("INSERT INTO Customers (firstName, lastName, email, phone, pwhash) VALUES (%s, %s, %s, %s, %s);", (firstName, lastName, email, phone, pwhash))
        self.conn.commit()
        return True

    def updateCustomer(self, customerID, firstName, lastName, email, phone, pwhash):
        self.cur.execute("UPDATE Customers SET firstName = %s, lastName = %s, email = %s, phone = %s, pwhash = %s WHERE customerID = %s;", (firstName, lastName, email, phone, customerID))
        self.conn.commit()
        return True

    def deleteCustomer(self, customerID):
        self.cur.execute("DELETE FROM Customers WHERE customerID = %s;", (customerID,))
        self.conn.commit()
        return True

    def getReservations(self):
        self.cur.execute("SELECT * FROM Reservations;")
        result = self.cur.fetchall()
        return result

    def getReservation(self, reservationID):
        self.cur.execute("SELECT * FROM Reservations WHERE reservationID = %s;", (reservationID,))
        result = self.cur.fetchall()
        return result

    def getReservationsByClient(self, customerID):
        self.cur.execute("SELECT * FROM Reservations WHERE customerID = %s;", (customerID,))
        result = self.cur.fetchall()
        return result
    
    def addReservation(self, customerID, vehicleID, pickupLocation, dropoffLocation, timeOfPickup, startDate, endDate, invoiceAmount):
        self.cur.execute("INSERT INTO Reservations (customerID, vehicleID, pickupLocation, dropoffLocation, timeOfPickup, startDate, endDate, invoiceAmount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (customerID, vehicleID, pickupLocation, dropoffLocation, timeOfPickup, startDate, endDate, invoiceAmount,))
        self.conn.commit()
        return True

    def updateReservation(self, reservationID, customerID, vehicleID, startDate, endDate):
        self.cur.execute("UPDATE Reservations SET customerID = %s, vehicleID = %s, startDate = %s, endDate = %s WHERE reservationID = %s;", (customerID, vehicleID, startDate, endDate, reservationID))
        self.conn.commit()
        return True
    
    def deleteReservation(self, reservationID):
        self.cur.execute("DELETE FROM Reservations WHERE reservationID = %s;", (reservationID,))
        self.conn.commit()
        return True
    
    def getVehicles(self):
        self.cur.execute("SELECT * FROM Vehicles;")
        result = self.cur.fetchall()
        return result

    def getVehicle(self, vehicleID):    
        self.cur.execute("SELECT * FROM Vehicles WHERE vehicleID = %s;", (vehicleID,))
        result = self.cur.fetchall()
        return result

    def addVehicle(self, make, model, year, color, mileage, price, priceClass, available, location):
        self.cur.execute("INSERT INTO Vehicles (make, model, year, color, mileage, price, priceclass, available, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (make, model, year, color, mileage, price, priceClass, available, location))
        self.conn.commit()
        return True

    def deleteVehicle(self, vehicleID):
        self.cur.execute("DELETE FROM Vehicles WHERE vehicleID = %s;", (vehicleID,))
        self.conn.commit()
        return True

    def updateVehicle(self, vehicleID, make, model, year, color, mileage, price, priceClass, available, location):
        self.cur.execute("UPDATE Vehicles SET make = %s, model = %s, year = %s, color = %s, mileage = %s, price = %s, priceClass = %s, available = %s, location = %s WHERE vehicleID = %s;", (make, model, year, color, mileage, price, priceClass, available, location,  vehicleID))
        self.conn.commit()
        return True