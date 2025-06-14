import flet as ft
import pyttsx3

def main(page: ft.Page):
    page.title = "Texto a Voz con pyttsx3" #Titulo de la ventana
    page.theme_mode = ft.ThemeMode.LIGHT #Forzar el tema claro
    page.window.width = 480
    page.window.height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.min_width = 480  # Ancho mínimo permitido
    page.window.min_height = 600  # Alto mínimo permitido
    page.window.resizable = False
    page.window.maximizable = False
    subtitle = ft.Text(
        value='Escribe un texto para hablar',
        weight=ft.FontWeight.W_700
    )
    texto_input = ft.TextField(
        width=500,
        multiline=True,
        min_lines=17,
        max_lines=17,
        autofocus=True, 
        expand=False
    )

    resultado_texto = ft.Text()

    def hablar(e):
        texto = texto_input.value.strip()
        if texto:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', rate - 30)
            engine.say(texto)
            engine.runAndWait()
        else:
            resultado_texto.value = "❗ Ingresa algún texto"
        page.update()

    boton_hablar = ft.ElevatedButton("Hablar", on_click=hablar)

    page.add(
        ft.Column([
            subtitle,
            texto_input,
            boton_hablar,
            resultado_texto
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
