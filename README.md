# Security Checksum Generator and Verifier

This is a desktop application with a graphical interface (developed in Python using Tkinter) that allows you to easily generate and verify file checksums. The program relies on the built-in Windows system utility `certutil` to perform cryptographic calculations.

## Main Features

1. **Checksum Generation**:
   - Calculates the cryptographic hash of any file using **SHA-1** or **SHA-256** algorithms.
   - Allows saving the generated hash into a dedicated text file (e.g., `.sha1` or `.sha256`).
   - Option to include additional details within the text file (like the used algorithm and the analyzed file name) alongside the checksum value.

2. **File Integrity Verification**:
   - Allows comparing a file with a pre-existing checksum file (`.sha1` or `.sha256`).
   - Provides an immediate visual response ("Valid" or "NOT Valid"), clearly indicating whether the file is intact or if it has been modified or corrupted.

## Prerequisites

- **Python 3.x**: The language in which the script is written.
- **Windows Operating System**: Essential, as the application natively calls the built-in Windows `certutil` command.

## Usage Instructions

1. Start the application by running the `codice_sha.py` file (by double-clicking it or via terminal with `python codice_sha.py`).
2. To **Generate** a checksum:
   - Use the "Browse" button in the "Generate Checksum" section to select your file.
   - Choose the desired algorithm using the corresponding buttons (SHA-1 or SHA-256).
   - Click "Generate Checksum" to calculate the hash. The output will appear in the text box.
   - Use "Save Checksum" to save the result to a file.
3. To **Verify** the integrity of a file:
   - In the lower section "Verify File Integrity", select the file to check.
   - Select the original checksum file.
   - Click "Verify Integrity" to get the result of the check.

---

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
