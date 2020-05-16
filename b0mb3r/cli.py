import os

import click
import pkg_resources
import uvicorn
from loguru import logger

os.chdir(os.path.join(pkg_resources.get_distribution("b0mb3r").location, "b0mb3r"))

from b0mb3r.app.main import app
from b0mb3r.logger import sentry_handler
from b0mb3r.utils import open_url

logger.add(sentry_handler, level="ERROR")


@logger.catch
@click.command()
@click.option("--ip", default="127.0.0.1")
@click.option("--port", default=8080)
def main(ip: str, port: int):
    open_url(f"http://{ip}:{port}/")
    uvicorn.run(app, host=ip, port=port, log_level="error")


if __name__ == "__main__":
    main()
