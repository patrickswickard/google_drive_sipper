import httplib2
import pprint
import sys
from apiclient.discovery import build

def printChildren(parent):
  param = {"q": "'" + parent + "' in parents and mimeType != 'application/vnd.google-apps.folder'"}
  result = service.files().list(**param).execute()
  files = result.get('files')

  for afile in files:
    print('File {}'.format(afile.get('name')))
    print('File {}'.format(afile.get('id')))
    print('File {}'.format(afile.get('kind')))
    print('File {}'.format(afile))

API_KEY = 'AIzaSyCucOfLw-ATt1nTYx3ScX_tUevXm1whyDg' # get from API->Credentials page in console.cloud.googl.com
FOLDER_ID = '1J9alevdVDUAWaFsKbgdRcAX860FFjJ1b' # NOTE: folder must be publicly visible when using an API key.
service = build('drive', 'v3', developerKey=API_KEY)
printChildren(FOLDER_ID)
