# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:05:42 2022

@author: User
"""

def get_lyrics(inp):
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    lyrics_text=[]
    strung_together=''.join(inp.split(' '))
    initial="https://www.google.com/search?q="
    str_=f"{initial}{strung_together}+lyrics&oq="
    
    driver.get(str_) 
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    lyrics_soup = soup.find_all('div', {'class': 'ujudUb'})
    for span_tags in lyrics_soup:
        span_content=soup.find_all('span', {'jsname': 'YS01Ge'})
        for embedded_lyrics in span_content:
            lyrics_text.append(embedded_lyrics.get_text())
    
    
    return lyrics_text


def ask_inp(inputfromuser):
    #song_inf=str(input("Enter artist name and song name space separated: "))    
    return get_lyrics(inputfromuser)

if __name__=='__main__':
    ask_inp()