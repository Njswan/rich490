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
)
from rich.text import Text


def env_truthy(name: str) -> bool:
    value = os.getenv(name, "")
    return value.strip().lower() not in {"", "0", "false", "no", "off"}


def build_header(disabled: bool) -> Text:
    if disabled:
        return Text("Progress demo — disabled by RICH_DISABLE_PROGRESS", style="bold yellow")
    return Text("Progress demo — active", style="bold green")


def main() -> None:
    console = Console()

    # If your app already loads .env into the environment, this is enough.
    # Example:
    #   RICH_DISABLE_PROGRESS=1
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

    with progress:
        task_id = progress.add_task("Loading demo...", total=100)

        console.print(
            Panel(
                Group(header, progress),
                title="Demonstration Panel",
                border_style="green",
            )
        )

        for _ in range(100):
            time.sleep(0.03)
            progress.advance(task_id, 1)


if __name__ == "__main__":
    main()