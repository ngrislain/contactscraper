import csv
from curses import *
from MySQLdb import *

HUBIC = '/Users/nicolas/hubiC/Documents/Contacts/'
CONTACTS = HUBIC+'google.csv'
FULL_CONTACTS = HUBIC+'google_full.csv'

fields = {}

with open(CONTACTS) as input_file:
    csv_reader = csv.reader(input_file, delimiter=',', quotechar='"')
    field_names = csv_reader.next()
    for k in xrange(len(field_names)):
        fields[field_names[k]] = k
    print field_names
    csv_reader.next()
    csv_reader.next()
    csv_reader.next()
    print csv_reader.next()
    for row in csv_reader:
        print row[fields['Given Name']], row[fields['Family Name']], row[fields['Gender']]



class Contact(object):
    def __init__(self, row, fields):
        self.title = row[fields['Gender']]
