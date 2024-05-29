book={}
book["toom"] = {
    "name":"tom",
    "addres":"sheikhupura",
    "phone":123324424
}
book["fareed"] = {
    "name":"fareed",
    "address":"lahore",
    "phone":24224242
}
import json
s = json.dumps(book)
with open("c://book.txt","w") as f:
    f.write(s)
