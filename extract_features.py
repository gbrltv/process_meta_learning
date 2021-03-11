import os
import pandas as pd
from tqdm import tqdm
from meta_feature_extraction import pipeline, sort_files
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter

print("Converting log files")
event_logs_path = "event_logs"
for f in tqdm(sort_files(os.listdir(event_logs_path))):
    log = xes_importer.apply(
        f"{event_logs_path}/{f}", parameters={"show_progress_bar": False}
    )
    f_name = f.split(".gz")[0]
    xes_exporter.apply(
        log, f"{event_logs_path}/{f_name}", parameters={"show_progress_bar": False}
    )
    os.remove(f"{event_logs_path}/{f}")

print("Extracting meta-features")
combined_features = []
for file in tqdm(sort_files(os.listdir(event_logs_path))):
    combined_features.append(pipeline(event_logs_path, file))

with open("meta_feature_extraction/column_names.txt") as f:
    columns = f.readlines()
columns = [x.strip() for x in columns]

print("Saving meta-features")
pd.DataFrame(combined_features, columns=columns).to_csv("log_features.csv", index=False)
