## CHEST CANCER CLASSIFICATION USING MLflow
 Objective:
 - The primary goal of this project is to classify chest CT images into different cancer types using deep neural networks (CNNs).

 - [Data link](https://drive.google.com/file/d/1z0mreUtRmR-P-magILsDR3T7M6IkGXtY/view?usp=sharing)

## Workflow
```bash
1. update config.yaml
2. update secrets.yaml
3. update params.yaml
4. update the entity
5. update the configaration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml
```
## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)
- MLflow is an open-source platform, purpose-built to assist machine learning practitioners and teams in handling the complexities of the machine learning process. MLflow focuses on the full lifecycle for machine learning projects, ensuring that each phase is manageable, traceable, and reproducible.
## Git Command
```bash
git add .

git commit -m "first commit"

git push -u origin main
```

## How To Run -->
```bash
conda create -n venv python=3.8 -y
```

```bash
conda activate venv
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


### Mlflow dagshub connection uri

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/Pouravi-2003/End_To_End_Chest_Cancer_Classification_Project.mlflow \
MLFLOW_TRACKING_USERNAME=Pouravi-2003 \
MLFLOW_TRACKING_PASSWORD=46c4f4f538134cf8f9896d024bd4fb059d72fd86 \
python script.py
```

### RUN from bash terminal

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Pouravi-2003/End_To_End_Chest_Cancer_Classification_Project.mlflow

export MLFLOW_TRACKING_USERNAME=Pouravi-2003 

export MLFLOW_TRACKING_PASSWORD=46c4f4f538134cf8f9896d024bd4fb059d72fd86

```
 - if  you will show this error ('export' is not recognized as an internal or external command,
    operable program or batch file) in your terminal use set insted of export
    ```bash
    set MLFLOW_TRACKING_URI=https://dagshub.com/Pouravi-2003/End_To_End_Chest_Cancer_Classification_Project.mlflow

    set MLFLOW_TRACKING_USERNAME=Pouravi-2003 

    set MLFLOW_TRACKING_PASSWORD=46c4f4f538134cf8f9896d024bd4fb059d72fd86
    ```



