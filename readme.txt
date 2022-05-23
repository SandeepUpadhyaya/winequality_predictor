1. Codes what I have used in mlflow perspective
to run the project bash "
mlflow run .
"
2. to change the parameter value: "bash
mlflow run . -P alpha = 0.9

3.For Individual runs 
mlflow run . -P alpha=0.7

mlflow run . -P l1_ratio=0.7

4. For changing paramter together
mlflow run . -P alpha=0.71 -P l1_ratio=0.71


creating new environment conda: "bash
conda create -n myenv python=3.6
"
tracking server setting
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

backend server/db setting
mlflow server --backend-store-uri sqlite:///mydb.sqlite --default-artifact-root .\mlruns

model serving
mlflow models serve -m mlruns\0\1b44805fd5e84ac3a536bd25fb59c26b\artifacts\model

mlflow models serve --model-uri runs:/1b44805fd5e84ac3a536bd25fb59c26b/ElasticnetWineModel

build docker image 
mlflow models build-docker -m mlruns\0\1b44805fd5e84ac3a536bd25fb59c26b\artifacts\model\ -n elastic_net_wine

deploy
docker run -p 8080:8080 elastic_net_wine.

------------------------------------------------------------------------------------