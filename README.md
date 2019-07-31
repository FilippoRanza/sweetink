# sweetink

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4f4c4f52d81145299a944dcba4ca755d)](https://app.codacy.com/app/FilippoRanza/sweetink?utm_source=github.com&utm_medium=referral&utm_content=FilippoRanza/sweetink&utm_campaign=Badge_Grade_Dashboard)

Template per il frontespizio della tesi in LaTex

## Descrizione
Questo progetto contiene dei template per il frontespizio
della tesi di laurea dell'Università degli Studi di Brescia

I template sono stati realizzati in  modo da soddisfare al meglio
le specifiche fornite dall'ateneo.

## Utilizzo

I template sono pensati per essere pronti all'uso, una volta fatte le
dovute modifiche, illustrate all'interno dei template stessi, basta includerli all'interno del proprio file _.tex_ principale, ad esempio:
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
```
