# sweetink

Template per il frontespizio della tesi in LaTex

## Descrizione
Questo progetto contiene dei template per il frontespizio
della tesi di laurea dell'[Università degli Studi di Brescia](https://www.unibs.it/)
realizzati in latex.

I template sono stati realizzati in  modo da soddisfare al meglio
le [specifiche](https://www.unibs.it/segreterie-studenti/laurearsi/esami-di-laurea/redazione-tesi-di-laurea/relazione-finale)
fornite dall'ateneo.

### File Utili
Qui sono presenti i template dei frontespizi
*   [Frontespizio per la Tesi Triennale](triennale.html)
*   [Frontespizio per la Tesi Magistrale](magistrale.html)

Per il download si raccomanda l'utilizzo degli appositi bottoni 
in cima alla pagina, i quali consentono di scaricare anche 
il logo dell'Università utilizzato all'interno dei template.

## Utilizzo
I template sono pensati per essere pronti all'uso, una volta fatte le
dovute modifiche, illustrate all'interno dei template stessi, basta includerli
all'interno del proprio file _.tex_ principale, ad esempio:
```latex
% dovrebbe essere la prima riga del corpo del documento
\include{frontespizio_magistrale}
```

Per poter compilare il documento è necessario includere alcuni 
pacchetti esterni:
```latex
% vanno aggiunti fuori dal corpo del documento
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{graphicx}
```

È dunque sufficente copiare il template d'interesse e il logo 
dell'ateneo nella cartella in cui è presente il codice latex
della tesi e procedere con le opportune modifiche.  

Una volta fatto è possibile eliminare i file scaricati 
senza alcun problema.

### Note Compilazione
Il codice viene compilato automaticamente in ambiente:
*   _Linux_ utilizzando _texlive-full_
*   _macOS_ utilizzando _mactex_
*   _Windows_ utilizzando _miktex_ (attualmente su Windows non è possible il testing)

Vista la necessità di diversi pacchetti esterni, per procedere ad una compilazione 
corretta è consigliato di installare la versione completa dell'ambiente di
sviluppo latex per la propria piattaforma.
