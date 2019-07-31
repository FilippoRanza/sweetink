# sweetink

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4f4c4f52d81145299a944dcba4ca755d)](https://app.codacy.com/app/FilippoRanza/sweetink?utm_source=github.com&utm_medium=referral&utm_content=FilippoRanza/sweetink&utm_campaign=Badge_Grade_Dashboard)

Template per il frontespizio della tesi in LaTex

## Descrizione
Questo progetto contiene dei template per il frontespizio
della tesi di laurea dell'[Università degli Studi di Brescia](https://www.unibs.it/)

I template sono stati realizzati in  modo da soddisfare al meglio
le [specifiche](https://www.unibs.it/segreterie-studenti/laurearsi/esami-di-laurea/redazione-tesi-di-laurea/relazione-finale)
fornite dall'ateneo.

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

## Download
Il download di questo codice può essere effettuato tramite l'apposito
bottone download in alto nella pagina oppute tramite i seguenti link:
*  [zip versione di sviluppo](https://github.com/FilippoRanza/sweetink/archive/master.zip)
*  [zip versione revisionata (Windows)](https://github.com/FilippoRanza/sweetink/archive/v0.1.zip)
*  [tar.gz versione revisionata (macOS - Linux)](https://github.com/FilippoRanza/sweetink/archive/v0.1.tar.gz)
