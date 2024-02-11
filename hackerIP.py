import requests
from bs4 import BeautifulSoup

url = 'https://sites.google.com/site/iplistforhe/ip-database'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
hacker_list = list(soup.find_all('div', dir='ltr')[5].stripped_strings)[1:]

for hacker_ip in hacker_list:
    print(hacker_ip)
    
# 현재 디렉토리에 1.txt 파일 만들어서 쓰고 저장.
with open('hackerIP.txt', 'w') as file:
    for hacker_ip in hacker_list:
         file.write(str(hacker_ip) + "\n") 
         
def fileopen(data):
    
    #파일 불러오기 
    with open(data, 'r', encoding='UTF8') as file:
        
        text = file.read()
        
        splitdata = text.split()
        
        #리스트의 중첩된 부분 삭제하기 
        splitdata = list(dict.fromkeys(splitdata))
 
    return splitdata
 
 
if __name__ == '__main__':
 
    #파일1번 불러오기
    NewList = fileopen('foreigncountryIP.txt')
    
    #파일2번 불러오기
    NewList1 = fileopen('hackerIP.txt')
    
    
    
 
    dif1 = list(set(NewList1) - set(NewList))
    dif2 = list(set(NewList) - set(NewList1))
    
    # 두 파일중 공통된 요소 출력 
    print('hacker', list((set(NewList)-set(dif1))-set(dif2)))