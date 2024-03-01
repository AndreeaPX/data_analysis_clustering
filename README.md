# data_analysis_clustering
Sursa datelor : http://statistici.insse.ro:8077/tempo-online/#/pages/tables/insse-table
În cadrul acestei aplicații au fost folosite două seturi de date principale, anume:
1.	Unitățile de învățământ pe niveluri de educație, județe si localități, în anul 2020 (neincluzând formele de învățământ special)
Secțiunea Educație – Unități școlare - Unitățile de învățământ pe niveluri de educație, județe si localități
Acest fișier de intrare are numele „unități_învățământ.csv”
3.	Populația școlară, pe niveluri de educație, județe si localități în anul 2020 (neincluzând formele de învățământ special)
Secțiunea Educație –Populația școlară- Populația școlară, pe niveluri de educație, județe si localități
Acest fișier de intrare are numele „persoane_înscrise.csv”

În cadrul acestei teme am plecat de la setul de date precizat mai sus, care include prezența informațiilor pentru Municipiul București. Acest fapt, după cum vom observa pe parcurs, a determinat crearea unui cluster special pentru această componentă a setului de date. În prima fază a proiectului, am realizat analiza setului de date incluzând și Municipiul București. A doua faza prezinta aceeasi analiza, insa fara Municipiu, deoarece se poate observa cu usurinta faptul ca acesta reprezinta o variabila de tip outlier.
