
import SSE.dbaccess as dbaccess

class CarRental:
    db = None

    def __init__(self):
        self.db = dbaccess.DBAccess()

    def __del__(self):
        self.db.__del__()

    def getReservations(self):
        return self.db.getReservations()

    def getReservation(self, id):
        return self.db.getReservation(id)

    def addReservation(self, reservation):
        return self.db.addReservation(reservation)

    def updateReservation(self, id, reservation):
        return self.db.updateReservation(id, reservation)

    def deleteReservation(self, id):
        return self.db.deleteReservation(id)

    def getVehicles(self):
        return self.db.getVehicles()

    def getVehicle(self, id):
        return self.db.getVehicle(id)

    def addVehicle(self, vehicle):
        return self.db.addVehicle(vehicle)

    def updateVehicle(self, id, vehicle):
        return self.db.updateVehicle(id, vehicle)

    def deleteVehicle(self, id):
        return self.db.deleteVehicle(id)

    def getClients(self):
        return self.db.getCustomers()
    
    def getClient(self, id):
        return self.db.getCustomer(id)
    
    def addClient(self, client):
        return self.db.addCustomer(client)

    def updateClient(self, id, client):
        return self.db.updateCustomer(id, client)

    def deleteClient(self, id):
        return self.db.deleteCustomer(id)

    def getReservationsByClient(self, id):
        return self.db.getReservationsByClient(id)