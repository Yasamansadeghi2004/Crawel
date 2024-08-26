# yasaman sadeghi

import requests
from bs4 import BeautifulSoup

#  HTTP web
url = 'https://codeyad.com/'
response = requests.get(url)

#  HTML reg
soup = BeautifulSoup(response.content, 'html.parser')

#link
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

#courses
courses = soup.find_all('div', class_='course-wrapper mt-4 flex gap-[18px] xl:gap-[15px] md:!gap-3 flex-wrap md:justify-between')
for course in courses:
    courses1 = soup.find_all('div', class_='course-card flex flex-col gap-2 w-[24%] lg:!w-[31.6%]')
    for cours in courses1:
        title = cours.find('a', class_='course-title hover:!text-blue')
        price = cours.find('p', class_='text-blue font-[500] text-[15px]')
        if title and price:
            title_text = title.get_text(strip=True)
            price_text = price.get_text(strip=True)
            if title_text and price_text:
                print(f"{title}: {price}")


#master
masters = soup.find_all('div', class_='teacher-card flex w-[22%] justify-center items-center flex-col bg-surface sm:w-full')
for teacher in masters:
    name = teacher.find('p', class_='text-black text-h7 font-bold mt-1')
    print(name)
    if name:
        name_text = name.get_text(strip=True)
        if name_text:
            print(name_text)


            #saved notpad
            with open('output,txt', 'w', encoding='utf-8')as file:
                for item in courses:
                    file.write(item.get('utf-8') + '\n')


















