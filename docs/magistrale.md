# Template Frontespizio Tesi Magistrale

```latex
\newgeometry{left=20mm,right=20mm,top=25mm,bottom=20mm}
\begin{titlepage}
    \begin{center}
        
        \begin{figure}[t]
            \centering
            \includegraphics[width=72.4mm,height=30mm]{logo_unibs.png}    
        \end{figure}

        \vspace*{10mm}
        
        {\fontsize{17}{17}\fontfamily{lmss}\selectfont
            % se risci a trovare avent pavm8r
            % Inserisci qui il dipartimento
            DIPARTIMENTO DI ...........\\
        }

        \vspace*{10mm}

        {\fontsize{17}{17}\fontfamily{cmss}\selectfont
            Corso di Laurea Magistrale\\
            % inserisci qua il corso di laurea
            in ...........\\

        }    
        
        \vspace*{20mm}

        {\fontsize{20}{20}\fontfamily{lmss}\selectfont 
            % inserisci il titolo
            Tesi di Laurea\\
            Titolo 1\\
            Titolo 2\\
            Titolo 3\\
        }

    \end{center}

    \vfill

    \begin{flushleft}
        % inserisci il nome del relatore
        {\fontsize{17}{17}\fontfamily{lmss}\selectfont 
            \textbf{Relatore:} Chiar.mo Prof. ..........
            \textbf{Correlatore:} Chiar.mo Prof. ..........
        }
        
    \end{flushleft}

    \vspace*{5mm}

    \begin{flushright}
        % completa con il tuo nome e matricola
        {\fontsize{17}{17}\fontfamily{lmss}\selectfont 
            Laureand..:\\
            ............\\
            Matricola n. .......\\
        }

    \end{flushright}

 
    \vspace*{5mm}

    \rule{0.8\textwidth}{0.4pt}
    \begin{center}
    {\fontsize{17}{17}\fontfamily{lmss}\selectfont 
        % specifica l'anno accademico
        Anno Accademico ........
    }
    \end{center}
    
    
\end{titlepage}
\restoregeometry
```
