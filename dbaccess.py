import psycopg
from psycopg import Error as psycopgError

class DBAccess:
    conn = None
    cur = None

    def __init__(self):
        print("Connecting to PostgreSQL")
        try:
            self.conn = psycopg.connect("dbname='projdb' user='postgres' host='ec2-54-237-205-175.compute-1.amazonaws.com' password='FSd0\\0*K<PTNEwhg^SUaM6&6' port='5433'")
            #self.conn = psycopg2.connect(host="54.237.205.175", database="testdb", user="postgres", password="FSd0\\0*K<PTNEwhg^SUaM6&6")
            self.cur = self.conn.cursor()
            print("Connected to PostgreSQL")
        except (Exception, psycopgError) as error:
            print("Error while connecting to PostgreSQL:", error)

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
    
    def getCustomer(self, customerID):
        self.cur.execute("SELECT * FROM Customers WHERE customerID = %s;", (customerID,))
        result = self.cur.fetchall()
        return result

    def addCustomer(self, customerID, firstName, lastName, email, phone):
        self.cur.execute("INSERT INTO Customers (customerID, firstName, lastName, email, phone) VALUES (%s, %s, %s, %s, %s);", (customerID, firstName, lastName, email, phone))
        self.conn.commit()
        return True

    def updateCustomer(self, customerID, firstName, lastName, email, phone):
        self.cur.execute("UPDATE Customers SET firstName = %s, lastName = %s, email = %s, phone = %s WHERE customerID = %s;", (firstName, lastName, email, phone, customerID))
        self.conn.commit()
        return True

    def deleteCustomer(self, customerID):
        self.cur.execute("DELETE FROM Customers WHERE customerID = %s;", (customerID,))
        self.conn.commit()
        return True

    def getReservations(self, customerID):
        self.cur.execute("SELECT * FROM Reservations;")
        result = self.cur.fetchall()
        return result

    def getReservation(self, reservationID):
        self.cur.execute("SELECT * FROM Reservations WHERE reservationID = %s;", (reservationID,))
        result = self.cur.fetchall()
        return result

    def addReservation(self, customerID, vehicleID, startDate, endDate):
        self.cur.execute("INSERT INTO Reservations (customerID, vehicleID, startDate, endDate) VALUES (%s, %s, %s, %s);", (customerID, vehicleID, startDate, endDate))
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

    def addVehicle(self, vehicleID, make, model, year, color, mileage, price, status):
        self.cur.execute("INSERT INTO Vehicles (vehicleID, make, model, year, color, mileage, price, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (vehicleID, make, model, year, color, mileage, price, status))
        self.conn.commit()
        return True

    def deleteVehicle(self, vehicleID):
        self.cur.execute("DELETE FROM Vehicles WHERE vehicleID = %s;", (vehicleID,))
        self.conn.commit()
        return True

    def updateVehicle(self, vehicleID, make, model, year, color, mileage, price, status):
        self.cur.execute("UPDATE Vehicles SET make = %s, model = %s, year = %s, color = %s, mileage = %s, price = %s, status = %s WHERE vehicleID = %s;", (make, model, year, color, mileage, price, status, vehicleID))
        self.conn.commit()
        return True
