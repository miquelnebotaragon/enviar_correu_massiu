# 📤 Enviament massiu de correu des de Python
[![Website](https://img.shields.io/badge/Moodle-miquelnebot.eu-blue)](https://miquelnebot.eu)
[![License](https://img.shields.io/badge/Llicència-MIT-green)](LICENSE)

# 👁️‍🗨️ Introducció

Aquest projecte és una aplicació senzilla escrita en Python que permet enviar correus electrònics personalitzats a una llista de destinataris a partir d’un fitxer CSV que conté únicament el nom i el mail. El missatge es pot escollir entre dos tipus (inicial o final) que es llegeixen des de fitxers de text (adjunts al repositori).

# ✅ Funcionalitats
- Connexió segura a un servidor SMTP (amb SSL/TLS).
- Enviament de correus personalitzats amb nom del destinatari inclòs.
- Permet escollir entre diferents missatges predefinits.
- Gestió d’errors bàsica en connexió i enviament.
- Llegeix els destinataris i les dades de contacte d’un fitxer CSV.

# 💻 Requisits

- Python 3.6 o superior
- Paquet **pandas**

# 🔌 Instal·lació

1. Clona o descarrega aquest repositori.

2. Instal·la les dependències:

    ```bash
    pip install pandas
    ```

3. Assegura’t de tenir els fitxers següents a la mateixa carpeta que l’script:

    - `usuaris.csv` — Fitxer CSV amb les columnes `nom` i `email`.
    - `missatge_inicial.txt` — Fitxer de text amb el missatge inicial. La primera línia ha de començar amb `Assumpte:`, la resta és el cos del missatge.
    - `missatge_final.txt` — Fitxer de text amb el missatge final, amb el mateix format que el missatge inicial.

# 🛠️ Configuració

Edita les variables de configuració a l’inici del fitxer Python per afegir les teves dades SMTP:

```python
SMTP_SERVER = "smtp.prova.com"
SMTP_PORT = 465
SMTP_USER = "el_teu_correu@prova.com"
SMTP_PASSWORD = "la_teva_contrasenya"