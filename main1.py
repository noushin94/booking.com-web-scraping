from bs4 import BeautifulSoup

# Initialize variables
l = []
g = []
o = {}
k = {}
fac = []
fac_arr = []

# Load the provided HTML file
file_path = 'The Lenox, Boston (updated prices 2024).html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract hotel name, address, and rating
o["name"] = soup.find("h2", {"class": "pp-header__title"}).text if soup.find("h2", {"class": "pp-header__title"}) else 'N/A'
o["address"] = soup.find("span", {"class": "hp_address_subtitle"}).text.strip("\n") if soup.find("span", {"class": "hp_address_subtitle"}) else 'N/A'
o["rating"] = soup.find("div", {"class": "d10a6220b4"}).text if soup.find("div", {"class": "d10a6220b4"}) else 'N/A'

# Extract important facilities
fac = soup.find_all("div", {"class": "important_facility"})
for i in range(len(fac)):
    fac_arr.append(fac[i].text.strip("\n"))

# Extract data-block-ids
ids = []
tr = soup.find_all("tr")
for row in tr:
    id = row.get('data-block-id')
    if id:
        ids.append(id)

print("ids are ", len(ids))

# Extract room types and prices based on data-block-ids
for i in range(len(ids)):
    try:
        allData = soup.find("tr", {"data-block-id": ids[i]})
        if allData:
            # Extract room type
            room_types = allData.find_all("span", {"class": "hprt-roomtype-icon-link"})
            room_type_text = ' / '.join([room.text.replace("\n", "") for room in room_types])
            k["room"] = room_type_text if room_type_text else 'N/A'
            
            # Extract price
            price = allData.find("div", {"class": "bui-price-display__value"})
            k["price"] = price.text.replace("\n", "") if price else 'N/A'

            g.append(k)
            k = {}

    except Exception as e:
        k["room"] = None
        k["price"] = None
        g.append(k)
        k = {}

l.append(g)
l.append(o)
l.append(fac_arr)
print(l)
