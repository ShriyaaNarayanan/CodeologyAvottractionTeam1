from bs4 import BeautifulSoup
import requests
import re
import csv
main_url = "https://www.theknot.com/content/pick-up-lines"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')
ret = ""
figures = soup.find_all('figure', class_='xo-article-image-container')
pickup_lines = set()
for figure in figures:
    if figure:
        steps_section = figure.find_next_sibling('ul')
        if steps_section:
            li_items = steps_section.find_all('li')
            for li in li_items:
                text = li.get_text(strip=True)
                if '::marker' in text:
                    text = text.split('::marker', 1)[1].strip()
                text = text.strip('"').strip()
                pickup_lines.add(text)
for line in pickup_lines:
    print(line)
print(len(pickup_lines))
with open('pick_up_lines.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header (optional)
        writer.writerow(['Unique List Item'])
        
        # Write each item from the set as a new row
        for item in pickup_lines:
            writer.writerow([item])