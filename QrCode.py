import qrcode

#User Input For Qrcode
user_input = input("Enter You Data To Be Stored In Qrcode: ")

#data
dat = (user_input)

#File Name
file_name = 'qrcode.png'

#Saving Data In Qr Code
img = qrcode.make(data=user_input)

#Saving The Qrcode
img.save(file_name)