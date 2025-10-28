
# OGSZG - interni pretraživač sudske prakse

Jednostavan Python/Flask webapp za dodavanje i pretragu sudske prakse koji sam izradio za OGSZG.<br>
Iz .docx datoteka koje mogu sadržavati više primjera sudske praske, aplikacija izvlači sudske praske pojedinačno i sprema ih u databazu.<br>
<br>
Webapp je u Flask direktoriju.<br>
U početnom direktoriju su 4 skripte, počevši od 0starter.py koji pokreće sljedeće 3 skripte i u tom procesu briše staru databazu i dokumente koje je u prethodnim radnjama izvukao.<br>
Navedene skripte služe izvlačenju sudske praske iz dokumenta koji sadrže više istih, a potom se ti dokumenti spremaju u Extracted_sections direktorij.<br>
Nakon toga skripta 2. dodaje izvučene dokumente u databazu.<br>
Zadnji korak 3.check_db.py kreira jednostavnu html.html stranicu za test preview funkcionalnosti.

