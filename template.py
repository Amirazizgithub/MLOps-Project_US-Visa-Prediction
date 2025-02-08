import os
from pathlib import Path

# Define the project name
Project_Name = "US_Visa_Prediction"

# Define the list of files to be created in the project
list_of_files = [
    f"{Project_Name}/__init__.py",
    f"{Project_Name}/components/__init__.py",
    f"{Project_Name}/components/data_ingestion.py",
    f"{Project_Name}/components/data_validation.py",
    f"{Project_Name}/components/data_transformation.py",
    f"{Project_Name}/components/model_trainer.py",
    f"{Project_Name}/components/model_evaluation.py",
    f"{Project_Name}/components/model_pusher.py",
    f"{Project_Name}/configurations/__init__.py",
    f"{Project_Name}/configurations/mongo_db_connection.py",
    f"{Project_Name}/constants/__init__.py",
    f"{Project_Name}/data_access/__init__.py",
    f"{Project_Name}/data_access/usvisa_data.py",
    f"{Project_Name}/entity/__init__.py",
    f"{Project_Name}/entity/config_entity.py",
    f"{Project_Name}/entity/artifact_entity.py",
    f"{Project_Name}/exceptions/__init__.py",
    f"{Project_Name}/logger/__init__.py",
    f"{Project_Name}/pipeline/__init__.py",
    f"{Project_Name}/pipeline/train_pipeline.py",
    f"{Project_Name}/pipeline/prediction_pipeline.py",
    f"{Project_Name}/utils/__init__.py",
    f"{Project_Name}/utils/main_utils.py",
    "notebooks/__init__.py",
    "notebooks/mongo_db.ipynb",
    "notebooks/EDA_US_Visa.ipynb",
    "notebooks/Feature_Engineering_and_Model_Training.ipynb",
    "app.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    ".env",
    ".dockerignore",
    "Dockerfile",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

# Create the directories of the folder and write the files if they do not exist
for file in list_of_files:
    file_path = Path(file)
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file, "w") as f:
            f.write("# Path: " + file)
print("Project structure created successfully!")

