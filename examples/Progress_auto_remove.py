import time
from rich.progress import Progress, BarColumn, TaskProgressColumn, TimeRemainingColumn

tasks_config = [
    ("Downloading assets",       0.04, "cyan"),
    ("Compiling modules",        0.06, "green"),
    ("Running tests",            0.03, "yellow"),
    ("Packaging release",        0.05, "magenta"),
    ("Uploading artifacts",      0.07, "cyan"),
    ("Installing dependencies",  0.02, "green"),
    ("Building Docker image",    0.04, "yellow"),
    ("Running migrations",       0.06, "magenta"),
    ("Syncing database",         0.03, "cyan"),
    ("Fetching config",          0.08, "green"),
    ("Validating schema",        0.05, "yellow"),
    ("Generating reports",       0.04, "magenta"),
    ("Cleaning cache",           0.07, "cyan"),
    ("Indexing files",           0.03, "green"),
    ("Compressing logs",         0.06, "yellow"),
    ("Archiving backups",        0.04, "magenta"),
    ("Scanning vulnerabilities", 0.05, "cyan"),
    ("Deploying to staging",     0.03, "green"),
    ("Running linter",           0.07, "yellow"),
    ("Checking types",           0.04, "magenta"),
    ("Minifying assets",         0.06, "cyan"),
    ("Optimizing images",        0.03, "green"),
    ("Sending notifications",    0.08, "yellow"),
    ("Updating changelog",       0.05, "magenta"),
    ("Tagging release",          0.04, "cyan"),
    ("Publishing to PyPI",       0.03, "green"),
    ("Clearing temp files",      0.07, "yellow"),
    ("Restarting services",      0.05, "magenta"),
    ("Verifying deployment",     0.04, "cyan"),
    ("Done finalizing",          0.06, "green"),
]

with Progress(
    "[progress.description]{task.description}",
    BarColumn(),
    TaskProgressColumn(),
    TimeRemainingColumn(),
    auto_remove=True,
) as progress:

    handles = [
        progress.add_task(f"[{color}]{label}[/{color}]", total=100)
        for label, _, color in tasks_config
    ]

    while not progress.finished:
        for handle, (_, speed, _) in zip(handles, tasks_config):
            if handle in progress.task_ids:
                progress.advance(handle, speed * 100 * 0.05)
        time.sleep(0.05)