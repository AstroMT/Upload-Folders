# Project 101

import os, dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    self.dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.BjQKb53QcrvXgAhsBG6w8iZotsbSIJSXtbPwGXjl7E0_GgByOSBHmQYMBVE7RvemIwYpq6zQHkzTn4XauerkxQ0bd-orcMb-0RD3RsxPzqbtQwZDo5_jAhpfTAUf95C58IuwI9muk8yj" 
    transferData = TransferData(access_token)

    file_from = input("Enter the full path of the directory to upload: ")
    file_to = input("Enter the full path in Dropbox to upload the files to: ")

    transferData.upload_file(file_from, file_to)
    print("Files uploaded successfully!")
