from selenium.webdriver.common.by import By
from selenium import webdriver
import basecon as bdd
base=bdd.conexion()
Busqueda = input("Ingrese el nombre de un eléctrodomestico:")
driver = webdriver.Chrome()
driver.get("https://www.almaceneslaganga.com/pedidos-en-linea/")
publicidad=driver.find_element(by=By.CSS_SELECTOR, value="body > div.container > div > div.popup-onload > div > a > img")
publicidad.click()
textbox=driver.find_element(by=By.CSS_SELECTOR, value="#input_buscar")
textbox.send_keys(Busqueda)
boton=driver.find_element(by=By.CSS_SELECTOR, value="#btn_buscar_catalogo")
boton.click()
grupo=driver.find_elements(by=By.CSS_SELECTOR, value="#id_mostrar_productos_padres>div>div")
for pro in grupo:
    try:
        nombre=pro.find_element(By.CSS_SELECTOR,value="#id_mostrar_productos_padres > div >div > div > center > div > label > div.titulo_producto_interno").text
        marca = pro.find_element(By.CSS_SELECTOR,value="#id_mostrar_productos_padres > div >div > div > center > div > label > div.marca_producto_interno").text
        precio = pro.find_element(By.CSS_SELECTOR,value="#id_mostrar_productos_padres > div >div > div > center > div > span.precio_producto").text
        print("Nombre: ", nombre)
        print("Marca: ", marca)
        print("Precio: ", precio)
        print("**********************************************")
        ganga = {
            "name": nombre,
            "marca": marca,
            "price": precio
        }
        enviar = base.get_collection(Busqueda)
        enviar.insert_one(ganga)
    except Exception as e:
        print("ERROR AL OBTENER INFORMACIÓN O EXTRAER DATOS",e)
driver.close()
print("//////////////////////////////")
print("//////////*GRACIAS*///////////")
print("//////////////////////////////")

