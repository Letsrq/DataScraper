import os
import requests


from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm 

url = "https://xkcd.com/"

output_dir = "xkcd_comics"
os.makedirs(output_dir, exist_ok=True)

toplamcr = 4

# bar yapan edevat \/
with tqdm(total=toplamcr, desc=".....INDIRILIYOR.....") as pbar:

    for comicsayi in range(1, toplamcr + 1): #<- 1 100 
            
            comic_url = urljoin(url, str(comicsayi))

            response = requests.get(comic_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            img_element = soup.find("div", id="comic").find("img")
            if img_element:
                img_src = img_element["src"]

                img_response = requests.get(urljoin(url, img_src))
                img_response.raise_for_status()

                img_filename = f"numara_{comicsayi}.png"
                img_path = os.path.join(output_dir, img_filename)

                with open(img_path, "wb") as img_file:
                    img_file.write(img_response.content)
                pbar.update(1)
            else:
                print("hata")
print("done.")
