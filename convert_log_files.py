import os
from tqdm import tqdm
from meta_feature_extraction import sort_files
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
