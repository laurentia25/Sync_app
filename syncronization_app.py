import os

"""
Vă rugăm să implementați un program care sincronizează două foldere: sursă și replica.
Programul ar trebui să mențină o copie completă, identică a folderului sursă la folderul replica.

->  Sincronizarea trebuie să fie unidirecțională: după sincronizare, conținutul folderului replica ar 
    trebui să fie modificat pentru a se potrivi exact cu conținutul folderului sursă;
    
->  Sincronizarea trebuie efectuată periodic;

->  Operațiunile de creare/copiere/eliminare a fișierelor ar trebui să fie înregistrate într-un fișier și în ieșirea consolei;
    Căile pentru foldere, intervalul de sincronizare și calea fișierului jurnal trebuie furnizate folosind argumentele liniei
    de comandă;
"""
path = "C:\\Users\Laurentia\OneDrive\Рабочий стол\Proiecte\Automated_testing\BDD_project"
list = os.listdir(path)

print(list)