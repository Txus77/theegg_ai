import requests
from bs4 import BeautifulSoup
import re
import operator

def extraer_texto():
    
    r=requests.get("http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/")

    print(r.status_code)

    webtexto=BeautifulSoup (r.text,"html.parser")

    texto_buscado = webtexto.find_all("p" ) #busco todas las etiquetas <p>, find_all me da una lista de todas

   
    listacadena=[] #creo una lista con los textos de todas las etiquetas <p>
    
    for i in texto_buscado:
        tag_element=i.text #saco el texto de cada etiqueta
        listacadena.append(tag_element) 
            
    textocadena=" ".join(listacadena) #convierto la lista anterior en una cadena
    
    regex_texto_inicio=re.compile(r"En Strandhill, Irlanda")#para buscar el texto que quiero lo hago con una expresión regular poniendo como patrón el inicio del texto buscado
    regex_texto_final= re.compile(r"también te han pasado cosas así.")#para buscar el texto que quiero lo hago con una expresión regular poniendo como patrón el final del texto buscado
    
    coincidencia_inicio=re.search(regex_texto_inicio, textocadena)#defino la busqueda con la función "search" que me da la primera coincidencia que encuentre
    coincidencia_final=re.search(regex_texto_final, textocadena)
    
    indice_inicio=coincidencia_inicio.start()#establezco en el indice de la cadena donde empieza el texto
    indice_final=coincidencia_final.end()#establezco en el indice de la cadena donde finaliza el texto
    
    textofinal=textocadena[indice_inicio:indice_final]
   
    return textofinal

texto=extraer_texto()# El texto lo he sacado con scraping para poner en practica más cosas pero si no se puede poner aquí la cadena que interese sacar


def normalizar(palabra):
    
    """ función para limpiar de caracteres especiales el texto para poder ordenar las palabras alfabéticamente tras haberlas ordenado primero por el número de repeticones en el texto.
    Para simplificar únicamente considero como caracteres especiales los acentos y la ñ"""
    
    i=palabra
    traducido=i.maketrans("áéíóúÁÉÍÓÚüÜñ", "aeiouAEIOUuUn")#El metodo maketrans () permite crear una tabla de asignación que luego se ejecuta llmando al metodo translate()
    palabra_sin_acento=i.translate(traducido)
        
    return (palabra_sin_acento + " . La palabra correctamente escrita es - "+ i + " -" )#Es importante distinguir las palabras que tenían acento ya que si no si tengo 2 palabras iguales una acentuada y la otra no me la considera como la misma en la lista ordenada


def buscar_num_caracteres():
    
    patron=r"\S"
    regex_caracteres=re.compile(patron)
    
    lista_caracteres=re.findall(regex_caracteres,texto)
    print("El número total de caracteres es de: ", len(lista_caracteres))


def palabras():
    
    patron=r"[a-zA-ZñÑáÁéÉíÍóÓúÚüÜ]+"#se establece este patrón para considerar únicamente las palabras compuestas por letras. También se consideran los acentos, dieresis y la ñ. Si quisieramos considerar también números sería r"\w+"
    regex_palabras=re.compile(patron)
    lista_palabras=re.findall(regex_palabras,texto)
    lista_palabras_minus=[x.lower() for x in lista_palabras]#pongo todas las palabras en minúsculas para que no me considere palabras diferentes en caso de quew esté alguna letra en mayúsculas
    print("El número de palabras es: ", len (lista_palabras_minus))
    return lista_palabras_minus


def ordenar_palabras():
    """Con esta función determino el número de repeticiones de cada palabra y las ordeno primero por número de repeticiones de más a menos y, luego, alfabéticamente entre las que se han repetido el mismo número de veces"""
    y=palabras()
    conjunto=set(y) #Convierto la lista de palabras en un conjunto para obtener las palabras sin repeticiones
    listaconj=list(conjunto)
    
    diccinario={}#creo un diccionario con clave cada palabra del conjunto creado y como valor el número de repeticiones
    
    for j in listaconj:
        k=y.count(j)
        diccinario[j]=k
    
    diccionario_normalizado={}
    
    for m,p in diccinario.items():
        if "á" in m  or "é" in m  or "í" in m or "ú" in m or "ñ" in m:
            m= normalizar(m)
        diccionario_normalizado[m]=p
        
    #Como quiero realizar una doble ordenación inversa una de otra (de mayor a menor en valor y de menor a mayor en clave) primero ordeno por la clave ya que esta ordenación es secundaria y luego por el valor que es la ordenación principal.
    orden1=dict((sorted(diccionario_normalizado.items(),key=operator.itemgetter(0))))
    orden=dict(sorted(orden1.items(), key=operator.itemgetter(1), reverse=True))#el metodo itemgetter del modulo operator  sirve para referirmos o a la clave "itemgetter(0) o al valor "itemgetter(1)"" cuando queremos ordenar con la funcion sorted ()

    for m,p in orden.items():

        print(m+" :se repite "+str(p)+" veces")


buscar_num_caracteres()

ordenar_palabras()  


