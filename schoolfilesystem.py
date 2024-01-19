
#Libraries you may need:
#import csv, collections, dictionary, (pandas as pd), urlopen, etc..
import pandas as pd
import requests
import csv
import collections


class SchoolAssessmentSystem:
    def __init__(self, data):
        self.data = data

    def process_file(file_path, file_format):            
        if file_format == "csv":
            data = pd.read_csv(file_path)
        elif file_format == "excel":
            data = pd.read_excel(file_path)
        elif file_format == "txt":
            with open(file_path, "r") as f:
                data = f.read()
        else:
            raise ValueError("Unsupported file format")
        return data

    
    def transfer_data(source_data, target_file_path, target_file_format):
        def preprocess_data(data):
            return data.apply(lambda x: x.astype(str).str.upper())

        processed_data = preprocess_data(source_data)

        if target_file_format not in ["csv", "excel"]:
            raise ValueError("Unsupported file format for data transfer")

        if target_file_format == "csv":
            processed_data.to_csv(target_file_path, index=False)
        elif target_file_format == "excel":
            processed_data.to_excel(target_file_path, index=False)

    
    def fetch_web_data(data):
        response = requests.get(data)
        response.raise_for_status()
        return response.text
    
    def analyze_data(data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input 'data' must be a pandas DataFrame")

        summary_statistics = data.describe()
        outliers = data[(data - data.mean()).abs() > 3 * data.std()].dropna()

        average_scores_by_student = data.groupby('Student').mean()
        average_scores_by_subject = data.groupby('Subject').mean()

        insights = {
            'summary_statistics': summary_statistics,
            'outliers': outliers,
            'average_scores_by_student': average_scores_by_student,
            'average_scores_by_subject': average_scores_by_subject
        }
        return insights

    def generate_summary(insights):
        summary = f"Assessment Summary:\n\n"
        summary += f"Summary Statistics:\n{insights['summary_statistics']}\n\n"
        summary += f"Outliers:\n{insights['outliers']}\n\n"
        summary += f"Average Scores by Student:\n{insights['average_scores_by_student']}\n\n"
        summary += f"Average Scores by Subject:\n{insights['average_scores_by_subject']}\n\n"
        return summary
