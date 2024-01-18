# Nosleguma projekts
## Password Generator and Strength Checker
### Apraksts

Šis projekts ietver programmu paroļu ģenerēšanai un to stipruma pārbaudei. Programma ļauj izveidot gan vienkāršus PIN kodus, gan sarežģītas paroles ar iespēju iekļaut īpašās zīmes, jo ne visas vietnes pieprasa, lai parolēs būtu pieturzīmes. Izveidotās paroles programma ieraksta failā passwords.txt. Turklāt programma var pārbaudīt teksta failā saglabāto paroļu stiprumu, izmantojot tīmekļa pakalpojumu

### Funkcijas
+ Četrciparu PIN kodu ģenerēšana
+ Piecciparu PIN kodu ģenerēšana
+ Paroļu ģenerēšana ar iepriekš iestatītu garumu un iespēju iekļaut īpašās rakstzīmes
+ Paroles stipruma pārbaude no faila
+ Izvēles slēdzis (switch), tā kā python nav switch funkcijas, tika nolemts uzrakstīt funkciju, kas izsauks funkcijas atkarībā no lietotāja izvēles. To pašu varētu izdarīt ar if. Šim nolūkam tika izveidota arī vārdnīca, kuras atslēgas ir lietotāja ievadītie cipari, bet vērtība ir funkcijas izsaukums.

### Prasības

Programmā ir nepieciešams:
+ Python 3.x
+ Selenium WebDriver
+ ChromeDriver (atbilstoši instalētajai Google Chrome versijai).

