from bs4 import *
import requests 
from skimage import io
import pytesseract

baseURL= "https://www.mist.com/documentation/evpn-multihoming-deployment-via-mist-cloud/"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36', "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}

##sampleimage = requests.get(baseURL+"/documentation", headers = headers)

sampleimage = requests.get(baseURL, headers = headers)

#print(sampleimage.text)
pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'


soup = BeautifulSoup(sampleimage.text, "html.parser")

images = soup.findAll("img")
print(len(images))
##print(images)
for image in images:


    if "http" not in image["src"]:
        source = baseURL +image["src"]
    
    else:
        source = image["src"]

    source = source.replace(" ", "%20" )

    try: 
        print(image["src"])
        print(source)
        var = io.imread(source, headers = headers)
        text = pytesseract.image_to_string(var)
  
# Displaying the extracted text
        print(text[:-1])

    except FileNotFoundError:
        print("File not found")
        print(image["src"])
        print(source)
        var = io.imread(source)
        text = pytesseract.image_to_string(var)
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
    except KeyError:
        print("No source found")

    except ValueError:
        print("invalid url")

    except TypeError:
        print(image["src"])
        print(source)
        var = io.imread(source)
        text = pytesseract.image_to_string(var)
  
# Displaying the extracted text
        print(text[:-1])
    

