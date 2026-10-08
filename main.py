import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.padding = 20
    page.bgcolor = "#1e1e2e"
    page.vertical_alignment = ft.MainAxisAlignment.END

    # Pantalla de resultados
    pantalla = ft.Text(value="0", size=40, color="#E79F93", text_align=ft.TextAlign.RIGHT)

    # Lógica al presionar un botón
    def click_boton(e):
        texto_boton = e.control.text

        if texto_boton == "C":
            pantalla.value = "0"
        elif texto_boton == "=":
            try:
                expresion = pantalla.value.replace("×", "*").replace("÷", "/")
                pantalla.value = str(eval(expresion))
            except Exception:
                pantalla.value = "Error"
        else:
            if pantalla.value in ["0", "Error"]:
                pantalla.value = texto_boton
            else:
                pantalla.value += texto_boton

        page.update()

    # Creador de botones reutilizables
    def crear_boton(texto, color="#9959FF", expand=1):
        return ft.ElevatedButton(
            text=texto,
            on_click=click_boton,
            bgcolor=color,
            color="white",
            expand=expand,
            height=65,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
        )

    # Diseño de la interfaz
    page.add(
        ft.Container(
            content=pantalla,
            alignment=ft.alignment.center_right,
            padding=15,
            bgcolor="#7D6180",
            border_radius=10,
        ),
        ft.Column([
            ft.Row([
                crear_boton("C", color="#CA1FDE"),
                crear_boton("÷"),
                crear_boton("×"),
                crear_boton("-")
            ]),
            ft.Row([crear_boton("7"), crear_boton("8"), crear_boton("9"), crear_boton("+")]),
            ft.Row([crear_boton("4"), crear_boton("5"), crear_boton("6"), crear_boton("=")]),
            ft.Row([
                crear_boton("1"),
                crear_boton("2"),
                crear_boton("3"),
                crear_boton("0")
            ]),
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)