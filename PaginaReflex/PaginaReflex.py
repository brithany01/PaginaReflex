import reflex as rx


class State(rx.State):
    mensaje = "Bienvenida a Beauty Studio ✨"

    def mostrar_tip(self):
        self.mensaje = "💄 Tip: Una piel hidratada mejora cualquier maquillaje"

    def mostrar_makeup(self):
        self.mensaje = "🌸 El maquillaje resalta tu belleza natural"

    def mostrar_reflex(self):
        self.mensaje = "💜 Página creada con Reflex y Python"


def index():
    return rx.center(
        rx.vstack(

            rx.heading(
                "Beauty Studio",
                size="9",
                color="#7c3aed",
            ),

            rx.text(
                "Mi primera página web sobre maquillaje ✨",
                size="5",
                color="#6b7280",
            ),

            rx.box(
                rx.text(
                    State.mensaje,
                    size="5",
                    color="#5b21b6",
                    text_align="center",
                ),
                bg="#f5f3ff",
                padding="1.2em",
                border_radius="16px",
                width="100%",
            ),

            rx.hstack(

                rx.button(
                    "💄 Tip",
                    on_click=State.mostrar_tip,
                    bg="#c4b5fd",
                    color="white",
                    radius="full",
                ),

                rx.button(
                    "🌸 Makeup",
                    on_click=State.mostrar_makeup,
                    bg="#d8b4fe",
                    color="white",
                    radius="full",
                ),

                rx.button(
                    "💜 Reflex",
                    on_click=State.mostrar_reflex,
                    bg="#a78bfa",
                    color="white",
                    radius="full",
                ),

                spacing="4",
            ),

            rx.text(
                "La belleza comienza con confianza ✨",
                color="#9ca3af",
                font_style="italic",
            ),

            spacing="6",
            align="center",

            bg="white",
            padding="3em",
            border_radius="24px",
            box_shadow="0px 4px 12px rgba(0,0,0,0.08)",
            width="65%",
        ),

        bg="#f3f0ff",
        width="100%",
        height="100vh",
        padding="2em",
    )


app = rx.App()
app.add_page(index)