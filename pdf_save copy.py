from selenium import webdriver
import os 
import urllib.request
import img2pdf

PATH="D:\Downloads\chromedriver_win32\chromedriver.exe"

s=input("Name of the Comic Series you want : ")
c=-1
while c not in [0,1,2]:
    print("Enter 1 for High Quality print")
    print("Enter 2 for Low Quality print")
    print("Enter 0 to exit")
    c=int(input())

if c!=0:
    try:
        os.mkdir('Downloads/'+s)
    except:
        pass

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--log-level=3")

    issue=13
    name=s.split()
    path='https://readcomiconline.li/Comic/'+'-'.join(name)+'/Issue-'+str(issue)+'?readType=1'
 #   path='https://readcomiconline.li/Comic/'+'-'.join(name)+'/Full'+'?readType=1'
  
    if c==1:
        path+='&quality=hq'
    driver = webdriver.Chrome(PATH,chrome_options=chrome_options)
    driver.get(path)
    end=False
    while end==False:
        os.chdir('D:/Downloads/comic_Downloader/')
        imgs=driver.find_elements_by_xpath("//div[@id='divImage']/p/img")
        os.mkdir('Downloads/'+s+'/'+str(issue))
        pgno=1
        for img in imgs:
            url = img.get_attribute("src")
            urllib.request.urlretrieve(url, 'Downloads/'+s+'/'+str(issue)+'/'+str('{:02}'.format(pgno))+'.jpg')
            pgno+=1
        try:
            button=driver.find_elements_by_class_name('btnNext')
            button[1].click()
        except:
            end=True
        path='D:/Downloads/comic_Downloader/Downloads/'+s+'/'+str(issue)+'/'
        os.chdir(path)
        with open('D:/Downloads/comic_Downloader/Downloads/'+s+'/'+str(issue)+'.pdf', "wb") as f:
            f.write(img2pdf.convert([i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]))
        issue+=1
