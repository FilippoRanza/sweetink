# sweetink
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
