## ρυθμιση php 

sto path C:\Apache24\conf to file httpd antikatastasi sthn proteleytaia grammi poy prosthesame prin toy AddTupe me AddHandler



(proairetika) -> start -> Services.msc -> Apache24 -> restart


sto C:\Apache24\htdocs new file me onoma info.php  apo notepad o code:




<? php
phpinfo();
?>



save as info.php all files



if it is ok, then open browser -> http://.../info.php -> and appears php informations




## εγκατάσταση phpmyadmin 
κατεβασμα απο το site all languages 

δημιουργια φακελου στο htdocs -> phpmyadmin 

εξαγωγη ολων των στιιχειων του zip εκει 
προσοχη μην γινει διπλος φακελος 

στον φακελο που δημιουργησες κάνεις αντιγραφη το config sample.inc.php και το μετονομαζεις το καινούριο σε config.inc.php

ανοίγεις το καινουριο και στηβ γραμμη 16 προσθέτεις εναν τυχαίο κωδικό 32 χαρακτήρων 


ανοίγεις το httpd.conf και προσθέτεις στο τελος 

Alias /phpmyadmin "C:/Apache24/htdocs/phpmyadmin"
<Directory "C:/Apache24/htdocs/phpmyadmin">
    AllowOverride All
    Require all grunted
</Directory>

and save.


cmd as admin
cd C:\Apache24\bin 
httpd -k restart


ανοιξε το http://localhost/phpmyadmin 
