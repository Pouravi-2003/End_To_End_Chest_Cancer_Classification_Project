## CHEST CANCER CLASSIFICATION

 - [Data link](https://drive.google.com/file/d/1z0mreUtRmR-P-magILsDR3T7M6IkGXtY/view?usp=sharing)

## Workflow

1. update config.yaml
2. update secrets.yaml
3. update params.yaml
4. update the entity
5. update the configaration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml

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




