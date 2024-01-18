# Nosleguma projekts
## Password Generator and Strength Checker
### Apraksts

Šis projekts ietver programmu paroļu ģenerēšanai un to stipruma pārbaudei. Programma ļauj izveidot gan vienkāršus PIN kodus, gan sarežģītas paroles ar iespēju iekļaut īpašās zīmes, jo ne visas vietnes pieprasa, lai parolēs būtu pieturzīmes. Izveidotās paroles programma ieraksta failā passwords.txt. Turklāt programma var pārbaudīt teksta failā saglabāto paroļu stiprumu, izmantojot tīmekļa pakalpojumu
### Izmantotās bibliotēkas 
+ random
   Šis modulis tiek izmantots skaitļu ģenerēšanai Python. Tas piedāvā dažādas funkcijas, lai veiktu tādus uzdevumus kā nejaušu skaitļu ģenerēšana, nejaušu elementu atlase no saraksta, nejauša elementu sajaukšana u. c. Skripta gadījumā tas galvenokārt tiek izmantots, lai ģenerētu nejaušus PIN kodus un atlasītu nejaušas rakstzīmes, veidojot paroles.
+ string
   Modulī ir vairākas noderīgas konstantes, klases un vairākas funkcijas standarta Python virkņu apstrādei. Es to izmantojat savā skripta programmā, lai piekļūtu rakstzīmju kolekcijām, piemēram, string.ascii_letters (mazo un lielo burtu saraksts), string.digits (visi skaitļi 0-9) un string.punctuation (visas pieturzīmes piemēram: ./!@#$%^&), kas ir noderīgas, veidojot rakstzīmju kopas paroles ģenerēšanai.
+ selenium
  Spēcīgs rīks, kas ļauj kontrolēt tīmekļa pārlūkprogrammas, izmantojot programmas, un veikt pārlūkprogrammu automatizāciju. To plaši izmanto tīmekļa lietojumprogrammu automatizācijai testēšanas nolūkos, taču tas spēj veikt arī jebkuru uzdevumu, ko pārlūkprogrammā var veikt manuāli. Skripta gadījumā Selenium tiek izmantots, lai automatizētu paroles stipruma pārbaudes procesu tīmekļa vietnē. 
  Tika izmantotas arī Selenium bibliotēkas apakšbibliotēkas (webdriver, Service and ChromeOptions un By)
  Webdriver ir Selenium daļa, ko izmanto tīmekļa lietojumprogrammu testēšanas automatizēšanai. Tā nodrošina iespēju palaist un mijiedarboties ar dažādām tīmekļa pārlūkprogrammām, piemēram, Chrome, Firefox u. c. Lai mijiedarbotos ar pārlūkprogrammu Chrome, izmantojiet webdriver.Chrome.
  Service un ChromeOptions: Tos izmanto, lai iestatītu Chrome WebDriver ar īpašām konfigurācijām.
  By ir Selenium nodrošināta klase, lai atrastu elementus lapā. Piemēram, By.ID ļauj atrast elementus pēc to ID.
+ time
  Šis modulis nodrošina dažādas ar laiku saistītas funkcijas. Skripta izpildē izmantojiet time.sleep(), lai apturētu skripta izpildi uz noteiktu sekunžu skaitu. Tas ir īpaši noderīgi, kad, izmantojot Selenium, mijiedarbojas ar tīmekļa lapām, dodot laiku, lai lapas ielādētos vai elementi kļūtu pieejami.
  
### Funkcijas
+ Četrciparu PIN kodu ģenerēšana
+ Piecciparu PIN kodu ģenerēšana
+ Paroļu ģenerēšana ar iepriekš iestatītu garumu un iespēju iekļaut īpašās rakstzīmes
+ Paroles stipruma pārbaude no faila
+ Izvēles slēdzis (switch_choise), tā kā python nav switch funkcijas, tika nolemts uzrakstīt funkciju, kas izsauks funkcijas atkarībā no lietotāja izvēles. To pašu varētu izdarīt ar if. Šim nolūkam tika izveidota arī vārdnīca, kuras atslēgas ir lietotāja ievadītie cipari, bet vērtība ir funkcijas izsaukums.

### Prasības

Programmā ir nepieciešams:
+ Python 3.x
+ Selenium WebDriver
+ ChromeDriver (atbilstoši instalētajai Google Chrome versijai).

