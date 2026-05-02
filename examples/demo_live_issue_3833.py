from time import sleep
from rich.live import Live
from rich.text import Text

with Live(Text("frame 1"), screen=True, auto_refresh=False) as live:
    sleep(1)
    live.console.print("printed line should remain visible")
    sleep(1)
    live.console.log("logged line should remain visible")
    sleep(1)
    live.update(Text("frame 2"), refresh=True)
    sleep(3)