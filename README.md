# RiNBP25 - opis projekta
**Učinkovitost Rukovanja JSON Podacima: DuckDB naspram Couchbasea**

Uvod

U ovom projektu analizira se učinkovitost rukovanja JSON podacima pomoću DuckDB-a i Couchbasea. Cilj je usporediti DuckDB-ovo JSON parsiranje s nativnim pohranom dokumenata u Couchbaseu u kontekstu analize ugniježdenih podataka, kao što su objave na društvenim mrežama ili katalozi proizvoda. Evaluacija se temelji na izvedbi, brzini pretrage i fleksibilnosti manipulacije podacima u oba sustava. Uz to, istražit će se prednosti i nedostaci svakog rješenja kako bi se identificirao optimalan pristup za različite scenarije uporabe.

Metodologija

Projekt će obuhvatiti sljedeće korake:
Priprema skupa podataka Generiranje ili preuzimanje JSON podataka sa složenom ugniježdenom strukturom, simulirajući stvarne primjene, poput društvenih mreža ili e-trgovine.
Učitavanje podataka Umetanje JSON podataka u DuckDB i Couchbase, analizirajući zahtjeve resursa, veličinu pohranjenih podataka i vrijeme inicijalne obrade.
Izvršavanje upita Pisanje i pokretanje raznih SQL upita za izdvajanje i agregaciju podataka, uključujući jednostavne dohvaćanja, filtriranje, grupiranje i složenije analitičke operacije.
Mjerenje performansi Analiza vremena izvršavanja upita, korištenja memorije, efikasnosti pretrage te sposobnosti skaliranja kod različitih volumena podataka.
Indeksiranje i optimizacija Evaluacija mogućnosti optimizacije performansi korištenjem indeksa, particioniranja podataka i drugih tehnika poboljšanja brzine rada.

 Očekivani Rezultati

DuckDB Trebao bi pokazati visoku učinkovitost u analitičkim upitima zbog kolumnarne arhitekture, što omogućava bržu obradu velikih skupova podataka. Međutim, njegova podrška za JSON strukture mogla bi biti ograničena u odnosu na sustave dizajnirane primarno za rad s dokumentima.
Couchbase Kao NoSQL rješenje, Couchbase bi trebao omogućiti brže dohvaćanje podataka, osobito u scenarijima gdje su upiti nepredvidivi ili gdje postoji potreba za radom u stvarnom vremenu. Njegov indeksni sustav mogao bi osigurati prednost u performansama pri pretrazi specifičnih elemenata unutar JSON dokumenata.
Skalabilnost i primjena Analizom će se utvrditi koji sustav bolje odgovara različitim analitičkim i operativnim scenarijima, uključujući obradu velikih podataka, real-time analitiku i ad-hoc upite.

Zaključak

Rezultati istraživanja pokazat će prednosti i nedostatke svakog pristupa te preporučiti optimalan izbor alata ovisno o specifičnim zahtjevima analize podataka. DuckDB bi mogao biti idealan za analitičke upite na velikim, strukturiranim podacima, dok bi Couchbase mogao biti bolji za fleksibilnije, skalabilne i dinamične aplikacije. Ove spoznaje mogu pomoći istraživačima i tvrtkama u donošenju informiranih odluka o odabiru baze podataka za rad s JSON podacima.

