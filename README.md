Usporedba baza podataka: DuckDB vs MySQL na skupu podataka "Million News Headlines"
Opis projekta
Ovaj projekt ima za cilj usporediti performanse i praktičnost korištenja DuckDB i MySQL baza podataka pri analizi stvarnog podatkovnog skupa — Million News Headlines, koji sadrži više od milijun naslova vijesti australske novinske agencije ABC od 2003. do 2021. godine.

Ciljevi
Usporediti vrijeme izvođenja upita između DuckDB-a i MySQL-a

Usporediti jednostavnost implementacije analitičkih upita

Evaluirati pogodnost za obradu tekstualnih i vremenskih podataka

Prezentirati rezultate kroz mjerne tablice i zaključke

Korišteni podaci
Dataset: Million News Headlines (Kaggle)
https://www.kaggle.com/datasets/therohk/million-headlines/data
Format: CSV
Polja:

publish_date – datum objave naslova (YYYYMMDD)

headline_text – tekstualni naslov vijesti

Tehnologije
DuckDB 

MySQL 

Python (pandas, duckdb, pymysql, time)

Jupyter Notebook

Testirani upiti
Broj vijesti po godini

Filtriranje naslova koji sadrže određenu ključnu riječ (npr. "war")

Broj naslova po danu/tjednu

Učestalost pojavljivanja pojedinih riječi (jednostavna analiza)

Mjerenje performansi
Vrijeme izvođenja svakog upita mjerilo se u sekundama pomoću Python modula time. Uspoređena su vremena izvođenja istih upita nad identičnim podacima u obje baze.

Zaključak
DuckDB se pokazao kao izuzetno praktičan za analitičku obradu većih skupova podataka, s izrazito jednostavnom integracijom u Python okruženje. MySQL je stabilan i moćan alat, pogotovo za dugoročno spremanje i upravljanje podacima, ali zahtijeva više konfiguracije i nije optimiziran za analizu u memoriji.
