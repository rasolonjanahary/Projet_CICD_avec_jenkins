#!/bin/sh
# Lance MLflow en arrière-plan
mlflow ui --host 0.0.0.0 --port 5000 &
# Lance Uvicorn au premier plan
uvicorn src.app:app --host 0.0.0.0 --port 8000