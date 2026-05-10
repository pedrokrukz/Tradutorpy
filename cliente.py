
from langserve import RemoteRunnable

chain_remote = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remote.invoke({"idioma": "alemão", "texto": "Basquete é chato"})
print(texto)
