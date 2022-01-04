# importazione delle librerie necessarie
# https://www.fabiobiffi.it/sito/web-server-python/
import http.server
import socketserver
import os

# definizione di una costante col numero di porta
PORT = 8000
# definizione di una costante col nome della cartella root
ROOT_FOLDER = 'wwwroot'

# settaggio della cartella root
web_dir = os.path.join(os.path.dirname(__file__), ROOT_FOLDER)
os.chdir(web_dir)

# istanziamento del server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT) # log di successo
# servizio attivo fino all'interruzione manuale del programma
httpd.serve_forever()