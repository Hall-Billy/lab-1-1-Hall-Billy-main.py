#!/usr/bin/env python3
# GitHub Lab 1: Creating a Class


# Create Contact Class
class Contact(object):
    pass
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.phone = ''
        self.addr_city  = ''
        self.addr_zip = ''
        self.email = ''
        self.addr_state = ''
        self.addr_street = ''

    def set_phone(self, Num):
        self.phone = Num
        
    def set_email(self, Mail):
        self.email = Mail
        
    def set_addr_zip(self, Zip):
        self.addr_zip = Zip

    def set_addr_street(self, street):
        self.addr_street = street
        
    def set_addr_state(self, state):
        self.addr_state = state

    def set_addr_city(self, city):
        self.addr_city = city

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email
    
    def get_addr_zip(self):
        return self.addr_zip

    def get_addr_street(self):
        return self.addr_street
    
    def get_addr_state(self):
        return self.addr_state
    
    def get_addr_city(self):
        return self.addr_city
    
    def calc_full_name(self):
        return f'{self.fname} {self.lname}'
    
    def calc_full_address(self):
        return f'{self.calc_full_name()}\n{self.addr_street}\n{self.addr_city}, {self.addr_state} {self.addr_zip}'
    
# Modify the main() function to work below 
def main():
    # User Input
    nm1 = input("First: ")
    nm2 = input("Last: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip Code: ")
    eml = input("Email: ")
    phone = input("Phone: ")
    
    # TO DO: Create Contact Object
    contact = Contact(nm1, nm2)

    # TO DO: Set Contact Attributes Using the Setter Methods
    contact.set_phone(phone)
    contact.set_addr_street(address)
    contact.set_addr_state(state)
    contact.set_addr_zip(zip_code)
    contact.set_addr_city(city)
    contact.set_email(eml)


    # TO DO: Display Contact Using the calculate full address
    print(contact.calc_full_address())
    print(f'Email: {contact.get_email()}')
    print(f'Phone: {contact.get_phone()}')
    

# DO NOT MODIFY BELOW
if __name__ == "__main__":
    # Call Main Program
    main()
''''
Questions:

1: By following your instructions and using the previous labs and participation assignments as models I assumed I'd have to set the var's to nothing. (hopefully this is what you're asking)
2: It allows for easier understanding of the code when a problem occurs.
3: I believe the code would still be able to run.
4: If the methods were private the code would not work unless .

''''
