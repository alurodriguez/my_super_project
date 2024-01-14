import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")

import time
import psycopg2
from psycopg2 import OperationalError

def create_conn():
    conn = None
    while not conn:
        try:
            conn = psycopg2.connect(
                dbname="mydb",
                user="myuser",
                password="mypassword",
                host="db"
            )
            print("Database connection successful")
        except OperationalError as e:
            print(e)
            time.sleep(5)
    return conn



if __name__ == "__main__":
    main()
    conn = create_conn()