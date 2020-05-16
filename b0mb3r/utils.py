import os
import re
import subprocess
import sys
import webbrowser
from typing import Awaitable, Callable

from loguru import logger


@logger.catch
def open_url(url: str):
    logger.info(f"Opening {url}...")
    try:
        if "com.termux" in os.environ.get("PREFIX", ""):  # If device is running Termux
            subprocess.run(
                ["am", "start", "--user", "0", "-a", "android.intent.action.VIEW", "-d", url]
            )
    except FileNotFoundError:
        pass
    webbrowser.open(url, new=2, autoraise=True)


@logger.catch
def retrieve_installed_version() -> str:
    package_info = subprocess.run(
        [sys.executable, "-m", "pip", "show", "b0mb3r"], stdout=subprocess.PIPE, check=True
    )
    bytes_version = re.search(br"Version: ([0-9]\.[0-9.]*)", package_info.stdout).group(1)
    return bytes_version.decode()


@logger.catch
async def await_with_callback(coroutine: Awaitable, callback: Callable, *args, **kwargs):
    try:
        await coroutine
    except Exception:
        pass
    finally:
        callback(*args, **kwargs)
