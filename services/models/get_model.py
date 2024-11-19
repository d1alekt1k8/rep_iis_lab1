import mlflow
import pickle as pkl

# Работаем с MLflow локально
TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000

registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

mlflow.set_tracking_uri(tracking_uri)   
mlflow.set_registry_uri(registry_uri)   

RUN_NAME = '9fa1c8768389439eae3319b6a98568c0'
loaded_model = mlflow.sklearn.load_model(f'runs:/{RUN_NAME}/models')

with open('model.pkl', 'wb+') as f:
    pkl.dump(loaded_model, f)