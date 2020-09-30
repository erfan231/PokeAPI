import urllib
import json
from urllib.request import urlopen

site = "https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0"


user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"

headers = {"User-Agent":user_agent}

request=urllib.request.Request(site,None,headers) 
response = urllib.request.urlopen(request)
datas = json.load(response) 

#if you iterate through a list it starts from 0, blocks user from using index 0
data_list = ['o']

for data in datas["results"]:
    data_list.append(data["name"])


#print("Welcome to PokeAPI")
#print("enter 0 for exit")
if __name__ == "__main__":
    while True:
        try:
            ask = int(input("Enter an ID: "))
            if ask == 0:
                print("Exiting...")
                break
            else:
                name = (data_list[ask])
                img_id = str(ask)
                link = (f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{img_id}.png")
                print(f"Name: {data_list[ask]}|\t Source Img: {link}")
        except TypeError:
            print("Please enter an ID (Digit)")
        except ValueError:
            print("Please enter an ID (Digit)")
        except urllib.error.HTTPError:
            print("Site broken:( \n Error: {}".format(urllib.error.HTTPError))
            break
else:
    pass