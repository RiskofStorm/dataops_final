docker network create monitoring-net


cd mlflow && docker compose up -d # UI доступен на http://localhost:5000
cd ..
mkdir -p airflow/dags airflow/logs airflow/plugins
cd airflow && docker compose up airflow-init && docker compose up -d # UI: http://localhost:8080  admin/admin
cd ..
cd lakefs && docker compose up -d # LakeFS UI: http://localhost:8001 # MinIO UI:  http://localhost:9001
cd ..
cd jupyterhub && docker compose up -d # UI: http://localhost:8000  admin/admin
cd ..
cd ml-service && docker compose up -d # Тест: curl -X POST http://localhost:8080/api/v1/predict -H "Content-Type: application/json"  -d '{"features": [1.0, 2.0, 3.0]}'
cd ..


helm create helm/ml-service
# Затем замени содержимое файлов:
