import requests
import re
import html
import codecs
import json
from datetime import datetime

url_or_id = 'REDACTED'

SEEN_ID_HASH = {}
BIGHASH = {}

def grab_all_info_from_url(url_or_id):
  thishash = {}
  p = re.compile("https://drive.google.com/drive/folders/(.*)")
  m = p.match(url_or_id)
  if m:
      thisid = m.group(1)
  else:
      thisid = url_or_id
  if SEEN_ID_HASH.get(thisid) == 1:
    print("Already seen this...")
    return
  else:
    thisurl = 'https://drive.google.com/drive/folders/' + thisid
    SEEN_ID_HASH[thisid] = 1
  try:
    print('trying url ' + thisurl)
    txt = requests.get(thisurl).text
    x = re.findall(r"window\['_DRIVE_ivd'\]\s*=\s*'(.*?)';if[^<]*</script>", txt)
    for match in x:
      escaped_data = match.replace("\u2018", "'").replace("\u2019", "'").replace("\u0300", "e").replace("\u0308", "e").replace("\u2013", "-").replace("\u0410", "A")
      blah = escaped_data.encode().decode('unicode_escape')
      bigdumblist = json.loads(blah)
      #print(json.dumps(bigdumblist))
  except:
    print("welp...moving on...")
    return

  try:
    shared_folder_list = bigdumblist[0]

    for shared_folder in shared_folder_list:
      item_id = shared_folder[0]
      item_name = shared_folder[2]
      item_type = shared_folder[3]
      print('***********')
      if item_type == 'application/vnd.google-apps.shortcut':
          item_category = 'SHORTCUT'
          timestamp = shared_folder[9]
          dt_obj = datetime.fromtimestamp(int(timestamp/1000)).strftime('%Y-%m-%d')
          item_link = 'https://drive.google.com/drive/folders/' + item_id
          thishash['item_category'] = item_category
          thishash['item_id'] = item_id
          thishash['item_name'] = item_name
          thishash['item_link'] = item_link
          thishash['dt_obj'] = dt_obj
          print(item_category)
          print(item_id)
          print(item_name)
          print(item_link)
          print(dt_obj)
          grab_all_info_from_url(item_link)
      elif item_type == 'application/vnd.google-apps.folder':
          item_category = 'FOLDER'
          timestamp = shared_folder[9]
          dt_obj = datetime.fromtimestamp(int(timestamp/1000)).strftime('%Y-%m-%d')
          item_link = 'https://drive.google.com/drive/folders/' + item_id
          thishash['item_category'] = item_category
          thishash['item_id'] = item_id
          thishash['item_name'] = item_name
          thishash['item_link'] = item_link
          thishash['dt_obj'] = dt_obj
          thishash['item_category'] = item_category
          thishash['item_id'] = item_id
          thishash['item_name'] = item_name
          thishash['item_link'] = item_link
          thishash['dt_obj'] = dt_obj
          print(item_category)
          print(item_id)
          print(item_name)
          print(item_link)
          print(dt_obj)
          grab_all_info_from_url(item_link)
      else:
          item_category = 'FILE'
          timestamp = shared_folder[9]
          dt_obj = datetime.fromtimestamp(int(timestamp/1000)).strftime('%Y-%m-%d')
          item_link = 'https://drive.google.com/file/d/' + item_id
          thishash['item_category'] = item_category
          thishash['item_id'] = item_id
          thishash['item_name'] = item_name
          thishash['item_link'] = item_link
          thishash['dt_obj'] = dt_obj
          print(item_category)
          print(item_id)
          print(item_name)
          print(dt_obj)
          print(item_link + '  !!!!!!!!!!!!!')
      print('***********')
      BIGHASH[thisid] = thishash
  except:
    print("welp...moving on2...")
    return

grab_all_info_from_url(url_or_id)
final_file = open('all_craptoo.json','w')
final_file.write(json.dumps(BIGHASH))
final_file.close()

