import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuració del servidor SMTP
SMTP_SERVER = "smtp.prova.com"  # Servidor SMTP del nostre proveïdor
SMTP_PORT = 465  # Port de la connexió SSL/TLS
SMTP_USER = "miquel@prova.com"  # El teu correu electrònic
SMTP_PASSWORD = "password"  # La teva contrasenya

# Demandar a l'usuari quin missatge vol enviar (inicial o final)
opcio = input("Quin missatge vols enviar? (1: inicial, 2: final): ")

if opcio == "1":
    arxiu_missatge = "missatge_inicial.txt"
elif opcio == "2":
    arxiu_missatge = "missatge_final.txt"
else:
    print("Opció no vàlida. Sortint del programa.")
    exit()

# Llegir el missatge del fitxer
try:
    with open(arxiu_missatge, "r") as file:
        linies = file.readlines()
        assumpte = linies[0].replace("Assumpte:", "").strip()  # Primera línia com a assumpte
        missatge_base = "".join(linies[1:]).strip()  # Resta del fitxer com a cos del missatge
except FileNotFoundError:
    print(f"L'arxiu {arxiu_missatge} no existeix. Assegura't que està en la mateixa carpeta.")
    exit()

# Càrrega del fitxer CSV
arxiu_csv = "usuaris.csv"  # Assegura't també que el fitxer CSV està en la mateixa carpeta
try:
    df = pd.read_csv(arxiu_csv)
except FileNotFoundError:
    print(f"L'arxiu {arxiu_csv} no existeix. Assegura't que està en la mateixa carpeta.")
    exit()

# Connexió amb el servidor SMTP
try:
    print("Connectant al servidor SMTP...")
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)  # Utilitza SMTP_SSL per al port 465
    server.login(SMTP_USER, SMTP_PASSWORD)
    print("Connexió al servidor SMTP establerta.")
except Exception as e:
    print(f"Error al connectar amb el servidor SMTP: {e}")
    exit()

# Enviament de correus electrònics
for _, fila in df.iterrows():
    nom = fila["nom"]
    destinatari = fila["email"]
    
    missatge_personalizat = missatge_base.format(nom=nom)

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = destinatari
    msg["Subject"] = assumpte
    msg.attach(MIMEText(missatge_personalizat, "plain"))

    try:
        server.sendmail(SMTP_USER, destinatari, msg.as_string())
        print(f"Correu enviat a {nom} ({destinatari})")
    except Exception as e:
        print(f"Error enviant correu a {nom} ({destinatari}): {e}")

# Cierre de la conexión
server.quit()
print("Tots els correus s'han enviat correctament.")
