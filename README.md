# Veckouppgift 3 - Prestandatest

## 📊 Status

Här nedan presenteras en översikt över statusen på lösande av uppgfterna.

| Uppgift                          | Status |
|:---------------------------------|:------:|
| 0. Projektstruktur               |   🟢   |
| 1. Diskussionsfrågor             |   🟢   |
| 2. Prestandatest: Insertion sort |   🟡   |
| 3. Prestandatest: merge sort     |   🔴   |


## 0️⃣Projektstruktur
Skapa ett projekt enligt alla konstens regler, på det sätt vi gått igenom på lektionen.



## 1️⃣Diskussion

### Uppgift: 
Svara på frågorna:
1. Vad är en regression? När inträffar de oftast under ett projekts livstid?
En regression är när något som tidigare fungerat slutat fungera efter en ändring. 
De inträffar oftast då någon förändring av koden sker. Det kan vara vid:
- Implementering av ny kod
- Refaktorering - Förändring av befintlig kod ändrar beteendet
- Bugfixning - lösning av ett problem skapar ett annat
- Ändringar av kodens beroenden
- Förändring av gränssnitt mor databeser och api'er

2. Vad är skillnaden mellan enhetstest och regressionstest?
Enhetstest är det initiala testet av delsystem, t.ex. en funktion. Syftet är att kontrollera  
att en specifik del fungerar korrekt. Regressionstest syftar till att verifiera att tidgiare
implementerad kod fungerar efter ändringar. Det innebär att ett test som från början var ett
enhetstest kan bli ett regressionstest senare i projektet.   


3. Vilka krav på git-kunskap kräver det av utvecklare att jobba med CI? 
GIT är en central del i CI konceptet. Då en ändring gjorts i ett repository startar ofta
en pipeline automatiskt. Den kan då t.ex. köra tester och bygga kod. Den som arbetar med 
CI bör minst vara bekant med kommandona Clone, Pull, Add, Commit, Push. Det är också viktigt
att förstå begreppen branch och merge samt kunna hantera pull och merge requests.


4. Vad är en feature? Hur förhåller det sig till kraven? 
En feature är oftast en funktion eller funktionalitet i ett system. Det är en del av 
systemet som kan göra något för användaren av detsamma. Det kan t.ex. vara en inloggnings-
funktion, gör en betalning eller lägga till en vara i en kundkorg.  
En feature motsvarar ofta ett funktionellt krav och motsvarar en del av vad systemet ska 
kunna göra. Featuren utvecklas för att uppfylla ett funktionellt krav. T.ex. kan ett krav 
vara att användaren ska kunna radera ett testfält och detta leder till en funktionalitet som 
uppfyller kravet - "text_filed-reset".


5. Vilka fördelar får en kund av att utvecklarna jobbar med CD?  
Att arbete md CD medför ofta snabbare leveranstider, felrättning och feedback av nya leveranser. 
Automatiska tester körs regelbundet, vilket ökar kvalitén och miskar risken för regression. Man 
slipper stora komplexa och oförutsägbara leveranser. Med mindre och snabbare leveranser kan kunden 
snabbt få tillgång till ny funktionalitet och projektet får fortlöpande feedback på levererad funktionalitet.


6. Vilka fördelar får utvecklare av att jobba med CD?  
Fördelarna för utvkecklarna övernstämmer mycket med de för kunden. Automatiserade processer 
minskar behovet av manuellt arbete. Då varje förändring är mindre blir det lättare att hitta 
eventuella fel och buggar. Utvecklaren får snabbt feedback om den nya koden är tillfyllest eller
om den orsakar fel.


7. Varför kan man inte veta exakt hur lång tid det kommer ta att köra kod?   
Det är många faktorer som påverkan hur lång tid det tar att köra kod. Datorn som koden körs
på kan ha olika prestanda på OS, CPU, GPU och minnen. Lagringsmedia och nätverk kan variera då koden
läser data och filer. Datorns cache kan innehålla data vid ett körtillfälle och inte vid ett annat.


8. Varför skriver man till exempel O(n) men inte O(2*n + 10)?  
Big O tar inte hänsyn till några exakta detaljer, utan används för att beskriva hur tiden 
ökar när n blir större. Värdet + 10 blir ointressant redan vid mindre ökningar av n. Om n = 
10 blir 2n + 10 = 30. Om man ökar n till 100 blir 2n + 10 = 210. 2n har en mycket större inverkan 
på tidsåtgången än de + 10. Konstanten (2) för 2n spelar ingen roll för tillväxttakten. Om n = 10 
är 2n = 20. Ökas n till 20 blir 2n 40. Ökningen är alltså proportionellt lika och man kan bortse
från konstanten då tillväxttakten är densamma. 


## 2️⃣ Prestandatest: Insertion sort

## 3️⃣  Prestandatest: merge sort


