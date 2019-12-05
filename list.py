#!/usr/bin/python3

import email
from imapclient import IMAPClient
import os

def print_folder_and_emails(server):

    folders_on_server = server.list_folders()

    for folder in folders_on_server:
        flags = folder[0]

        # figure out whether the folder can be selected
        # i.e. does it "have emails" or "more than one folder"?
        can_select = True

        for flag in flags:
            if flag == b'\\Noselect' :
                can_select = False

        folder_name = folder[2]

        if can_select :
            print(f'Working on folder: {folder_name}:', end=" ")
            result = server.select_folder(folder_name, readonly=True)
            print(result[b'EXISTS'])
        else:
            print(f'Skipping {folder_name}, noselect')

first_email_password = os.environ['GMAIL_FIRST_PASSWORD']
first_email_user = os.environ['GMAIL_FIRST_USER']

first_email_server = IMAPClient('imap.gmail.com', use_uid=True)
first_email_server.login(first_email_user, first_email_password)

print_folder_and_emails(first_email_server)

print("---------")

second_email_password = os.environ['GMAIL_SECOND_PASSWORD']
second_email_user = os.environ['GMAIL_SECOND_USER']

second_email_server = IMAPClient('imap.gmail.com', use_uid=True)
second_email_server.login(second_email_user, second_email_password)

print_folder_and_emails(second_email_server)


raise SystemExit
