from ursina import*

#Inicializar la aplicación
app = Ursina()


window.size = (800, 600)
window.title = "Juego de Vida 2D"
window.render_mode = '2d'
camera.orthographic = True
camera.fov = 5


# Declaracion entidad 
entidad_Cubo = Entity(model = "cube", color = color.red, scale=(0.8,1,1))

def update():

    if held_keys['w']:
        entidad_Cubo.y += 0.03

    if held_keys['s']:
        entidad_Cubo.y -= 0.03

    if held_keys['a']:
        entidad_Cubo.x -= 0.03

    if held_keys['d']:
        entidad_Cubo.x += 0.03
    

    def on_click():
        print("Click en la entidad")

    entidad_Cubo.on_click = on_click


#Ejecutar la aplicación
app.run()

