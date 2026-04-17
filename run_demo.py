import os
import time

from rich.console import Console, Group
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
    nested_track,
)
from rich.text import Text


def env_truthy(name: str) -> bool:
    value = os.getenv(name, "")
    return value.strip().lower() not in {"", "0", "false", "no", "off"}


def build_header(disabled: bool) -> Text:
    if disabled:
        return Text("Progress demo — disabled by RICH_DISABLE_PROGRESS", style="bold yellow")
    return Text("Progress demo — active", style="bold green")


def run_demo() -> None:
    console = Console()

    progress_disabled = env_truthy("RICH_DISABLE_PROGRESS")

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=False,
        disable=progress_disabled,
    )

    header = build_header(progress_disabled)

    if progress_disabled:
        content = Group(
            header,
            Text(
                "The progress bar is hidden because RICH_DISABLE_PROGRESS is set.",
                style="dim",
            ),
        )
        console.print(Panel(content, title="Demonstration Panel", border_style="yellow"))
        return

    console.print(Panel(header, title="Demonstration Panel", border_style="green"))

    with progress:
        task_id = progress.add_task("Loading demo...", total=100)

        for _ in range(100):
            time.sleep(0.03)
            progress.advance(task_id, 1)
def run_nested_demo() -> None:
    console = Console()

    progress_disabled = env_truthy("RICH_DISABLE_PROGRESS")

    if progress_disabled:
        console.print(
            Panel(
                Text(
                    "Nested progress bars hidden because RICH_DISABLE_PROGRESS is set.",
                    style="dim",
                ),
                title="Nested Progress Demo",
                border_style="yellow",
            )
        )
        return

    console.print(
        Panel(
            Text("Nested progress demo - nested_track()", style="bold cyan"),
            title="Nested Progress Demo",
            border_style="cyan",
        )
    )

    for i in nested_track(
        range(5),
        description="Outer loop...",
        console=console,
        disable=progress_disabled,
    ):
        for j in nested_track(
            range(20),
            description="Inner loop...",
            disable=progress_disabled,
        ):
            time.sleep(0.02)

if __name__ == "__main__":
    # First run: progress bar enabled (env var unset)
    os.environ.pop("RICH_DISABLE_PROGRESS", None)
    run_demo()

    print()

    # Second run: progress bar disabled (env var set)
    os.environ["RICH_DISABLE_PROGRESS"] = "1"
    run_demo()

    os.environ.pop("RICH_DISABLE_PROGRESS", None)
    run_nested_demo()
    input("Press Enter to exit...")