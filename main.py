import flet as ft

def main(page: ft.Page):

    # Configuración de la ventana
    page.title = "Star Penguin🐧"
    page.bgcolor = "#B3E5FC"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False

    # Título del juego
    titulo = ft.Text(
        "Star Penguin🐧",
        size=30,
        color="#17365D",
        font_family="Pacifico"
    )

    # Mensaje inicial
    mensaje = ft.Text(
        "¡Ayuda al pingüino a conseguir sus estrellas!",
        size=20,
        color="#17365D",
        font_family="Pacifico"
    )

    # Escenario
    escenario = ft.Container(
        width=700,
        height=400,
        bgcolor="#E1F5FE",
        border_radius=20,
        alignment=ft.Alignment.CENTER,
        content=ft.Text(
            "❄️ ¡Aquí vivirá nuestro pingüino! ❄️",
            size=23,
            color="#2676A8"
            font_family="Pacifico"
        )
    )

    page.add(
        ft.Column(
            [
                titulo,
                mensaje,
                escenario
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)