import subprocess
import sys
import webbrowser
import time
import os

def avvia_streamlit():
    percorso = os.path.join(os.path.dirname(sys.argv[0]), 'app.py')
    processo = subprocess.Popen([
        'streamlit', 'run', percorso,
        '--server.headless=true',
        '--server.port=8501'
    ])
    return processo

if __name__ == "__main__":
    processo = avvia_streamlit()
    
    # Aumenta il tempo di attesa (ad esempio 10 secondi)
    time.sleep(10)

    # Apri automaticamente il browser quando il server è avviato
    webbrowser.open('http://localhost:8501')

    # Attendi la chiusura del processo
    processo.wait()
