def writetolist(f):
  '''adding links in the file to a list'''
  my_list = f.read().splitlines()
  f.close()
  return my_list

def save_image(image_list):
  '''setting filename'''
  import urllib.request
  urllib.error.HTTPError
  for i in image_list:
    filename: str = str((image_list.index(i))+1) +".jpg"
    try:
        # using urlretrieve to download the image
        urllib.request.urlretrieve(i, filename)
        print('Image sucessfully Downloaded:', filename)
    except urllib.error.HTTPError as err:
      print('error is:', err.code, '.so, Image Could not be retrieved', filename)

def main():
  f = open("links.txt", "r+")
  image_list = writetolist(f)
  save_image(image_list)

if __name__ == '__main__':
  main()