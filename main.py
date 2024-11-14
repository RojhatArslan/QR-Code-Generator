import qrcode

customer = input("please enter a url you would like to add")
img = qrcode.make(customer)
type(img)
img.save("some_file.png")

