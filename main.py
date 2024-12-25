import yaml
import csv


def collect_stages():
    with open('data/gitlab-ci.yml', 'r') as file:
        data = yaml.safe_load(file)
    
    stage_counts = {}
    
    for job_name, job_details in data.items():
        if isinstance(job_details, dict) and 'stage' in job_details:
            stage = job_details['stage']
            if stage in stage_counts:
                stage_counts[stage] += 1
            else:
                stage_counts[stage] = 1
    
    with open('stages_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Stage', 'Count'])
        for stage, count in stage_counts.items():
            writer.writerow([stage, count])
    
    print("CSV файл успешно обновлен с подсчетом stage.")

collect_stages()
