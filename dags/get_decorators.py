from airflow.decorators import dag, task
from datetime import datetime, date
import logging
import os

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

@dag(
    dag_id="get_decorators",
    start_date=datetime(day=11, month=2, year=2026),
    schedule_interval="0 */4 * * *",
)
def etl_pipeline():

    @task()
    def print_hello():
        _logger.info("hello")

    @task()
    def get_dependencies():
        os.system("python3 -m pip freeze")

    print_hello()
    get_dependencies()

etl_pipeline()