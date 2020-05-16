import sentry_sdk

from b0mb3r.utils import retrieve_installed_version

sentry_sdk.init(
    "https://f9be285af3ff4f949baba007ddebee24@sentry.io/3144601",
    release=retrieve_installed_version(),
)


def sentry_handler(message):
    sentry_sdk.capture_exception(message.record["exception"])
