# DataOps Final Project

Финальный проект по предмету DataOps. Разворачивает полный стек ML-инфраструктуры: MLflow, Airflow, LakeFS, JupyterHub, ML-сервис с мониторингом.

## Запуск
```bash
docker network create monitoring-net
```
```bash
cd mlflow && docker compose up -d
cd ../airflow && docker compose up -d
cd ../lakefs && docker compose up -d
cd ../jupyterhub && docker compose up -d
cd ../ml-service && docker compose up -d
cd ../monitoring && docker compose up -d
```

## Сервисы

| Сервис | URL |
|--------|-----|
| MLflow | http://localhost:5000 |
| Airflow | http://localhost:8080 |
| LakeFS | http://localhost:8001 |
| JupyterHub | http://localhost:8000 |
| ML-сервис | http://localhost:8088 |
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |

## Тест ML-сервиса
```bash
curl -X POST http://localhost:8088/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0]}'
```