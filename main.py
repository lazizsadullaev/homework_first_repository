# class Person:
#     def __init__(self, name,  age):
#         self.__name = name
#         self.__age = age
#         self.display_info()
#
#     def display_info(self):
#         print(f'Имя : {self.__name}, возраст : {self.__age}')
#
# person1 = Person('Laziz', 15)
# person2 = Person('Kamol', 19)

#
# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#
#
# class SalaryCalculator:
#     def calculate(self, employee: Employee):
#         pass
#
#
# class EmployeeRepository:
#     def save_to_database(self, employee: Employee):
#         pass
#
#
# class ReportGeneration:
#     def generate_report(self, employee: Employee):
#         pass
#


import requests

from bs4 import BeautifulSoup

url = 'https://upl.uz/'

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

blocks_wrapper = soup.find('div', class_='main-story')

blocks_items = soup.find_all('div', class_='short-story')
#
# blocks_items = blocks_wrapper.find_all('h2', class_='sh-tit')
#
# for i in blocks_items:
#     print(i)
#
# print(len(blocks_items))
#
result = []
#
# for i in blocks_items:
#     result.append(i)

for block in blocks_items:
    name = block.find('h2', class_='sh-tit').get_text(strip=True)
    print(name)
    info = block.find('div', class_='sh-pan').get_text(strip=True)
    print(info)
    data = block.find('div', class_='sh-dat').get_text(strip=True)
    time = data.split(" ")
    for i in time:
        if ':' in i:
            print(i)
    comments = block.find('span', class_='icom').get_text(strip=True)
    print(comments)
    img_link = url + block.find('img').get('data-src')
    print(img_link)
    result.append({
        'name': name,
        'info': info,
        'time': time,
        'comments_count': comments,
        'img': img_link

    })

print(result)