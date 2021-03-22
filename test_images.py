import unittest
from images import *
import urllib.request
import pathlib

class Testimage(unittest.TestCase):
    global urls
    urls = ['https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png',
            'https://i.pinimg.com/originals/d9/7a/d7/d97ad7d1f3f486dc9309a87b0209538a.jpg',
            'https://i.pinimg.com/originals/a9/5d/6d/a95d6d7a0c60c18b0504c921939f6524.png',
            'https://kariselovuo.pro/ksprov1/wp-content/uploads/2018/02/css-logo-300x300.png',
            'https://www.djangoproject.com/m/img/logos/django-logo-negative.png',
            'https://medialibrarycdn.blueyonder.com/-/media/images/blue%20yonder/master/homepage/default%20opengraph%20image.png?rev=-1',
            'https://www.bradyplc.com/careers/&#8221']

    def test_list(self):
        a = open("links.txt", "r+")
        result = writetolist(a)
        self.assertEqual(result, urls)                                    # check for the list

    def test_url(self):
        for i in urls:
            try:
                result = ((urllib.request.urlopen(i).getcode()) == 200)    # check for url is found successfully
                self.assertEqual(result,True)
            except:
              print("urls is wrong for:" + str((urls.index(i))+1) +".jpg")

    def test_pics(self):
        for i in urls:
            file = pathlib.Path(str((urls.index(i)) + 1) + ".jpg")
            result = file.exists()
            try:
              self.assertEqual(result, True)
            except:
              print(str((urls.index(i)) + 1)+".jpg"+"not exists")

if __name__ == '__main__':
    unittest.main()