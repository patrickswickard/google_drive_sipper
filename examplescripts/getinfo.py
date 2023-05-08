import httplib2
import pprint
import sys
from apiclient.discovery import build

# see https://developers.google.com/drive/api/reference/rest/v2/files/list

def printChildren(parent):
  param = {"q": "'" + parent + "' in parents and mimeType != 'application/vnd.google-apps.folder'"}
  result = service.files().list(**param).execute()
  files = result.get('files')

  for afile in files:
    print('File {}'.format(afile.get('name')))
    print('File {}'.format(afile.get('id')))
    print('File {}'.format(afile.get('kind')))
    print('File {}'.format(afile))

API_KEY = 'CHANGEME' # get from API->Credentials page in console.cloud.googl.com
FOLDER_ID = 'CHANGEME' # NOTE: folder must be publicly visible when using an API key.
service = build('drive', 'v3', developerKey=API_KEY)
printChildren(FOLDER_ID)
