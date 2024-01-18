import random
import string
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def PIN4_creat():
    # Ģenerē četrzīmju PIN kodu
    PIN4 = random.randint(1,9999)
    return str(PIN4).zfill(4)

def PIN5_creat():
    # Ģenerē pieczīmju PIN kodu
    PIN5 = random.randint(1,99999)
    return str(PIN5).zfill(5)

def Password_creat():
    # Jautā lietotājam, vai nepieciešama punktuācija parolē
    print("Include punctuation? (Y/N)")
    include_punctuation = input().upper() == "Y"
    # Jautā paroles garumu un pārbauda, vai ievadītais skaitlis ir pozitīvs
    while True:
        try:
            print("Password length ?")
            length = int(input())
            if length> 0 :
                break
            else: 
                print("Please enter a positive number.") 
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Izvēlas rakstzīmes paroles ģenerēšanai
    if include_punctuation:
        char = string.ascii_letters + string.digits + string.punctuation*2
    else:
        char = string.ascii_letters + string.digits
    # Ģenerē paroli
    password = ''
    for i in range(length):
        password += random.choice(char)
    return password

def switch_choise(choise):
    # Pārvērš lietotāja izvēli par skaitli
    choise = int(choise)
    # Iegūst funkciju no vārdnīcas, izmantojot lietotāja izvēli kā atslēgu
    func = switch_dict.get(choise)
    # Pārbauda, vai funkcija eksistē un izsauc to
    if func:
        return func()
    else:
    # Izvada kļūdas ziņojumu, ja lietotāja izvēle nav derīga
        print("Invalid choice")
        return None

def Cheсk_password():
    # Pārbauda paroļu stiprumu izmantojot "passwordmonster.com"
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    url = "https://www.passwordmonster.com"
    driver.get(url)
    time.sleep(2)
    # Atrod ievades lauku paroles stipruma pārbaudei
    find = driver.find_element(By.ID, "lgd_out_pg_pass")
    try:
        # Atver teksta failu lasīšanai un rakstīšanai
        with open('passwords.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate(0)
            for line in lines:
                # Izdala paroli no pārējās teksta rindas
                password = line.split()[0]
                # Pārbauda, vai rindā ir vairāk nekā viens elements
                if len(line.split()) > 1:
                    file.write(line)
                    continue
                # Ievada paroli pārbaudes vietnē un gaida rezultātu
                find.send_keys(password)
                time.sleep(1)
                result = driver.find_element(By.ID, "complexity-span")
                find.clear()
                # Saglabā pārbaudītās paroles un to stiprumu failā
                file.write(password + " "+ result.text + '\n')
        print("File has been checked")
        driver.quit()
    except:
        # Izvada kļūdas ziņojumu, ja nav atrasts paroļu fails
        print("There is no password file")

 # Izveido funkciju vārdnīcu      
switch_dict = {
    1:PIN4_creat,
    2:PIN5_creat,
    3:Password_creat,
    4:Cheсk_password,
}
# Lietotāja izvēles dialoga sākums
print("Choose the option: ")
print("Create a four-digit pin code - 1")
print("Create a five-digit pin code - 2")
print("Create password from letters and numbers - 3  ")
print("Want to check the strength of the passwords on file - 4")
print()
# Iegūst lietotāja izvēli
choise = input()
# Izsaukums funkcijai, kas ģenerē paroli atkarībā no lietotāja izvēles
generated_password = switch_choise(choise)
if type(generated_password) != str:
    # Ja netika ģenerēta parole, izvada ziņojumu un aicina atkārtot programmu
    print("No password generated")
    print("Rerun the program")
else:
    # Izvada ģenerēto paroli
    print("Generated Password:", generated_password)
    print("If you want to save your generated password in a txt file, press (Y/N)")
    writing = input().upper() == "Y"
    if writing:
        # Saglabā paroli failā "passwords.txt"
        with open ('passwords.txt', 'a') as file:
            file.write(generated_password + '\n')
            print("Password saved to passwords.txt")
