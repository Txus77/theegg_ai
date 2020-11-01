# Simular redes informáticas con packet tracer

Se trata de simular las siguientes redes en Packet Tracer

a.- Red con servidor web y servidor de DNS
b.- Red con servidor DHCP
c.- Red VLAN básica
d.- Unir dos redes VLAN con un router
e.- Enrutamiento estático

## Solución

La solución se ha realizado con Packet tracer 7.2
Se plantea una solución que engloba todas los tipos de redes que se quieren obtener. Así en el mismo archivo están todas las redes que se piden.
La topología planteada consta de 2 routers, un servidor WEB, un servidor DHCP, un servidor DNS, 3 switch y 10 Host. 
En un router están conectados el servidor DHCP y el servidor DNS.
En el otro router se ha conectado el servidor WEB y 2 switch que dan acceso a las diferentes Vlan.
Respecto a las Vlan planteadas se ha realizado con 2 topologías diferentes: 

- En una de las topologías planteadas las 3 Vlan comparten un Switch que a su vez está conectado al router compartiendo las 3 el mismo interfaz fisico.

- En la otra topología hay 2 switch y 2 Vlan de forma que los Host de cada Vlan están repartidos 2 y 2 en los 2 switch, es decir, a cada Vlan le pertenecen 2 Host de los 4 conecatados a cada switch. Estas Vlan también comparten un de los interfaces físicos del router.

A continuación se pasa a detallar las configuraciones planteadas:

### Configuración DNS

!Desktop

	IP address 10.1.50.2
	Subnet Mask 255.255.255.0
	Default Gateway 10.1.50.1
	DNS Server 0.0.0.0

!Services

DNS Service On

!Resource Records

Name www.conseguido.es 	!es el nombre que queremos que se relaciones con la IP que indiquemos

Type A record

Address 192.168.1.2 	!Se pone la IP del servidor WEB cuya pagina queremos que muuestre al poner el nombre www.conseguido.es

pulsamos ADD para añadir y Save para guardar

### configuración servidor WEB

!Desktop

	IP address 192.168.1.2
	Subnet Mask 255.255.255.0
	Default Gateway 192.168.1.1
	DNS Server 0.0.0.0

!Services

	HTTP On
	HTTPS On

!Se pueden cambiar los mensajes que saldrán cuando desde un host accedamos a esa dirección editándolos y guardandolos.

### Configurar Routers

#### Router1

!En la configuarción fisica se añaden las interfaces que se prevea necesitar. En este caso se ha añadido NM2FE2W y WIT-2T con el objeto de añadirle interfaces fastEthernet e interfaces serial

!A este router van el servidor web y todas las redes con Host. Todos estos dispositivos se conectan al router por medio de las interfaces FastEthernet. Además, se ha conectado a otro router que es donde se encuntran conectados el servidor DHCP y el servidor DNS

!A continuación se describe la configuración de las diferentes interfaces en uso:

!Entramos en modo configuración del router

!Interface fastEthernet 0/0 (A través de esta interface se conecta dos redes de 4 PCs cada una dispuetos de 2 en 2 en switch diferentes, es decir, 2 PCs conectados al primer switch y 2 PCs del segundo switch pertenecen a la misma red)

  ##### Configurar VLANs con Host en 2 switch diferentes
  
	!Primero configuramos los dos switch igual:
	
	vlan 2
	name BASICA1
	exit
 
	vlan 3
	name BASICA2
	exit

	!Asignación de puertos a la red BASICA1

	interface fastEthernet 0/1
	switchport access vlan 2
	exit
 
	interface fastEthernet 0/2
	switchport access vlan 2
	exit

	!Asignación de puertos a la red BASICA2 

	interface fastEthernet 0/3
	switchport access vlan 3
	exit
 
	interface fastEthernet 0/4
	switchport access vlan 3
	exit
	 
  	!En el switch que se conecta al servidor el interface lo ponemos en modo trunk
	interface fastEthernet 0/5
	switchport mode trunk

	!se hace lo mismo en el interface del segundo switch donde se conecta el cable que une ambos switch
	interface fastEthernet 0/24
	switchport mode trunk

##### Configurar Interface fastEthernet 0/0

!Configuración la interface del  Router donde se conecta el switch. En este caso el puerto fastEthernet 0/0 lo van a compartir las 2 subredes

	!Entramos en el modo configuración del router

	interface fastEthernet 0/0.1 
	encapsulation dot1Q 2                 !así se añade una etiqueta a en la trama ethernet para diferenciar de que vlan provienen los datos
	ip address 172.16.1.1 255.255.255.0   !establecemos una puerta de enlace para esta subred. 
	exit
 
	interface fastEthernet 0/0.2
	encapsulation dot1Q 3
	ip address 172.16.2.1 255.255.255.0
	exit

	!Al querer que todos los PCs tengan IP dinamica y al estar el servidor DHCP en otra red hay que recurrir al comando ip helper-address en cada subred:
	interface fastEthernet 0/0.1
	ip helper-address 174.32.1.2
	exit

	interface fastEthernet 0/0.2
	ip helper-address 174.32.1.2
	exit

##### Configurar Interface fastEthernet 1/0

!Interface fastEthernet 1/0 (A través de esta interface se conecta el servidor WEB)

	Interface fastEthernet 1/0
	IP address 192.168.1.1
	Subnet Mask 255.255.0.0
	no shutdown
	exit

!Interface fastEthernet 1/1 (A través de esta interface se conecta 3 subredes, de 2 PCs cada una, que están conectadas a un switch)

  ##### Configurar VLANs que comparten switch
  
	!Primero configuramos el switch

	vlan 2
	name RED1
	exit
 
	vlan 3
	name RED2
	exit
 
	vlan 4
	name RED3
	exit

	!Asignación de puertos a la RED1

	interface fastEthernet 0/1
	switchport access vlan 2
	exit
 
	interface fastEthernet 0/2
	switchport access vlan 2
	exit

	!Asignación de puertos a la RED2

	interface fastEthernet 0/3
	switchport access vlan 3
	exit
 
	interface fastEthernet 0/4
	switchport access vlan 3
	exit

	!Asignación de puertos a la RED3

	interface fastEthernet 0/4
	switchport access vlan 4
	exit
 
	interface fastEthernet 0/5
	switchport access vlan 4
	exit

	!Puerto 24 en modo trunk ya que es el puerto que conecta con el router y así se permite que las subredes conecten entre ellas y puedan compartir la misma interface del router

	interface fastEthernet 0/24
	switchport mode trunk
	exit

##### Configurar Interface fastEthernet 1/1

!Configuración la interface del  Router donde se conecta el switch. En este caso el puerto fastEthernet 1/1 lo van a compartir las 3 subredes

	!Entramos en el modo configuración del router

	interface fastEthernet 1/1.1 
	encapsulation dot1Q 2                   !así se añade una etiqueta a en la trama ethernet para diferenciar de que vlan provienen los datos
	ip address 100.100.1.1 255.255.255.0    !establecemos una puerta de enlace para esta subred. 
	exit
 
	interface fastEthernet 1/1.2
	encapsulation dot1Q 3
	ip address 100.100.2.1 255.255.255.0
	exit
 
	interface fastEthernet 1/1.3
	encapsulation dot1Q 4
	ip address 100.100.3.1 255.255.255.0
	exit

	!Al querer que todos los PCs tengan IP dinamica y al estar el servidor DHCP en otra red hay que recurrir nuevamente al comando ip helper-address en cada subred:
	interface fastEthernet 1/1.1
	ip helper-address 174.32.1.2
	exit

	interface fastEthernet 1/1.2
	ip helper-address 174.32.1.2
	exit

	interface fastEthernet 1/1.3
	ip helper-address 174.32.1.2
	exit

##### Configurar Interface Serial 0/0

!configuramos el puertos serial 0/0 que es que conecta con el Router2

	interface serial0/0
	IP address 200.33.1.1
	Subnet Mask 255.255.255.0
	no keepalive 			!El keepalivecomando especifica el intervalo (en seconds) que el enrutador espera antes de enviar un mensaje en la interfaz para probar el enlace y determinar si está activo o inactivo. En las interfaces Ethernet, el enrutador se envía el mensaje a sí mismo. En las interfaces seriales, el mensaje se envía al enrutador en el otro extremo del enlace.La configuración de Keepalive puede ser muy sensible. Si el intervalo keepalive es demasiado bajo, los paquetes keepalive pueden verse retrasados por otro tráfico. Si el intervalo es demasiado alto, el enrutador tardará más en actualizar el estado de la interfaz, lo que ralentiza la convergencia de rutas
	no shutdown
	exit

##### Enrutamiento

!por último creamos la tabla de enrutamiento

	ip router 10.1.50.0 255.255.255.0 200.33.1.2
	ip router 174.32.1.0 255.255.255.0 200.33.1.2

#### Router 2

!configuramos el Router2. En este router van conectados el servidor DNS y el servidor DHCP

!como en el Router1 en el apartado de configuración fisica añadimos las interfaces que necesitemos. En este caso han sido las mismas que en el Router1

!configuramos el interface fastEthernet 0/0 que es donde va conectado el servidor DNS

!entramos en modo de configuración del router

##### Configurar Interface FastEthernet 0/0

	interface fastEthernet 0/0
	IP address 10.1.50.1
	Subnet Mask 255.255.0.0
	exit

##### Configurar Interface FastEthernet 1/0

!configuramos interface fastEthernet 1/0 que es donde está conectado el servidor DHCP

	interface fastEthernet 1/0
	IP address 174.32.1.1
	Subnet Mask 255.255.255.0
	exit

##### Configurar Interface Serial 0/0

!configuramos el interface serial 0/0 que va conectado al otro Router

	IP address 200.33.1.2
	Subnet Mask 255.255.255.0
	clock rate 56000 		        !establece la velocidad de transmisión
	no keepalive 
	no shutdown 
	exit

##### Enrutamiento

!Por último creamos la tabla de enrutamiento

	ip router 192.168.1.0 255.255.255.0 200.33.1.1
	ip router 172.16.1.0 255.255.255.0 200.33.1.1
	ip router 172.16.2.0 255.255.255.0 200.33.1.1
	ip router 100.100.1.0 255.255.0.0 200.33.1.1
	ip router 100.100.2.0 255.255.0.0 200.33.1.1
	ip router 100.100.3.0 255.255.0.0 200.33.1.1

### configuración DHCP

	!Desktop

	IP address 174.32.1.2
	Subnet Mask 255.255.255.0
	Default Gateway 174.32.1.1

!Services

	Service On

	Pool Name ServerPool            !por cada red a la que queramos asignar IP a sus Host hay que poner configurar un Pool diferente con los datos correspondientes
	Default Gateway 172.16.1.1      !puerta de enlace que se asignará por defecto a cada Host
	DNS server 10.1.50.2            !DNS que se asignará por defecto a cada Host
	Start IP address 172.16.1.100   !IP por la que se empezará a asignar a cada Host
	Subnet Mask 255.255.255.0       !mascara de subred que se aisgnará!
	Maxinum Number of Users: 8      !número maximo de host a los que se aignará IP!

!todo lo anterior se tiene que configurar en cada Pool para cada red en la que se quiera asignar IP a sus Host

!Las siguientes son las configuraciones de los Pool para las Vlan 2, Vlan 3 y Vlan 4 que están conectadas al Switch_subredes. Estas comparten el Interfaz fastEthernet 1/1 del Router1.

	Pool Name ServerPool1
	Default Gateway 100.100.1.1 
	DNS server 10.1.50.2 
	Start IP address 100.100.1.100 
	Subnet Mask 255.255.255.0 
	Maxinum Number of Users: 8

	Pool Name ServerPool2
	Default Gateway 100.100.2.1 
	DNS server 10.1.50.2 
	Start IP address 100.100.2.100 
	Subnet Mask 255.255.255.0 
	Maxinum Number of Users: 8

	Pool Name ServerPool3
	Default Gateway 100.100.1.1 
	DNS server 10.1.50.2 
	Start IP address 100.100.1.100 
	Subnet Mask 255.255.255.0 
	Maxinum Number of Users: 8

	Pool Name ServerPool4
	Default Gateway 172.16.2.1 
	DNS server 10.1.50.2 
	Start IP address 172.16.2.100 
	Subnet Mask 255.255.255.0 
	Maxinum Number of Users: 8
