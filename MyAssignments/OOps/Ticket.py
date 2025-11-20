from datetime import datetime
import random
class TicketBooking:
    bookingnumber=0
    def __init__(self,loginUserName,password):
        self.username=loginUserName
        self.password=password
        self.is_logged_in = False
        TicketBooking.bookingnumber += 1
    def RegisterUserName(self,entered_username,entered_password):

        
    def LoginIsSuccess(self,entered_username,entered_password):
        is_logged_in = True
        with open("TicketBookingUserdetails.txt","r") as file:
                for line in file:
                    line=line.strip()
                    if not line:
                        continue
                    storedusername,storedpassword=line.split(':')
                    if storedusername==entered_username and storedpassword==entered_password:
                        self.is_logged_in = True
                        print (f"{storedusername} has successfully Logged in ")
                        return True
        else:
            self.is_logged_in = False
            print("Login Failed due to wrong userid or password")
            return False
    def bookTicket(self):
        if self.is_logged_in == True:
            today = datetime.now().strftime("%Y%m%d")  # 20251117
            self.booking_no = f"TICKET-{today}-{TicketBooking.bookingnumber:04d}"
            with open("user.txt","a")
            print(f"Ticket has booked for the user {self.username} and ticket booking number is {self.booking_no}")
            
        else:
            print("Ticket cannot be booked,please Login")
    def CancelTicket(self,ticketbookingnumber):
        booking = []
        found = False
        with open("TicketBookingUserdetails","a") as file:
            for line in file:
                line= line.strip()
                if not line:
                    continue
                user,bookingnum = line.split(",")
                if (user== self.username and bookingnum=ticketbookingnumber):
                    found = True
                    print{"Cancelled : {ticketbookingnumber}

        print("TicketBooking number is cancelled")


user1 = TicketBooking("ResmyPushpam","Success123") 
print(user1.LoginIsSuccess("ResmyPushpam", "Success123"))
user1.bookTicket()
user1.bookTicket()

# print(user1.bookTicket())
# bookTicket

             


    

