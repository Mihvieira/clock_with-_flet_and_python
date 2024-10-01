import flet as ft
import asyncio
from time import strftime

class ClockAsync(ft.Container):
    def __init__(self, height=50, width=100):
        super().__init__()
        self.height = height
        self.width = width
        self.time_string = ft.Text(style=ft.TextStyle(size=15))
        self.content = ft.Column(
            alignment=ft.alignment.center,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row([self.time_string])
            ]
        )
    
    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_time)
    
    def will_unmount(self):
        self.running = False
    
    async def update_time(self):
        while self.running:
            self.time_string.value = strftime('%H:%M:%S')
            self.update()
            await asyncio.sleep(1)

def main(page: ft.Page):
    page.title = "Clock"
    page.window_width = 200
    page.window_height = 200
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    clock = ClockAsync()
    page.add(clock)

ft.app(target=main)
