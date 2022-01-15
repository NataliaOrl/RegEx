from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="UTF-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def get_contacts(contacts_list):
  contacts = []
  for el in contacts_list:
      if len(el[0].split()) == 3:
          lastname = el[0].split()[0]
          firstname = el[0].split()[1] 
          surname = el[0].split()[2]
      elif len(el[0].split()) == 2:
          lastname = el[0].split()[0]
          firstname = el[0].split()[1] 
          surname = el[1]  
      else:
          lastname = el[0].split()[0]
          firstname = el[1] if len(el[1].split()) == 1 else el[1].split()[0]
          surname = el[2] if len(el[1].split()) == 1 else el[1].split()[1]
      organization = el[3]
      position = el[4]
      email = el[6]
      if 'доб' in el[5]:
          phone = re.sub(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})\s*\(*доб\.*\s*(\d+)*\)*', r'+7(\2)\3-\4-\5 доб.\6', el[5])
      else:
          phone = re.sub(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', r'+7(\2)\3-\4-\5', el[5])
      if  firstname not in contacts and lastname not in contacts:
          contacts.extend([lastname, firstname, surname, organization, position, phone, email])
  return contacts

def get_list(contacts, column=7):
  col = column
  contacts_new = [contacts[x:col+x] for x in range(0,len(contacts),col)]
  return contacts_new


with open("phonebook_2.csv", "w", newline='', encoding="UTF-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(get_list(get_contacts(contacts_list), column=7))

