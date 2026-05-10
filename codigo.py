from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
api_key = os.getenv("OPENAI_KEY") 

mensagens = [
    SystemMessage("Traduza o texto a seguir para o inglês:"),
    HumanMessage("Futebol é legal")
]                                                                  #modelo de mensagem

modelo = ChatOpenAI(temperature=0.3, model="gpt-4o-mini")          #onde vem a resposta
parser = StrOutputParser()                                         #transforma a resposta em string
chain = modelo | parser 

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para o {idioma}"),
    ("user", "{texto}"),                                           #prompts
])
#print(template_mensagem.invoke({"idioma": "inglês", "texto": "Basquete é chato"}))

chain = template_mensagem | modelo | parser # essa é a cadeia sequencial
#texto = chain.invoke({"idioma": "alemão", "texto": "Basquete é chato"})

#print(texto)
