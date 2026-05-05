from rich.console import Console
import webbrowser, os, re

console = Console(record=True, width=60)
console.print("STRING_WITH_UNDERSCORE_CHARS")

svg = console.export_svg(title="Rich")

svg = re.sub(
    r'(<rect[^>]+id="[^"]clip-terminal[^"]"[^>]+height=")([0-9.]+)(")',
    lambda m: m.group(1) + str(float(m.group(2)) + 8) + m.group(3),
    svg
)

with open("demo.svg", "w") as f:
    f.write(svg)

webbrowser.open(f"file://{os.path.abspath('demo.svg')}")