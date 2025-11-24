p1 = "Make a lot"
p2 = "Click it"
p3 = "Subscribe"
p4 = "Bank Account"

message = input("Enter your message:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is spam. Your message:" , message)

else:
    print("This message is not spam Your message:" , message) 


