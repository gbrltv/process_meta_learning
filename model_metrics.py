import os
import time
import pandas as pd
from tqdm import tqdm
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.conformance.tokenreplay.variants import token_replay
from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator
from meta_feature_extraction import sort_files

columns = [
    "log",
    "variant",
    "fitness_time",
    "precision_time",
    "generalization_time",
    "simplicity_time",
    "perc_fit_traces",
    "average_trace_fitness",
    "log_fitness",
    "precision",
    "generalization",
    "simplicity",
]

discovery_algorithms = ["IM", "IMf", "IMd", "HM", "AM"]


def extract_metrics(log, net, im, fm):
    """
    Extracts model quality criteria: fitness, precision, generalization, simplicity
    Also records time spent in each metric
    """
    start_time = time.time()
    fitness = replay_fitness_evaluator.apply(
        log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED
    )
    fitness_time = time.time() - start_time

    start_time = time.time()
    precision = precision_evaluator.apply(
        log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN
    )
    precision_time = time.time() - start_time

    start_time = time.time()
    generalization = generalization_evaluator.apply(log, net, im, fm)
    generalization_time = time.time() - start_time

    start_time = time.time()
    simplicity = simplicity_evaluator.apply(net)
    simplicity_time = time.time() - start_time

    return [
        fitness_time,
        precision_time,
        generalization_time,
        simplicity_time,
        *fitness.values(),
        precision,
        generalization,
        simplicity,
    ]


model_metrics = []
event_logs_path = "event_logs"

print("Extracting model quality metrics")

# loop through logs, discover model and extract features
for file in tqdm(sort_files(os.listdir(event_logs_path))):
    log_name = file.split(".xes")[0]

    # read event log
    log = xes_importer.apply(
        f"{event_logs_path}/{file}", parameters={"show_progress_bar": False}
    )

    # discover models
    for miner in discovery_algorithms:
        if miner == "IM":
            net, im, fm = inductive_miner.apply(
                log, variant=inductive_miner.Variants.IM
            )
        elif miner == "IMf":
            net, im, fm = inductive_miner.apply(
                log, variant=inductive_miner.Variants.IMf
            )
        elif miner == "IMd":
            net, im, fm = inductive_miner.apply(
                log, variant=inductive_miner.Variants.IMd
            )
        elif miner == "HM":
            net, im, fm = heuristics_miner.apply(log)
        else:
            net, im, fm = alpha_miner.apply(log)

        # compute model metrics
        model_metrics.append([log_name, miner, *extract_metrics(log, net, im, fm)])

# save file
output_path = "results"
os.makedirs(output_path, exist_ok=True)

pd.DataFrame(model_metrics, columns=columns).to_csv(f"{output_path}/model_metrics.csv", index=False)
