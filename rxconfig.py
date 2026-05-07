import reflex as rx

config = rx.Config(
    app_name="PaginaReflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)