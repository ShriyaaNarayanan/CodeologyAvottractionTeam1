from bs4 import BeautifulSoup
import requests
import csv
import re
main_url = "https://www.wikihow.com/Rizz-Lines"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')
ret = ""
steps_section = soup.find_all('ol', class_='steps_list_2')
pickup_lines = set()
for step in steps_section:
    li_items = step.find_all('li')
    for li in li_items:
        # Look for an <i> tag inside the <li>
        italic = li.find('i')
        if italic:
            # Get the text inside the <i> tag
            line = italic.get_text(strip=True)
            pickup_lines.add(line)

    # Step 4: Print the pickup lines
for line in pickup_lines:
    print(line)
print(len(pickup_lines))
with open('pick_up_lines_0.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header (optional)
        writer.writerow(['Unique List Item'])
        
        # Write each item from the set as a new row
        for item in pickup_lines:
            writer.writerow([item])

