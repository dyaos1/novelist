"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx

import requests, json

WRITER_URL = "http://localhost:8000/writer"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    first_input: str
    second_input: str
    text: str

class ButtonState(rx.State):
    final: str =""
    def submit(self, first, second, last):
        r = requests.post(WRITER_URL, json={
            "genre": first,
            "character": second,
            "news_text": last
        })
        data = r.json()
        self.final = json.dumps(data, ensure_ascii=False)


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.input(
                placeholder="장르",
                value=State.first_input,
                on_change=State.set_first_input
            ),
            rx.input(
                placeholder="주인공 이름",
                value=State.second_input,
                on_change=State.set_second_input

            ),
            rx.text_area(
                placeholder="뉴스기사",
                value=State.text,
                on_change=State.set_text
            ),
            rx.button(
                'submit',
                on_click=ButtonState.submit(State.first_input, State.second_input, State.text)
            ),
            # rx.text(State.first_input),
            # rx.text(State.second_input),
            # rx.text(State.text),
            rx.text(ButtonState.final),
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
