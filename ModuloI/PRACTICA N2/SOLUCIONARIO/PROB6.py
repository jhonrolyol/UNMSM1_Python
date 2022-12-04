#Ejercicio extra:
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo. Para la función llamada “Login”, este recibirá un nombre de usuario y una contraseña y devolverá Verdadero si el nombre de usuario es (ejemplo: “usuario1” y la contraseña es “asdasd”). Además, recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

print('****** VENTANA DE ACCESO AL SISTEMA ******')
print('Bienvenido a la ventana de inicio de acceso al sistema')

def Login(user,password,attemps):
	attemps += 1
	if user == "usuario1" and password == "asdasd":
		return(True,attemps)
	else:
		return(False,attemps)

intentos = 0
while True:
	usuario = input("Ingrese su usuario:")
	clave = input("Ingrese su contraseña:")
	entrar,intentos = Login(usuario,clave,intentos)
	if not entrar:
		print("*** Error. Nombre de usuario o contraseña incorrecta.*** \n***Por favor, revise bien los datos ingresados.***")
	if entrar or intentos == 3: 
		break

if entrar:
	print("====== BIENVENIDO AL SISTEMA ======")
else: # Sale el mensaje si es que intentos llega a 3
	print("XXXXX ACCESO INVÁLIDO, NO SE PUEDE ACCEDER AL SISTEMA XXXXX")