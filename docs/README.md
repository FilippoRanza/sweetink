# sweetink

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4f4c4f52d81145299a944dcba4ca755d)](https://app.codacy.com/app/FilippoRanza/sweetink?utm_source=github.com&utm_medium=referral&utm_content=FilippoRanza/sweetink&utm_campaign=Badge_Grade_Dashboard)  [![Build Status](https://travis-ci.com/FilippoRanza/sweetink.svg?branch=master)](https://travis-ci.com/FilippoRanza/sweetink)

Template per il frontespizio della tesi in LaTex

## Descrizione
Questo progetto contiene dei template per il frontespizio
della tesi di laurea dell'[Università degli Studi di Brescia](https://www.unibs.it/)

I template sono stati realizzati in  modo da soddisfare al meglio
le [specifiche](https://www.unibs.it/segreterie-studenti/laurearsi/esami-di-laurea/redazione-tesi-di-laurea/relazione-finale)
fornite dall'ateneo.

### File Utili
I file di interesse per l'utente finale sono:
*   [Frontespizio per la Tesi Triennale](https://github.com/FilippoRanza/sweetink/blob/master/frontespizio_triennale.tex)
*   [Frontespizio per la Tesi Magistrale](https://github.com/FilippoRanza/sweetink/blob/master/frontespizio_magistrale.tex)
*   [Stemma dell'Università](https://github.com/FilippoRanza/sweetink/blob/master/logo_unibs.png)

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

### Note Compilazione
Il codice viene compilato automaticamente in ambiente:
*   _Linux_ utilizzando _texlive-full_
*   _macOS_ utilizzando _mactex_
*   _Windows_ utilizzando _miktex_ (attualmente su Windows non è possible il testing)

Per compilare con successo il codice fornito è consigliato installare 
la versione completa dei pacchetti LaTex per la propria piattaforma

## Download
Il download di questo codice può essere effettuato tramite l'apposito
bottone download in alto nella pagina oppute tramite i seguenti link:
*   [zip versione di sviluppo](https://github.com/FilippoRanza/sweetink/archive/master.zip)
*   [zip versione revisionata (Windows)](https://github.com/FilippoRanza/sweetink/archive/v0.1.zip)
*   [tar.gz versione revisionata (macOS - Linux)](https://github.com/FilippoRanza/sweetink/archive/v0.1.tar.gz)