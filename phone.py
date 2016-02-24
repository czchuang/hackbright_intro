import contacts_class

contact_courtney = contacts_class.Contact("Courtney", "Chuang")
contact_courtney.mobile_phone = "408-806-7903"
contact_courtney.email = "czchuang3@gmail.com"

contact_camila = contacts_class.Contact("Camila", "Toth")
contact_camila.mobile_phone = "415-425-2345"
contact_camila.email = "camilatoth@gmail.com"

contact_eli = contacts_class.Contact("Eli", "Haims")
contact_eli.mobile_phone = "818-782-1983"
contact_eli.email = "elihaims@gmail.com"

contacts_list = []
contacts_list.append(contact_courtney)
contacts_list.append(contact_camila)
contacts_list.append(contact_eli)

for contact in contacts_list:
	contact.send_email("Happy birthday!")
