# Nosleguma projekts
## Password Generator and Strength Checker
### Apraksts

Šis projekts ietver programmu paroļu ģenerēšanai un to stipruma pārbaudei. Programma ļauj izveidot gan vienkāršus PIN kodus, gan sarežģītas paroles ar iespēju iekļaut īpašās zīmes, jo ne visas vietnes pieprasa, lai parolēs būtu pieturzīmes. Izveidotās paroles programma ieraksta failā passwords.txt. Turklāt programma var pārbaudīt teksta failā saglabāto paroļu stiprumu, izmantojot tīmekļa pakalpojumu
### Izmantotās bibliotēkas 
+ random
  - Šis modulis tiek izmantots skaitļu ģenerēšanai Python. Tas piedāvā dažādas funkcijas, lai veiktu tādus uzdevumus kā nejaušu skaitļu ģenerēšana, nejaušu elementu atlase no saraksta, nejauša elementu sajaukšana u. c. Skripta gadījumā tas galvenokārt tiek izmantots, lai ģenerētu nejaušus PIN kodus un atlasītu nejaušas rakstzīmes, veidojot paroles.
+ string
  - Modulī ir vairākas noderīgas konstantes, klases un vairākas funkcijas standarta Python virkņu apstrādei. Es to izmantojat savā skripta programmā, lai piekļūtu rakstzīmju kolekcijām, piemēram, string.ascii_letters (mazo un lielo burtu saraksts), string.digits (visi skaitļi 0-9) un string.punctuation (visas pieturzīmes piemēram: ./!@#$%^&), kas ir noderīgas, veidojot rakstzīmju kopas paroles ģenerēšanai.
+ selenium
  - Spēcīgs rīks, kas ļauj kontrolēt tīmekļa pārlūkprogrammas, izmantojot programmas, un veikt pārlūkprogrammu automatizāciju. To plaši izmanto tīmekļa lietojumprogrammu automatizācijai testēšanas nolūkos, taču tas spēj veikt arī jebkuru uzdevumu, ko pārlūkprogrammā var veikt manuāli. Skripta gadījumā Selenium tiek izmantots, lai automatizētu paroles stipruma pārbaudes procesu tīmekļa vietnē. 
  - Tika izmantotas arī Selenium bibliotēkas apakšbibliotēkas (webdriver, Service and ChromeOptions un By)
  - Webdriver ir Selenium daļa, ko izmanto tīmekļa lietojumprogrammu testēšanas automatizēšanai. Tā nodrošina iespēju palaist un mijiedarboties ar dažādām tīmekļa pārlūkprogrammām, piemēram, Chrome, Firefox u. c. Lai mijiedarbotos ar pārlūkprogrammu Chrome, izmantojiet webdriver.Chrome.
  - Service un ChromeOptions: Tos izmanto, lai iestatītu Chrome WebDriver ar īpašām konfigurācijām.
  - By ir Selenium nodrošināta klase, lai atrastu elementus lapā. Piemēram, By.ID ļauj atrast elementus pēc to ID.
+ time
  - Šis modulis nodrošina dažādas ar laiku saistītas funkcijas. Skripta izpildē izmantojiet time.sleep(), lai apturētu skripta izpildi uz noteiktu sekunžu skaitu. Tas ir īpaši noderīgi, kad, izmantojot Selenium, mijiedarbojas ar tīmekļa lapām, dodot laiku, lai lapas ielādētos vai elementi kļūtu pieejami.
  
### Funkcijas
+ PIN4_creat
  -  Ģenerē 4 ciparu PIN kodu. Izmanto random.randint(1,9999), lai ģenerētu nejaušus skaitļus no 1 līdz 9999. Pēc tam šo skaitli pārvērš virknē un, izmantojot zfill(4), aizpilda to ar nullēm kreisajā pusē, lai nodrošinātu, ka tas vienmēr ir 4 ciparu garš.
+ PIN5_creat
  - Ģenerē 5 ciparu PIN kodu. Līdzīgi kā PIN4_creat(), taču tiek ģenerēts skaitlis no 1 līdz 99999 un tas tiek aizpildīts līdz 5 cipariem, izmantojot zfill(5).
+ Password_creat
  -  Izveido paroli, pamatojoties uz lietotāja definētiem kritērijiem (garums un interpunkcijas iekļaušana). Vispirms tiek jautāts lietotājam, vai viņš vēlas, lai parolē tiktu iekļauta interpunkcija. Pēc tam tiek uzdots jautājums par paroles garumu, nodrošinot, ka ievadītais skaitlis ir pozitīvs vesels skaitlis. Pamatojoties uz lietotāja izvēli attiecībā uz interpunkciju, tā izvēlas rakstzīmju kopu no string.ascii_letters, string.digits un pēc izvēles string.punctuation. Visbeidzot, tā ģenerē paroli, nejauši izvēloties rakstzīmes no izvēlētā kopuma, ņemot vērā norādīto garumu.
+ Cheсk_password
  - Pārbauda failā saglabāto paroļu stiprumu, izmantojot tīmekļa pakalpojumu. Izmantota Selenium WebDriver, lai atvērtu un mijiedarbotos ar konkrētu URL (paroles pārbaudes tīmekļa vietni). Lasa paroles no faila ar nosaukumu passwords.txt. Katrai parolei tā ievada paroli tīmekļa vietnē un iegūst tās stipruma novērtējumu. Atjaunina failu ar informāciju par paroles stiprumu.
+ switch_choise
  - Tā kā python nav switch funkcijas, tika nolemts uzrakstīt funkciju, kas izpilda funkciju, pamatojoties uz lietotāja izvēli. Pārveido lietotāja izvēli uz veselu skaitli. Atrod izvēlei atbilstošo funkciju switch_dict vārdnīcā. Ja funkcija pastāv, izsauc un atdod šīs funkcijas rezultātu. Pretējā gadījumā izdrukā kļūdas ziņojumu.
+ Scripts
  - Nodrošina lietotāja saskarni, lai izvēlētos darbību (ģenerēt PIN kodu/paroli vai pārbaudīt paroles stiprumu), un saglabā ģenerētās paroles, ja tas tiek pieprasīts. Tiek parādīta izvēlne un saņemta lietotāja izvēle. Izsauc switch_choise() ar lietotāja izvēli, lai izpildītu attiecīgo funkciju. Ja parole ir ģenerēta, tā piedāvā saglabāt paroli failā passwords.txt.

### Prasības

Programmā ir nepieciešams:
+ Python 3.x
+ Selenium WebDriver
+ ChromeDriver (atbilstoši instalētajai Google Chrome versijai).

### Uzstādīšana un palaišana
1. Python 3.x instalēšana
2. Instalējiet nepieciešamās paketes, izmantojot komandu: **pip install selenium**
3. lejupielādējiet Chrom un pārliecinieties, ka pārlūkprogramma darbojas
4. Lejupielādējiet failu no github un atveriet to ar Visual Studio Code, jo Selenium bibliotēka nevēlas strādāt tieši ar github
Passwords.txt varat arī lejupielādēt un atvērt tādā pašā veidā (programmu un failu ievietojiet vienā mapē). Failā jau ir dažas paroles un to kategorijas. Jums nav nepieciešams lejupielādēt failu ar parolēm, izmantojot programmu, jums tiks piedāvāts izveidot un ierakstīt paroles failā.


