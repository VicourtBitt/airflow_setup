from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import date, datetime
import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

# ============= VARIAVEIS GERAIS
__TODAY__ = date.today()

# ============= DEFINICAO DE TAREFAS UTILITARIAS
# Queries SQL, Dataframes, Tratamento
def print_today():
    _logger.info(f"Hello, today is {__TODAY__}")

def print_hello():
    _logger.info(f"hello")

def get_conn():
    conn = BaseHook.get_connection("avocados_postgres_prod")
    _logger.info(conn)

# ============= DEFINICAO DE TAREFAS PRINCIPAIS
# Pega -> Retorna
# def send_mail():
#     metadata = retrieve_email_metadata()
#     send_mail_class = SendMail()
#     send_mail_class.send_mail(metadata)

# ============= DAG (SCRIPT)
with DAG(
    dag_id="get_dependencies",
    start_date=datetime(day=11, month=2, year=2026),
                    #  M H D   M D/S
    schedule_interval="0 */4 * * *", # CRON
    catchup=False
) as dag:
    task_one = PythonOperator(
        task_id="task_one",
        python_callable=print_today
    )

    task_two = BashOperator(
        task_id="task_two",
        bash_command="python3 -m pip freeze",
    )

    task_three = PythonOperator(
        task_id="task_three",
        python_callable=print_hello
    )

    task_four = PythonOperator(
        task_id="task_four",
        python_callable=get_conn
    )

    task_one >> [task_two, task_three] >> task_four