#CREAR 10 EJERCICIOS POR CADA OPERACION DE DICCIONARIOS:

print("==============================   1.CREACIÓN   ===================================\n")

#EJERCICIO 01 - CREACIÓN
dict_vacio=dict()
print("1.  El diccionario creado es:",dict_vacio)

#EJERCICIO 02 - CREACIÓN
nros={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco"}
print("2.  El diccionario creado es:",nros)

#EJERCICIO 03 - CREACIÓN
cuaderno=dict(cuaderno="escribir",programa="python")
print("3.  El diccionario creado es:",cuaderno)

#EJERCICIO 04 - CREACIÓN
romanos=dict({"I":"uno","V":"cinco","X":"diez"})
print("4.  El diccionario creado es:",romanos)

#EJERCICIO 05 - CREACIÓN
clasificacion={"pais":"Peru","departamento":"Lambayeque","provincia":"chiclayo"}
print("5.  El diccionario creado es:",clasificacion)

#EJERCICIO 06 - CREACIÓN
hola=["hola","mundo"]
progra=["bienvenidos","programadores"]
diccionario=dict(zip(hola,progra))
print("6.  El diccionario creado es:",diccionario)

#EJERCICIO 07 - CREACIÓN
tiempo=dict(dia="24 horas",hora="60 minutos",minuto="60 segundos")
print("7.  El diccionario creado es:",tiempo)

#EJERCICIO 08 - CREACIÓN
dia={"dia":"sol","noche":"luna"}
print("8.  El diccionario creado es:",dia)

#EJERCICIO 09 - CREACIÓN
animales=dict(insecto="hormiga",ave="aguila",reptil="iguana")
print("9.  El diccionario creado es:",animales)

#EJERCICIO 10 - CREACIÓN
siglo=dict({"siglo":"100 años"})
print("10. El diccionario creado es:",siglo)

print("\n==============================   2.PERTENENCIA DE CLAVE   ===================================\n")

#EJERCICIO 01 - PERTENENCIA DE CLAVE
datos={"nombre":"leonardo","edad":19,"curso":"python"}
print("1.  nombre pertenece al diccionario:","nombre" in datos)

#EJERCICIO 02 - PERTENENCIA DE CLAVE
meses={"enero":"primer mes","febrero":"segundo mes","marzo":"tercer mes","abril":"cuarto mes"}
print("2.  febrero pertenece al diccionario:","febrero" in meses)

#EJERCICIO 03 - PERTENENCIA DE CLAVE
estaciones={"verano":"calor","invierno":"frio","otoño":"se caen las hojas","primavera":"florecen las plantas"}
print("3.  verano pertenece al diccionario:","verano" in estaciones)

#EJERCICIO 04 - PERTENENCIA DE CLAVE
estados={"solido":"hielo","liquido":"agua","gaseoso":"vapor"}
print("4.  cafe pertenece al diccionario:","cafe" in estados)

#EJERCICIO 05 - PERTENENCIA DE CLAVE
diccionario={"animal":"perro","fruta":"mandarina","verdura":"lechuga"}
print("5.  naranja pertenece al diccionario:","naranja" in diccionario)

#EJERCICIO 06 - PERTENENCIA DE CLAVE
sistema={"estrella":"sol","astro":"luna","planeta":"tierra"}
print("6.  marte no pertenece al diccionario:","marte" not in sistema)

#EJERCICIO 07 - PERTENENCIA DE CLAVE
paises={"peru":"america","francia":"europa","india":"asia","marruecos":"africa"}
print("7.  peru no pertenece al diccionario:","peru" not in paises)

#EJERCICIO 08 - PERTENENCIA DE CLAVE
regiones={"lambayeque":"costa","cajamarca":"sierra","loreto":"selva"}
print("8.  cusco no pertenece al diccionario:","cusco" not in regiones)

#EJERCICIO 09 - PERTENENCIA DE CLAVE
utiles={"lapiz":"escribir","pinturas":"pintar","borrador":"borrar"}
print("9.  pincel no pertenece al diccionario:","pincel" not in utiles)

#EJERCICIO 10 - PERTENENCIA DE CLAVE
progra={"hola":"mundo"}
print("10. python no pertenece al diccionario:","python" not in progra)

print("\n==============================   3.COCATENACIÓN   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO SE CONCATENAN  **")

print("\n==============================   4.COMPARACIÓN   ===================================\n")

#EJERCICIO 01 - COMPARACIÓN
fruit={"manzana":"rojo","sandia":"verde"}
color={"rojo":"manzana","verde":"sandia"}
print("1.  los diccionarios son iguales:",fruit==color)

#EJERCICIO 02 - COMPARACIÓN
velocidad={"rapido":"tren","lento":"tortuga"}
vel={"rapido":"tren","lento":"tortuga"}
print("2.  los diccionarios son iguales:",velocidad==vel)

#EJERCICIO 03 - COMPARACIÓN
facultad={"facfym":"electronica","ficsa":"civil"}
fac={"facfym":"estadistica","ficsa":"sistemas"}
print("3.  los diccionarios son iguals:",facultad==fac)

#EJERCICIO 04 - COMPARACIÓN
frutas={"piña":"dulce","limon":"agrio"}
frut={"piña":"dulce","limon":"agrio"}
print("4.  los diccionarios son iguales:",frutas==frut)

#EJERCICIO 05 - COMPARACIÓN
numeros={"uno":1,"dos":2,"tres":3}
nro={1:"uno",2:"dos",3:"tres"}
print("5.  los diccionarios son iguales:",numeros==nro)

#EJERCICIO 06 - COMPARACIÓN
bebidas={"gaseosa":"botella de plastico","cerveza":"lata","vino":"botella de vidrio"}
bebidas_1={"gaseosa":"botella de plastico","cerveza":"lata","vino":"botella de vidrio"}
print("6.  los diccionarios son diferentes:",bebidas!=bebidas_1)

#EJERCICIO 07 - COMPARACIÓN
aula={"pizarra":"blanca","sillas":"marronas","puerta":"granate"}
aula_2={"pizarra":"blanca","sillas":"grises","puerta":"azul"}
print("7.  los diccionarios son diferentes:",aula!=aula_2)

#EJERCICIO 08 - COMPARACIÓN
obj={"lapiz":"carbon","lapicero":"tinta"}
obj_1={"lapiz":"carbon","lapicero":"tinta"}
print("8.  los diccionarios son diferentes:",obj!=obj_1)

#EJERCICIO 09 - COMPARACIÓN
progra={"curso":"programacion II","tema":"diccionarios"}
progra_1={"curso":"programacion II","tema":"funciones"}
print("9. los diccionarios son diferentes:",progra!=progra_1)

#EJERCICIO 10 - COMPARACIÓN
agua={"oceano":"pacifico","rio":"amazonas","lago":"titicaca"}
agua_1={"oceano":"pacifico","rio":"amazonas","lago":"titicaca"}
print("10. los diccionaros son diferentes:",agua!=agua_1)

print("\n==============================   5.INDEXACIÓN   ===================================\n")

#EJERCICIO 01 - INDEXACIÓN
sentidos={"olfato":"nariz","vista":"ojo","audicion":"oido"}
print("1.  el valor de vista es:",sentidos["vista"])

#EJERCICIO 02 - INDEXACIÓN
playa={"roca":"arena","muelle":"madera"}
print("2.  el valor de muelle es:",playa["muelle"])

#EJERCICIO 03 - INDEXACIÓN
nros={"uno":1,"diez":10,"cien":100}
print("3.  el valor de cien es:",nros["cien"])

#EJERCICIO 04 - INDEXACIÓN
deporte={"basquet":"canasta","futbol":"arco"}
print("4.  el valor de basquet es:",deporte["basquet"])

#EJERCICIO 05 - INDEXACIÓN
extensiones={"mp3":"audio","png":"imagen","mp4":"video"}
print("5.  el valor de mp3 es:",extensiones["mp3"])

#EJERCICIO 06 - INDEXACIÓN
operaciones={"+":"suma","-":"resta","*":"multiplicacion","/":"division"}
print("6.  el valor de - es:",operaciones["-"])

#EJERCICIO 07 - INDEXACIÓN
nave={"auto":"ruedas","avio":"alas"}
print("7.  el valor de auto es:",nave["auto"])

#EJERCICIO 08 - INDEXACIÓN
dulces={"rellenita":"galleta","pepsi":"gaseosa"}
print("8. el valor de pepsi es:",dulces["pepsi"])

#EJERCICIO 09 - INDEXACIÓN
cel={"celular":"motorola","laptop":"acer"}
print("9.  el valor de celular es:",cel["celular"])

#EJERCICIO 10 - INDEXACIÓN
productos={"oro":"mineral","cafe":"bebida"}
print("10. el valor de oro:",productos["oro"])

print("\n==============================   6.CORTADO   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO PERMITEN EL SLICE  **")

print("\n==============================   7.LONGITUD   ===================================\n")

#EJERCICIO 01 - LONGITUD
meses={"enero":1,"febrero":2,"marzo":3,"abril":4,"junio":5}
print("1.  el nro de elementos del diccionario es:",len(meses))

#EJERCICIO 02 - LONGITUD
vacio=dict()
print("2.  el nro de elementos del diccionario es:",len(vacio))

#EJERCICIO 03 - LONGITUD
frutas={"mandarina":"anaranjado","platano":"amarillo"}
print("3.  el nro de elementos del diccionario es:",len(frutas))

#EJERCICIO 04 - LONGITUD
sabores={"picante":"aji","dulce":"miel","salado":"sal"}
print("4.  el nro de elementos del diccionario es:",len(sabores))

#EJERCICIO 05 - LONGITUD
animal={"caballo":"animal"}
print("5.  el nro de elementos del diccionario es:",len(animal))

#EJERCICIO 06 - LONGITUD
rom={"X":10,"V":5,"III":3,"I":1}
print("6.  el nro de elementos del diccionario es:",len(rom))

#EJERCICIO 07 - LONGITUD
tipo={"leon":"salvaje","pavo":"domestico"}
print("7.  el nro de elementos del diccionario es:",len(tipo))

#EJERCICIO 08 - LONGITUD
continentes={"africa":"nigeria","america":"peru","oceania":"australia"}
print("8.  el nro de elementos del diccionario es:",len(continentes))

#EJERCICIO 09 - LONGITUD
colors={"rojo":1,"amarillo":2,"azul":3,"azul":4,"verde":5,"verde":6}
print("9.  el nro de elementos del diccionario es:",len(colors))

#EJERCICIO 10 - LONGITUD
medidas={"longitud":"metro","masa":"kilogramo","peso":"newton"}
print("10. el nro de elementos del diccionario es:",len(medidas))

print("\n==============================   8.ITERACIÓN   ===================================\n")

#EJERCICIO 01 - ITERACIÓN
productos={"vaca":"leche","oveja":"lana","gallina":"huevos"}
print("1.")
for i in productos:
    print(i)

#EJERCICIO 02 - ITERACIÓN
cosas={"linterna":"alumbrarse","celular":"comunicarse"}
print("2.")
for i in cosas:
    print(i)

#EJERCICIO 03 - ITERACIÓN
animal={"leon":"sabana","tiburon":"mar","anaconda":"selva"}
print("3.")
for i in animal:
    print(i)

#EJERCICIO 04 - ITERACIÓN
etapas={"adolescente":"pepe","joven":"ramon","adulto":"julio"}
print("4.")
for i in etapas:
    print(i)

#EJERCICIO 05 - ITERACIÓN
insectos={"hormiga":"camina","mariposa":"vuela"}
print("5.")
for i in insectos:
    print(insectos[i])

#EJERCICIO 06 - ITERACIÓN
transporte={"tren":"tierra","avion":"aire","barco":"mar"}
print("6.")
for i in transporte:
    print(transporte[i])

#EJERCICIO 07 - ITERACIÓN
cadena={"herbivoro":"cuy","carnivoro":"tigre","carroñero":"hiena"}
print("7.")
for i in cadena:
    print(cadena[i])

#EJERCICIO 08 - ITERACIÓN
carreras={"electronica":"facfym","arquitectura":"ficsa","comercio":"faceac"}
print("8.")
for i,j in carreras.items():
    print(i,j)
#EJERCICIO 09 - ITERACIÓN
unis={"UNPRG":"Lambayeque","UNT":"La libertad","UNMSM":"Lima"}
print("9.")
for i,j in unis.items():
    print(i,j)

#EJERCICIO 10 - ITERACIÓN
estacion={"verano":"calor","invierno":"frio"}
print("10.")
for i,j in estacion.items():
    print(i,j)

print("\n==============================   9.BÚSQUEDA   ===================================\n")

#EJERCICIO 01 - BÚSQUEDA
boleano={"verdadero":True,"falso":False}
print("1.  el valor de verdadero es:",boleano.get("verdadero"))

#EJERCICIO 02 - BÚSQUEDA
longitud={"alto":"palmera","bajo":"cesped"}
print("2.  el valor de alto es:",longitud.get("alto"))

#EJERCICIO 03 - BÚSQUEDA
alumno={"nombre":"leonardo","apellido":"huaman","dni":"75864213"}
print("3.  el valor de dni es:",alumno.get("dni"))

#EJERCICIO 04 - BÚSQUEDA
musica={"Balada":"camila","regeton":"ozuna","electro":"avicii"}
print("4.  el valor de electro:", musica.get("electro"))

#EJERCICIO 05 - BÚSQUEDA
comidas={"costa":"ceviche","sierra":"cuy con papas","selva":"juane"}
print("5. el valor de sierra:",comidas.get("sierra"))

#EJERCICIO 06 - BÚSQUEDA
ocupaciones={"profesor":"educa","policia":"seguridad","modelo":"modela"}
print("6.  el valor de profesor es:",ocupaciones.get("profesor"))

#EJERCICIO 07 - BÚSQUEDA
uni={"UNPRG":"Peru"}
print("7.  el valor de UNPRG es:",uni.get("UNPRG"))

#EJERCICIO 08 - BÚSQUEDA
marcas={"auto":"Honda","ropa":"gucci","telefono":"motorola"}
print("8.  el valor de auto es:",marcas.get("auto"))

#EJERCICIO 09 - BÚSQUEDA
cursos={"matematicas":"ingenierias","poesia":"literatura","leyes":"derecho"}
print("9.  el valor de poesia es:",cursos.get("poesia"))

#EJERCICIO 10 - BÚSQUEDA
redes={"facebook":"historias","instagram":"fotos","whatsapp":"mensajes"}
print("10. el valor de instagram es:",redes.get("instagram"))

print("\n==============================   10.CONTEO   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO TRAEN EL METODO COUNT  **")

print("\n==============================   11.MAXIMOS/MINIMOS   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO TRAEN EL METODO MAX/MIN  **")

print("\n==============================   12.MULTIPLICACIÓN   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO SOPORTAN LA MULTIPLICACION  **")

print("\n==============================   13.ELIMINACIÓN   ===================================\n")

#EJERCICIO 01 - ELIMINACIÓN
nros={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco"}
del nros[3]
print("1. ",nros)

#EJERCICIO 02 - ELIMINACIÓN
estaciones={"verano":"calor","invierno":"frio","otoño":"se caen las hojas","primavera":"florecen las plantas"}
del estaciones["otoño"]
print("2. ",estaciones)

#EJERCICIO 03 - ELIMINACIÓN
velocidad={"rapido":"tren","lento":"tortuga"}
del velocidad["lento"]
print("3. ",velocidad)

#EJERCICIO 04 - ELIMINACIÓN
sentidos={"olfato":"nariz","vista":"ojo","audicion":"oido"}
del sentidos["vista"]
print("4. ",sentidos)

#EJERCICIO 05 - ELIMINACIÓN
playa={"roca":"arena","muelle":"madera"}
del playa["roca"]
print("5. ",playa)

#EJERCICIO 06 - ELIMINACIÓN
agua={"oceano":"pacifico","rio":"amazonas","lago":"titicaca"}
del agua
print("6.  variable eliminada")

#EJERCICIO 07 - ELIMINACIÓN
obj={"lapiz":"carbon","lapicero":"tinta"}
del obj
print("7.  variable eliminada")

#EJERCICIO 08 - ELIMINACIÓN
aula={"pizarra":"blanca","sillas":"marronas","puerta":"granate"}
del aula
print("8.  variable eliminada")

#EJERCICIO 09 - ELIMINACIÓN
numeros={"uno":1,"dos":2,"tres":3}
del numeros
print("9.  variable eliminada")

#EJERCICIO 10 - ELIMINACIÓN
frutas={"piña":"dulce","limon":"agrio"}
del frutas
print("10. variable eliminada")

print("\n==============================   14.REEMPLAZO   ===================================\n")

#EJERCICIO 01 - REEMPLAZO
cuaderno=dict(cuaderno="escribir",programa="python")
cuaderno["cuaderno"]="leer"
cuaderno["programa"]="C"
print("1. ",cuaderno)

#EJERCICIO 02 - REEMPLAZO
romanos=dict({"I":"uno","V":"cinco","X":"diez"})
romanos["I"]=1
romanos["V"]=5
print("2. ",romanos)

#EJERCICIO 03 - REEMPLAZO
tiempo=dict(dia="24 horas",hora="60 minutos",minuto="60 segundos")
tiempo["dia"]="noche"
tiempo["hora"]="siglo"
print("3. ",tiempo)

#EJERCICIO 04 - REEMPLAZO
dia={"dia":"sol","noche":"luna"}
dia["dia"]="semana"
dia["noche"]="estrellas"
print("4. ",dia)

#EJERCICIO 05 - REEMPLAZO
animales=dict(insecto="hormiga",ave="aguila",reptil="iguana")
animales["insecto"]="caracol"
animales["ave"]="gallina"
print("5. ",animales)

#EJERCICIO 06 - REEMPLAZO
datos={"nombre":"leonardo","edad":19,"curso":"python"}
datos["nombre"]="lucio"
datos["edad"]=50
print("6. ",datos)

#EJERCICIO 07 - REEMPLAZO
meses={"enero":"primer mes","febrero":"segundo mes","marzo":"tercer mes","abril":"cuarto mes"}
meses["enero"]=1
meses["febrero"]=2
meses["marzo"]=3
print("7. ",meses)

#EJERCICIO 08 - REEMPLAZO
estados={"solido":"hielo","liquido":"agua","gaseoso":"vapor"}
estados["solido"]="cafe"
estados["liquido"]="gaseosa"
print("8. ",estados)

#EJERCICIO 09 - REEMPLAZO
diccionario={"animal":"perro","fruta":"mandarina","verdura":"lechuga"}
diccionario["animal"]="oso"
diccionario["fruta"]="uva"
print("9. ",diccionario)

#EJERCICIO 10 - REEMPLAZO
sistema={"estrella":"sol","astro":"luna","planeta":"tierra"}
sistema["estrella"]="pluton"
sistema["planeta"]="marte"
print("10.",sistema)

print("\n==============================   15.AGREGADO   ===================================\n")

#EJERCICIO 01 - AGREGADO
paises={"peru":"america","francia":"europa","india":"asia","marruecos":"africa"}
paises.setdefault("nueva zelanda","oceania")
print("1. ",paises)

#EJERCICIO 02 - AGREGADO
regiones={"lambayeque":"costa","cajamarca":"sierra","loreto":"selva"}
regiones.setdefault("tumbes","manglares")
print("2. ",regiones)

#EJERCICIO 03 - AGREGADO
utiles={"lapiz":"escribir","pinturas":"pintar","borrador":"borrar"}
utiles.setdefault("tempera","pintar")
print("3. ",utiles)

#EJERCICIO 04 - AGREGADO
progra={"hola":"mundo"}
progra.setdefault("primer","programa")
print("4. ",progra)

#EJERCICIO 05 - AGREGADO
fruit={"manzana":"rojo","sandia":"verde"}
fruit.setdefault("amarillo","platano")
print("5. ",fruit)

#EJERCICIO 06 - AGREGADO
velocidad={"rapido":"tren","lento":"tortuga"}
velocidad.setdefault("normal","bicicleta")
print("6. ",velocidad)

#EJERCICIO 07 - AGREGADO
facultad={"facfym":"electronica","ficsa":"civil"}
facultad.setdefault("fiquia","quimica")
print("7. ",facultad)

#EJERCICIO 08 - AGREGADO
frutas={"piña":"dulce","limon":"agrio"}
frutas.setdefault("mango","dulce")
print("8. ",frutas)

#EJERCICIO 09 - AGREGADO
numeros={"uno":1,"dos":2,"tres":3}
numeros.setdefault("cincuenta",50)
print("9. ",numeros)

#EJERCICIO 10 - AGREGADO
aula={"pizarra":"blanca","sillas":"marronas","puerta":"granate"}
aula.setdefault("ventana","vieja")
print("10.",aula)

print("\n==============================   16.ANULACION   ===================================\n")

#EJERCICIO 01 - ANULACION
obj={"lapiz":"carbon","lapicero":"tinta"}
obj.clear()
print("1. ",obj)

#EJERCICIO 02 - ANULACION
progra={"curso":"programacion II","tema":"diccionarios"}
progra.clear()
print("2. ",progra)

#EJERCICIO 03 - ANULACION
agua={"oceano":"pacifico","rio":"amazonas","lago":"titicaca"}
agua.clear()
print("3. ",agua)

#EJERCICIO 04 - ANULACION
sentidos={"olfato":"nariz","vista":"ojo","audicion":"oido"}
sentidos.clear()
print("4. ",sentidos)

#EJERCICIO 05 - ANULACION
playa={"roca":"arena","muelle":"madera"}
playa.clear()
print("5. ",playa)

#EJERCICIO 06 - ANULACION
nros={"uno":1,"diez":10,"cien":100}
nros.clear()
print("6. ",nros)

#EJERCICIO 07 - ANULACION
deporte={"basquet":"canasta","futbol":"arco"}
deporte.clear()
print("7. ",deporte)

#EJERCICIO 08 - ANULACION
extensiones={"mp3":"audio","png":"imagen","mp4":"video"}
extensiones.clear()
print("8. ",extensiones)

#EJERCICIO 09 - ANULACION
operaciones={"+":"suma","-":"resta","*":"multiplicacion","/":"division"}
operaciones.clear()
print("9. ",operaciones)

#EJERCICIO 10 - ANULACION
nave={"auto":"ruedas","avio":"alas"}
nave.clear()
print("10.",nave)

print("\n==============================   17.CLONADO   ===================================\n")

#EJERCICIO 01 - CLONADO
dulces={"rellenita":"galleta","pepsi":"gaseosa"}
copia_dulces=dulces.copy()
print("1.  la copia del diccionario es:",copia_dulces)

#EJERCICIO 02 - CLONADO
cel={"celular":"motorola","laptop":"acer"}
copia_cel=cel.copy()
print("2.  la copia del diccionario es:",copia_cel)

#EJERCICIO 03 - CLONADO
productos={"oro":"mineral","cafe":"bebida"}
copia_productos=productos.copy()
print("3.  la copia del diccionario es:",copia_productos)

#EJERCICIO 04 - CLONADO
meses={"enero":1,"febrero":2,"marzo":3,"abril":4,"junio":5}
copia_meses=meses.copy()
print("4.  la copia del diccionario es:",copia_meses)

#EJERCICIO 05 - CLONADO
frutas={"mandarina":"anaranjado","platano":"amarillo"}
copia_frutas=frutas.copy()
print("5.  la copia del diccionario es:",copia_frutas)

#EJERCICIO 06 - CLONADO
sabores={"picante":"aji","dulce":"miel","salado":"sal"}
copia_sabores=sabores.copy()
print("6.  la copia del diccionario es:",copia_sabores)

#EJERCICIO 07 - CLONADO
rom={"X":10,"V":5,"III":3,"I":1}
copia_rom=rom.copy()
print("7.  la copia del diccionario es:",copia_rom)

#EJERCICIO 08 - CLONADO
tipo={"leon":"salvaje","pavo":"domestico"}
copia_tipo=tipo.copy()
print("8.  la copia del diccionario es:",copia_tipo)

#EJERCICIO 09 - CLONADO
continentes={"africa":"nigeria","america":"peru","oceania":"australia"}
copia_continentes=continentes.copy()
print("9.  la copia del diccionario es:",copia_continentes)

#EJERCICIO 10 - CLONADO
colors={"rojo":1,"amarillo":2,"azul":3,"azul":4,"verde":5,"verde":6}
copia_colors=colors.copy()
print("10. la copia del diccionario es:",copia_colors)

input("press enter to continue.....")
print("\n==============================   18.EXTENSIÓN   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO TRAEN EL METODO EXTEND  **")

print("\n==============================   19.INSERCIÓN   ===================================\n")

#EJERCICIO 01 - INSERCIÓN
#EJERCICIO 02 - INSERCIÓN
#EJERCICIO 03 - INSERCIÓN
#EJERCICIO 04 - INSERCIÓN
#EJERCICIO 05 - INSERCIÓN
#EJERCICIO 06 - INSERCIÓN
#EJERCICIO 07 - INSERCIÓN
#EJERCICIO 08 - INSERCIÓN
#EJERCICIO 09 - INSERCIÓN
#EJERCICIO 10 - INSERCIÓN

print("\n==============================   20.EXTRACCIÓN   ===================================\n")

#EJERCICIO 01 - EXTRACCIÓN
#EJERCICIO 02 - EXTRACCIÓN
#EJERCICIO 03 - EXTRACCIÓN
#EJERCICIO 04 - EXTRACCIÓN
#EJERCICIO 05 - EXTRACCIÓN
#EJERCICIO 06 - EXTRACCIÓN
#EJERCICIO 07 - EXTRACCIÓN
#EJERCICIO 08 - EXTRACCIÓN
#EJERCICIO 09 - EXTRACCIÓN
#EJERCICIO 10 - EXTRACCIÓN

print("\n==============================   21.SEPARACIÓN   ===================================\n")

print("**  NO SOPORTADO - LOS DICCIONARIOS NO TRAEN EL METODO REMOVE  **")

print("\n==============================   22.REVERSA   ===================================\n")

print("**  NO SOPORTADO - NO SOPORTADO EN LA VERSION 3.7  **")

print("\n==============================   23.ORDENADO   ===================================\n")

print("**  NO ES NECESARIO - LOS DICCIONARIOS SON ORDENADOS POR DISEÑO  **")

print("\n==============================   24.VER CLAVES   ===================================\n")

#EJERCICIO 01 - VER CLAVES
#EJERCICIO 02 - VER CLAVES
#EJERCICIO 03 - VER CLAVES
#EJERCICIO 04 - VER CLAVES
#EJERCICIO 05 - VER CLAVES
#EJERCICIO 06 - VER CLAVES
#EJERCICIO 07 - VER CLAVES
#EJERCICIO 08 - VER CLAVES
#EJERCICIO 09 - VER CLAVES
#EJERCICIO 10 - VER CLAVES

print("\n==============================   25.VER VALORES   ===================================\n")

#EJERCICIO 01 - VER VALORES
#EJERCICIO 02 - VER VALORES
#EJERCICIO 03 - VER VALORES
#EJERCICIO 04 - VER VALORES
#EJERCICIO 05 - VER VALORES
#EJERCICIO 06 - VER VALORES
#EJERCICIO 07 - VER VALORES
#EJERCICIO 08 - VER VALORES
#EJERCICIO 09 - VER VALORES
#EJERCICIO 10 - VER VALORES

print("\n==============================   26.CONVERSIÓN   ===================================\n")

#EJERCICIO 01 - CONVERSIÓN
#EJERCICIO 02 - CONVERSIÓN
#EJERCICIO 03 - CONVERSIÓN
#EJERCICIO 04 - CONVERSIÓN
#EJERCICIO 05 - CONVERSIÓN
#EJERCICIO 06 - CONVERSIÓN
#EJERCICIO 07 - CONVERSIÓN
#EJERCICIO 08 - CONVERSIÓN
#EJERCICIO 09 - CONVERSIÓN
#EJERCICIO 10 - CONVERSIÓN
