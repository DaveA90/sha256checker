# Generatore e Verificatore Checksum di Sicurezza

Questa è un'applicazione desktop con interfaccia grafica (sviluppata in Python usando Tkinter) che permette di generare e verificare i checksum dei file in modo semplice ed intuitivo. Il programma si appoggia all'utility di sistema `certutil` presente su Windows per effettuare i calcoli crittografici.

## Funzionalità Principali

1. **Generazione Checksum**:
   - Calcola l'hash crittografico di qualsiasi file utilizzando gli algoritmi **SHA-1** o **SHA-256**.
   - Possibilità di salvare l'hash generato in un file di testo dedicato (es. `.sha1` o `.sha256`).
   - Opzione per includere all'interno del file di testo ulteriori dettagli (come l'algoritmo utilizzato e il nome del file analizzato) insieme al valore del checksum.

2. **Verifica Integrità File**:
   - Permette di confrontare un file con un file di checksum (`.sha1` o `.sha256`) preesistente.
   - Fornisce un responso visivo immediato ("Valida" o "NON Valida") indicando chiaramente se il file è integro, oppure se è stato modificato o corrotto.

## Prerequisiti

- **Python 3.x**: Il linguaggio in cui è scritto lo script.
- **Sistema Operativo Windows**: Essenziale, poiché l'applicazione richiama nativamente il comando `certutil` integrato nei sistemi Windows.

## Istruzioni per l'Uso

1. Avvia l'applicazione eseguendo il file `codice_sha.py` (facendo doppio clic su di esso o tramite terminale con `python codice_sha.py`).
2. Per **Generare** un checksum:
   - Usa il pulsante "Sfoglia" nella sezione "Genera Checksum" per selezionare il tuo file.
   - Scegli l'algoritmo desiderato tramite i pulsanti appositi (SHA-1 o SHA-256).
   - Clicca su "Genera Checksum" per calcolare l'hash. L'output comparirà nel box di testo.
   - Usa "Salva Checksum" per salvare il risultato su file.
3. Per **Verificare** l'integrità di un file:
   - Nella sezione inferiore "Verifica Integrità File", seleziona il file da controllare.
   - Seleziona il file di checksum originale.
   - Clicca su "Verifica Integrità" per ottenere l'esito del controllo.
