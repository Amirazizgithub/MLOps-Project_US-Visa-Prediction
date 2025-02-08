# Path: US_Visa_Prediction/entity/artifact_entity.py

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    training_file_path: str
    testing_file_path: str
