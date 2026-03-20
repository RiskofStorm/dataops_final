import requests
import random
import json
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

ML_SERVICE_URL = "http://ml-service:8080/api/v1/predict"


def call_ml_service(num_requests: int = 10, **context):

    results = []

    for i in range(num_requests):
        features = [round(random.uniform(0.1, 5.0), 2) for _ in range(3)]

        try:
            response = requests.post(
                ML_SERVICE_URL,
                json={"features": features},
                timeout=10,
            )
            response.raise_for_status()
            result = response.json()

            logger.info(json.dumps({
                "request": i + 1,
                "features": features,
                "prediction": result["prediction"],
                "latency_ms": result["latency_ms"],
            }))
            results.append(result)

        except Exception as e:
            logger.error(f"Request {i + 1} failed: {e}")

    logger.info(f"Done: {len(results)}/{num_requests} successful requests")
    return results


def call_ml_service_burst(**context):
    return call_ml_service(num_requests=50)


def call_ml_service_light(**context):
    return call_ml_service(num_requests=5)


with DAG(
        dag_id="ML-Service",
        description="Generate traffic to ML service for Grafana metrics",
        start_date=datetime(2024, 1, 1),
        schedule=timedelta(minutes=1),
        catchup=False,
        tags=["ml-service", "monitoring"],
) as dag:
    light_load = PythonOperator(
        task_id="LOAD",
        python_callable=call_ml_service_light,
    )

    # normal_load = PythonOperator(
    #     task_id="normal_load",
    #     python_callable=call_ml_service,
    #     op_kwargs={"num_requests": 20},
    # )
    #
    # burst_load = PythonOperator(
    #     task_id="burst_load",
    #     python_callable=call_ml_service_burst,
    # )

    # light_load >> normal_load >> burst_load