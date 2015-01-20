#!/usr/bin/python
# -*- coding:utf8 -*-
import app
import time
import curses
import json
import csv
import MySQLdb as mysql

HUBIC = '/Users/nicolas/hubiC/Documents/Contacts/'
CONTACTS = HUBIC+'google.csv'
FULL_CONTACTS = HUBIC+'google_full.csv'

fields = {}

#['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix',
#'Name Suffix','Initials', 'Nickname', 'Short Name', 'Maiden Name',
#'Birthday', 'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity', 'Priority', 'Subject', 'Notes', 'Group Membership',
#'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value', 'E-mail 3 - Type', 'E-mail 3 - Value', 'E-mail 4 - Type', 'E-mail 4 - Value', 'IM 1 - Type', 'IM 1 - Service', 'IM 1 - Value',
#'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type', 'Phone 2 - Value', 'Phone 3 - Type', 'Phone 3 - Value', 'Phone 4 - Type', 'Phone 4 - Value', 'Phone 5 - Type', 'Phone 5 - Value',
#'Address 1 - Type', 'Address 1 - Formatted', 'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box', 'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address',
#'Address 2 - Type', 'Address 2 - Formatted', 'Address 2 - Street', 'Address 2 - City', 'Address 2 - PO Box', 'Address 2 - Region', 'Address 2 - Postal Code', 'Address 2 - Country', 'Address 2 - Extended Address',
#'Organization 1 - Type', 'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title', 'Organization 1 - Department', 'Organization 1 - Symbol', 'Organization 1 - Location', 'Organization 1 - Job Description', 'Website 1 - Type','Website 1 - Value']

to_match = ['Title', 'First name', 'Last name',
               'Address 1 - Type', 'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box', 'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address',
               'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value', 'E-mail 3 - Type', 'E-mail 3 - Value', 'E-mail 4 - Type', 'E-mail 4 - Value']
matched = ['Gender', 'Given Name', 'Family Name',
           'Address 1 - Type', 'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box', 'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address',
           'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value', 'E-mail 3 - Type', 'E-mail 3 - Value', 'E-mail 4 - Type', 'E-mail 4 - Value']
matching = dict(zip(to_match, matched))
print matching

def get_matching(fields_names, row):
    result = [[],[],[]]
    k = 0
    for i in xrange(len(row)):
        if fields_names[i] in matched:
            result[2].append(row[i])
        elif len(row[i])>0:
            

def get_contact():
    with open(CONTACTS) as input_file:
        csv_reader = csv.reader(input_file, delimiter=',', quotechar='"')
        field_names = csv_reader.next()
        print field_names
        for row in csv_reader:
            print row
            yield [
                   
                   row,
                   [fields['Gender'], fields['Family Name'], fields['Given Name']]
                   ]

if __name__ == '__main__':
    for c in get_contact():
        print c
#     records = []
#     def pull():
#         return [['Prénom', 'Nom', 'Fils'], ['Nicolas', 'Grislain', 'Tancrède'], [0, 2, 1]]
#     def push(result):
#         records.append(result)
#     app.Validator(pull, push).start()
#     for rec in records:
#         print rec