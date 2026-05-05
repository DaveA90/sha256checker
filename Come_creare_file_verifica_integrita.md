# How to create an integrity verification file

**What is this guide?**
This document explains what a checksum file is, what it is used for, and provides step-by-step instructions on how to manually generate an integrity verification file using the Windows command line, without using the graphical application.

**What is it used for?**
A checksum file (such as `.sha256` or `.sha1`) contains a unique alphanumeric string generated from a file. It is used to ensure that a file (like a video, an executable, or a document) has not been corrupted or tampered with during a download or transfer. Comparing the hash of the downloaded file with the hash saved in the checksum file allows you to verify its authenticity and integrity.

## Windows:

1. Open the Command Prompt (search for "cmd" in the Start menu).
2. Navigate to the folder where your file (e.g., a video) is located using the command `cd path\to\folder` (Windows uses `\` instead of `/`).
3. Type the following command:
   - For SHA-256: `certutil -hashfile video_name.mp4 SHA256`
   - For SHA-1: `certutil -hashfile video_name.mp4 SHA1`
4. Press Enter. The Command Prompt will display the file's hash.

### Save the checksum/hash

Now you have the hash of your file. Here is how to save it:
1. **Copy the hash**: Select and copy the alphanumeric string displayed in the terminal/command prompt.
2. **Create a text file**: Open a text editor (Notepad, TextEdit, etc.) and paste the hash.
3. **Save the file**: Save the text file with a name that identifies the original file, for example:
   - `video_name.mp4.sha256` (if you used SHA-256)
   - `video_name.mp4.sha1` (if you used SHA-1)

**Tips for the text file:**
- You can add a line to describe which algorithm was used.
- You can add a line with the file name.

**For example:**
```text
SHA-256:
File: video_name.mp4
7f83b1657ff1fc53b92dc18148a1d65dfc2d4aec1fa94e085699645c66f9e6d1
```

---

# Come creare un file di verifica integrità

**Cos'è questa guida?**
Questo documento spiega cos'è un file di checksum, a cosa serve e fornisce istruzioni passo-passo su come generare manualmente un file di verifica integrità usando la riga di comando di Windows, senza utilizzare l'applicazione grafica.

**A cosa serve?**
Un file di checksum (come `.sha256` o `.sha1`) contiene una stringa alfanumerica univoca generata a partire da un file. Serve a garantire che un file (come un video, un eseguibile o un documento) non sia stato corrotto o manomesso durante un download o un trasferimento. Confrontando l'hash del file appena scaricato con l'hash salvato nel file di checksum, è possibile verificarne l'autenticità e l'integrità.

## Windows:

1. Apri il Prompt dei comandi (cerca "cmd" nel menu Start).
2. Naviga alla cartella dove si trova il file (es. un video) usando il comando `cd percorso\della\cartella` (Windows usa `\` invece di `/`).
3. Digita il seguente comando:
   - Per SHA-256: `certutil -hashfile nome_del_video.mp4 SHA256`
   - Per SHA-1: `certutil -hashfile nome_del_video.mp4 SHA1`
4. Premi Invio. Il Prompt dei comandi mostrerà l'hash del file.

### Salva il checksum/hash

Ora hai l'hash del tuo file. Ecco come salvarlo:
1. **Copia l'hash**: Seleziona e copia la stringa di caratteri alfanumerici visualizzata nel terminale/prompt dei comandi.
2. **Crea un file di testo**: Apri un editor di testo (Blocco Note, TextEdit, ecc.) e incolla l'hash.
3. **Salva il file**: Salva il file di testo con un nome che identifichi il file originale, ad esempio:
   - `nome_del_video.mp4.sha256` (se hai usato SHA-256)
   - `nome_del_video.mp4.sha1` (se hai usato SHA-1)

**Consigli per il file di testo:**
- Puoi aggiungere una riga per descrivere quale algoritmo è stato usato.
- Puoi aggiungere una riga con il nome del file.

**Per esempio:**
```text
SHA-256:
File: nome_del_video.mp4
7f83b1657ff1fc53b92dc18148a1d65dfc2d4aec1fa94e085699645c66f9e6d1
```
