# BIOS_Project1
  By użyć stworzonego przez nas algorytmu należy otworzyć terminal i ustawić folder docelowy jako projektowy.
  Następnie za pomocą komendy
  
    python main.py [pierwsza sekwencja] [druga sekwencja]
szuka się lokalnego dopasowania między dwiema sekwencjami aminokwasowymi. Na wejściu podaje się dwa argumenty w postaci nazwy pliku z sekwencjami bez precyzowania formatu. Mimo to należy pamiętać,by pliki w folderze były zapisane w formacie fasta, gdyż inaczej program ich nie odczyta.
  Potem program wypisze w terminalu sekwencje wejściowe, uzyskany max score i dwa lokalne dopasowania, które znalazł. Do pliku o nazwie results.txt zostaną zapisane wyniki max score i wyniki dopasowania.
  
  Przykładowe użycie programu:
  
  D:\Projects\BIOS>python main.py rcsb_pdb_1MNH rcsb_pdb_1YOH
GLSDGEWQLVLNVWGKVEADVAGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKVGNRVLTALGGILKKKGHHEAELTPLAQSHATKHKIPVKYLEFISEAIIQVLQSKHPGDFGADAQGAMSKALELFRNDMAAKYKELGFQG

VLSEGEWQLVLHVWAKVEADVAGHGQDIRLFKSHPETLEKFDRFKHLKTEAETTASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGDFGADAQGAMNKALELFRKDIAAKYKELGYQG

Max score of alignment:  206

alignment 1:  LSDGEWQLVLNVWGKVEADVAGHGQEVLIRLFKGHPETLEKFDKFKHLKSEDEMKASEDLKKVGNRVLTALGGILKKKGHHEAELTPLAQSHATKHKIPVKYLEFISEAIIQVLQSKHPGDFGADAQGAMSKALELFRNDMAAKYKELGFQG

alignment 2:  LSEGEWQLVLHVWAKVEADVAGHGQ--DIRLFKSHPETLEKFDRFKHLKTEAETTASEDLKKHGVTVLTALGAILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGDFGADAQGAMNKALELFRKDIAAKYKELGYQG

(druga sekwencja została lekko zmodyfikowana w celu pokazania możliwości programu w poprawnym odnajdywaniu dopasowania w przypadku wystąpienia indeli lub niedopasowań lokalnych)
