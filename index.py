import csv
import urllib.parse 

image_mapping = {
    ("Alex Nemecek", "2021"): "2334968.jpg",  
    ("Alex Nemecek", "2022"): "18820257.jpg",
    ("Alex Nemecek", "2023"): "18820260.jpg",
    ("Alex Nemecek", "2024"): "18820279.jpg",
}

csv_file = 'folder/athletes/mens_team/Alex Nemecek18820260.csv'
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

athlete_name = data[1][0] 
rows = ""

for athlete in data[1:]:
    if len(athlete) < 8:
        print(f"Skipping row {athlete} due to missing data.")
        continue

    athlete_overall_place = athlete[1]
    athlete_grade = athlete[2]
    athlete_time = athlete[3]
    
    athlete_date = athlete[4] if athlete[4] else "Date unavailable"
    athlete_meet = athlete[5] if athlete[5] else "Meet unavailable"
    athlete_comments = athlete[6] if athlete[6] else "No comments"
    
    athlete_photo = f'folder/images/AthleteImages/{image_mapping.get((athlete[0], athlete_overall_place), "default_photo.jpg")}'
    
    rows += f'''
    <tr>
        <td>{athlete_overall_place}</td>
        <td>{athlete_grade}</td>
        <td>{athlete_time}</td>
        <td>{athlete_date}</td>
        <td>{athlete_meet}</td>
        <td>{athlete_comments}</td>
        <td><img src="{athlete_photo}" alt="Photo of {athlete[0]}"></td>
    </tr>
    '''

with open('index.html', 'r', encoding='utf-8') as template_file:
    html_template = template_file.read()

html_filled = html_template.replace("{{name}}", athlete_name)
html_filled = html_template.replace("{{rows}}", rows)

with open('output.html', 'w', encoding='utf-8') as output_file:
    output_file.write(html_filled)

print("HTML file generated successfully!")
