from flask import Flask, render_template,redirect,request,url_for
import numpy as np
import matplotlib.pyplot as plt
import base64
import joblib
import pandas as pd
import pickle
import csv
import io 
import os
app = Flask(__name__) 

crime_data={
    "2021": {
        "maharashtra": {
            "murder": 300, "attempt_to_murder": 150, "sexual_harassment": 200,
            "rape": 250, "theft": 400, "hit_and_run": 100, "causing_death_by_negligence": 90, "culpable_homicide": 240,
            "kidnapping_and_abduction": 184,"arson": 50, "grievous_hurt": 120, "dowry_deaths":230
        },
        "uttar_pradesh": {
            "murder": 500, "attempt_to_murder": 300, "sexual_harassment": 450,
            "rape": 500, "theft": 600, "hit_and_run": 200,"causing_death_by_negligence": 70, "culpable_homicide": 180,
            "kidnapping_and_abduction": 200,"arson": 100, "grievous_hurt": 106, "dowry_deaths":280
        },
        "rajsthan": {
            "murder": 200, "attempt_to_murder": 100, "sexual_harassment": 150,
            "rape": 180, "theft": 350, "hit_and_run": 80,"causing_death_by_negligence": 95, "culpable_homicide": 300,
            "kidnapping_and_abduction":130,"arson": 65, "grievous_hurt": 180, "dowry_deaths":300
        },
        "aasam": {
            "murder": 250, "attempt_to_murder": 50, "sexual_harassment": 70,
            "rape": 90, "theft": 120, "hit_and_run": 60,"causing_death_by_negligence": 120, "culpable_homicide": 96,
            "kidnapping_and_abduction": 230,"arson": 150, "grievous_hurt": 360, "dowry_deaths": 90
        },
        "jammu_and_kashmir": {
            "murder": 360, "attempt_to_murder":230, "sexual_harassment": 150,
            "rape": 70, "theft": 180, "hit_and_run": 30,"causing_death_by_negligence": 100, "culpable_homicide": 203,
            "kidnapping_and_abduction": 125,"arson": 63, "grievous_hurt": 120, "dowry_deaths": 0
        },
        "Andhra Pradesh": {
            "murder": 390, "attempt_to_murder":300, "sexual_harassment": 360,
            "rape": 102, "theft": 320, "hit_and_run": 120,"causing_death_by_negligence": 230, "culpable_homicide": 130,
            "kidnapping_and_abduction": 260,"arson": 70, "grievous_hurt": 130, "dowry_deaths": 150
        },
        "Madhya Pradesh": 
        {
            "murder": 250, "attempt_to_murder":280, "sexual_harassment": 250,
            "rape": 80, "theft": 100, "hit_and_run": 201,"causing_death_by_negligence": 63, "culpable_homicide": 75,
            "kidnapping_and_abduction": 85,"arson": 80, "grievous_hurt": 230, "dowry_deaths": 150
        },
        "Bihar": {
            "murder": 450, "attempt_to_murder":320, "sexual_harassment": 260,
            "rape": 120, "theft": 280, "hit_and_run": 150,"causing_death_by_negligence": 65, "culpable_homicide": 82,
            "kidnapping_and_abduction": 120,"arson":60, "grievous_hurt": 120, "dowry_deaths": 180
        },
        "Punjab": {
            "murder": 250, "attempt_to_murder":110, "sexual_harassment": 180,
            "rape": 90, "theft": 210, "hit_and_run": 65,"causing_death_by_negligence":62, "culpable_homicide": 120,
            "kidnapping_and_abduction": 95,"arson": 85, "grievous_hurt": 98, "dowry_deaths":75
        },
        "Manipur": {
            "murder": 280, "attempt_to_murder":160, "sexual_harassment": 200,
            "rape": 100, "theft":230, "hit_and_run": 85,"causing_death_by_negligence":89, "culpable_homicide": 96,
            "kidnapping_and_abduction": 120,"arson": 96, "grievous_hurt": 260, "dowry_deaths":30
        },
        "harayana": {
            "murder": 480, "attempt_to_murder":120, "sexual_harassment": 250,
            "rape": 180, "theft": 250, "hit_and_run": 90,"causing_death_by_negligence":130, "culpable_homicide": 230,
            "kidnapping_and_abduction": 150,"arson": 65, "grievous_hurt": 95, "dowry_deaths":130
        },
        "west bengal": {
            "murder": 230, "attempt_to_murder":120, "sexual_harassment": 150,
            "rape": 150, "theft":120, "hit_and_run": 180,"causing_death_by_negligence":62, "culpable_homicide": 120,
            "kidnapping_and_abduction": 95,"arson": 85, "grievous_hurt": 98, "dowry_deaths":75
        },
        "himachal": {
            "murder": 130, "attempt_to_murder":90, "sexual_harassment": 65,
            "rape": 50, "theft": 120, "hit_and_run":60,"causing_death_by_negligence":120, "culpable_homicide": 96,
            "kidnapping_and_abduction": 70,"arson": 36, "grievous_hurt": 52, "dowry_deaths":20
        }

    },
    "2022": {
        
        "maharashtra": {
            "murder": 250, "attempt_to_murder": 130, "sexual_harassment": 120,
            "rape": 50, "theft": 200, "hit_and_run": 150, "causing_death_by_negligence": 120, "culpable_homicide": 63,
            "kidnapping_and_abduction": 190,"arson": 65, "grievous_hurt": 110, "dowry_deaths":90
        },
        "uttar_pradesh": {
            "murder": 450, "attempt_to_murder": 230, "sexual_harassment": 260,
            "rape": 150, "theft": 250, "hit_and_run": 150,"causing_death_by_negligence": 93, "culpable_homicide": 110,
            "kidnapping_and_abduction": 320,"arson": 50, "grievous_hurt": 120, "dowry_deaths":63
        },
        "rajsthan": {
            "murder": 263, "attempt_to_murder": 120, "sexual_harassment": 160,
            "rape": 110, "theft": 260, "hit_and_run": 60,"causing_death_by_negligence": 120, "culpable_homicide": 130,
            "kidnapping_and_abduction":120,"arson": 96, "grievous_hurt": 65, "dowry_deaths":36
        },
        "aasam": {
            "murder": 250, "attempt_to_murder": 120, "sexual_harassment": 80,
            "rape": 30, "theft": 160, "hit_and_run": 89,"causing_death_by_negligence":63, "culpable_homicide": 75,
            "kidnapping_and_abduction": 150,"arson": 65, "grievous_hurt": 101, "dowry_deaths": 25
        },
        "jammu_and_kashmir": {
            "murder": 150, "attempt_to_murder":62, "sexual_harassment": 180,
            "rape": 50, "theft": 190, "hit_and_run": 100,"causing_death_by_negligence": 59, "culpable_homicide": 50,
            "kidnapping_and_abduction": 105,"arson": 96, "grievous_hurt": 140, "dowry_deaths": 12
        },
        "Andhra Pradesh": {
            "murder": 300, "attempt_to_murder":120, "sexual_harassment": 196,
            "rape": 96, "theft": 420, "hit_and_run":142,"causing_death_by_negligence": 251, "culpable_homicide": 131,
            "kidnapping_and_abduction": 65,"arson": 96, "grievous_hurt": 115, "dowry_deaths": 101
        },
        "Madhya Pradesh": 
        {
            "murder": 100, "attempt_to_murder":265, "sexual_harassment": 152,
            "rape": 102, "theft": 265, "hit_and_run": 351,"causing_death_by_negligence":125 , "culpable_homicide": 90,
            "kidnapping_and_abduction": 185,"arson": 95, "grievous_hurt": 120, "dowry_deaths": 36
        },
        "Bihar": {
            "murder": 250, "attempt_to_murder":220, "sexual_harassment": 160,
            "rape": 196, "theft": 126, "hit_and_run": 250,"causing_death_by_negligence": 85, "culpable_homicide": 102,
            "kidnapping_and_abduction": 105,"arson":96, "grievous_hurt": 85, "dowry_deaths": 98
        },
        "Punjab": {
            "murder": 120, "attempt_to_murder":95, "sexual_harassment": 120,
            "rape": 150, "theft": 320, "hit_and_run": 120,"causing_death_by_negligence":69, "culpable_homicide": 110,
            "kidnapping_and_abduction": 81,"arson": 95, "grievous_hurt": 120, "dowry_deaths":90
        },
        "Manipur": {
            "murder": 120, "attempt_to_murder":85, "sexual_harassment": 100,
            "rape": 85, "theft":130, "hit_and_run": 195,"causing_death_by_negligence":96, "culpable_homicide": 152,
            "kidnapping_and_abduction": 90,"arson": 56, "grievous_hurt": 52, "dowry_deaths":10
        },
        "harayana": {
            "murder": 230, "attempt_to_murder":120, "sexual_harassment": 32,
            "rape": 133, "theft": 120, "hit_and_run": 190,"causing_death_by_negligence":30, "culpable_homicide": 103,
            "kidnapping_and_abduction": 201,"arson": 75, "grievous_hurt": 105, "dowry_deaths":65
        },
        "west bengal": {
            "murder": 230, "attempt_to_murder":125, "sexual_harassment": 125,
            "rape": 102, "theft":220, "hit_and_run": 165,"causing_death_by_negligence":182, "culpable_homicide": 100,
            "kidnapping_and_abduction": 120,"arson": 123, "grievous_hurt": 85, "dowry_deaths":90
        },
        "himachal": {
            "murder": 253, "attempt_to_murder":190, "sexual_harassment": 75,
            "rape": 126, "theft": 220, "hit_and_run":120,"causing_death_by_negligence":150, "culpable_homicide": 53,
            "kidnapping_and_abduction": 170,"arson": 63, "grievous_hurt": 152, "dowry_deaths":52
        }
    },
    "2023": {
        "maharashtra": {
            "murder": 320, "attempt_to_murder": 230, "sexual_harassment": 108,
            "rape": 120, "theft": 560, "hit_and_run": 400, "causing_death_by_negligence": 100, "culpable_homicide": 140,
            "kidnapping_and_abduction": 130,"arson": 89, "grievous_hurt": 120, "dowry_deaths":62
        },
        "uttar_pradesh": {
            "murder": 250, "attempt_to_murder": 265, "sexual_harassment": 190,
            "rape": 210, "theft": 201, "hit_and_run": 280,"causing_death_by_negligence": 170, "culpable_homicide": 100,
            "kidnapping_and_abduction": 210,"arson": 135, "grievous_hurt": 111, "dowry_deaths":102
        },
        "rajsthan": {
            "murder": 220, "attempt_to_murder": 210, "sexual_harassment": 160,
            "rape": 190, "theft": 260, "hit_and_run": 198,"causing_death_by_negligence": 110, "culpable_homicide": 130,
            "kidnapping_and_abduction":120,"arson": 95, "grievous_hurt": 196, "dowry_deaths":150
        },
        "aasam": {
            "murder": 260, "attempt_to_murder": 150, "sexual_harassment": 85,
            "rape": 165, "theft": 120, "hit_and_run": 60,"causing_death_by_negligence": 120, "culpable_homicide": 96,
            "kidnapping_and_abduction": 230,"arson": 150, "grievous_hurt": 360, "dowry_deaths": 90
        },
        "jammu_and_kashmir": {
            "murder": 360, "attempt_to_murder":230, "sexual_harassment": 150,
            "rape": 70, "theft": 180, "hit_and_run": 30,"causing_death_by_negligence": 100, "culpable_homicide": 203,
            "kidnapping_and_abduction": 125,"arson": 63, "grievous_hurt": 120, "dowry_deaths": 0
        },
        "Andhra Pradesh": {
            "murder": 390, "attempt_to_murder":300, "sexual_harassment": 360,
            "rape": 102, "theft": 320, "hit_and_run": 120,"causing_death_by_negligence": 230, "culpable_homicide": 130,
            "kidnapping_and_abduction": 260,"arson": 70, "grievous_hurt": 130, "dowry_deaths": 150
        },
        "Madhya Pradesh": 
        {
            "murder": 250, "attempt_to_murder":280, "sexual_harassment": 250,
            "rape": 80, "theft": 100, "hit_and_run": 201,"causing_death_by_negligence": 63, "culpable_homicide": 75,
            "kidnapping_and_abduction": 85,"arson": 80, "grievous_hurt": 230, "dowry_deaths": 150
        },
        "Bihar": {
            "murder": 450, "attempt_to_murder":320, "sexual_harassment": 260,
            "rape": 120, "theft": 280, "hit_and_run": 150,"causing_death_by_negligence": 65, "culpable_homicide": 82,
            "kidnapping_and_abduction": 120,"arson":60, "grievous_hurt": 120, "dowry_deaths": 180
        },
        "Punjab": {
            "murder": 250, "attempt_to_murder":110, "sexual_harassment": 180,
            "rape": 90, "theft": 210, "hit_and_run": 65,"causing_death_by_negligence":62, "culpable_homicide": 120,
            "kidnapping_and_abduction": 95,"arson": 85, "grievous_hurt": 98, "dowry_deaths":75
        },
        "Manipur": {
            "murder": 280, "attempt_to_murder":160, "sexual_harassment": 200,
            "rape": 100, "theft":230, "hit_and_run": 85,"causing_death_by_negligence":89, "culpable_homicide": 96,
            "kidnapping_and_abduction": 120,"arson": 96, "grievous_hurt": 260, "dowry_deaths":30
        },
        "harayana": {
            "murder": 480, "attempt_to_murder":120, "sexual_harassment": 250,
            "rape": 180, "theft": 250, "hit_and_run": 90,"causing_death_by_negligence":130, "culpable_homicide": 230,
            "kidnapping_and_abduction": 150,"arson": 65, "grievous_hurt": 95, "dowry_deaths":130
        },
        "west bengal": {
            "murder": 230, "attempt_to_murder":120, "sexual_harassment": 150,
            "rape": 150, "theft":120, "hit_and_run": 180,"causing_death_by_negligence":62, "culpable_homicide": 120,
            "kidnapping_and_abduction": 95,"arson": 85, "grievous_hurt": 98, "dowry_deaths":75
        },
        "himachal": {
            "murder": 130, "attempt_to_murder":90, "sexual_harassment": 65,
            "rape": 50, "theft": 120, "hit_and_run":60,"causing_death_by_negligence":120, "culpable_homicide": 96,
            "kidnapping_and_abduction": 70,"arson": 36, "grievous_hurt": 52, "dowry_deaths":20
        }

    },
    "2024": {
        "maharashtra": {
            "murder": 250, "attempt_to_murder": 130, "sexual_harassment": 120,
            "rape": 50, "theft": 200, "hit_and_run": 150, "causing_death_by_negligence": 120, "culpable_homicide": 63,
            "kidnapping_and_abduction": 190,"arson": 65, "grievous_hurt": 110, "dowry_deaths":90
        },
        "uttar_pradesh": {
            "murder": 450, "attempt_to_murder": 230, "sexual_harassment": 260,
            "rape": 150, "theft": 250, "hit_and_run": 150,"causing_death_by_negligence": 93, "culpable_homicide": 110,
            "kidnapping_and_abduction": 320,"arson": 50, "grievous_hurt": 120, "dowry_deaths":63
        },
        "rajsthan": {
            "murder": 263, "attempt_to_murder": 120, "sexual_harassment": 160,
            "rape": 110, "theft": 260, "hit_and_run": 60,"causing_death_by_negligence": 120, "culpable_homicide": 130,
            "kidnapping_and_abduction":120,"arson": 96, "grievous_hurt": 65, "dowry_deaths":36
        },
        "aasam": {
            "murder": 250, "attempt_to_murder": 120, "sexual_harassment": 80,
            "rape": 30, "theft": 160, "hit_and_run": 89,"causing_death_by_negligence":63, "culpable_homicide": 75,
            "kidnapping_and_abduction": 150,"arson": 65, "grievous_hurt": 101, "dowry_deaths": 25
        },
        "jammu_and_kashmir": {
            "murder": 150, "attempt_to_murder":62, "sexual_harassment": 180,
            "rape": 50, "theft": 190, "hit_and_run": 100,"causing_death_by_negligence": 59, "culpable_homicide": 50,
            "kidnapping_and_abduction": 105,"arson": 96, "grievous_hurt": 140, "dowry_deaths": 12
        },
        "Andhra Pradesh": {
            "murder": 300, "attempt_to_murder":120, "sexual_harassment": 196,
            "rape": 96, "theft": 420, "hit_and_run":142,"causing_death_by_negligence": 251, "culpable_homicide": 131,
            "kidnapping_and_abduction": 65,"arson": 96, "grievous_hurt": 115, "dowry_deaths": 101
        },
        "Madhya Pradesh": 
        {
            "murder": 100, "attempt_to_murder":265, "sexual_harassment": 152,
            "rape": 102, "theft": 265, "hit_and_run": 351,"causing_death_by_negligence":125 , "culpable_homicide": 90,
            "kidnapping_and_abduction": 185,"arson": 95, "grievous_hurt": 120, "dowry_deaths": 36
        },
        "Bihar": {
            "murder": 250, "attempt_to_murder":220, "sexual_harassment": 160,
            "rape": 196, "theft": 126, "hit_and_run": 250,"causing_death_by_negligence": 85, "culpable_homicide": 102,
            "kidnapping_and_abduction": 105,"arson":96, "grievous_hurt": 85, "dowry_deaths": 98
        },
        "Punjab": {
            "murder": 120, "attempt_to_murder":95, "sexual_harassment": 120,
            "rape": 150, "theft": 320, "hit_and_run": 120,"causing_death_by_negligence":69, "culpable_homicide": 110,
            "kidnapping_and_abduction": 81,"arson": 95, "grievous_hurt": 120, "dowry_deaths":90
        },
        "Manipur": {
            "murder": 120, "attempt_to_murder":85, "sexual_harassment": 100,
            "rape": 85, "theft":130, "hit_and_run": 195,"causing_death_by_negligence":96, "culpable_homicide": 152,
            "kidnapping_and_abduction": 90,"arson": 56, "grievous_hurt": 52, "dowry_deaths":10
        },
        "harayana": {
            "murder": 230, "attempt_to_murder":120, "sexual_harassment": 32,
            "rape": 133, "theft": 120, "hit_and_run": 190,"causing_death_by_negligence":30, "culpable_homicide": 103,
            "kidnapping_and_abduction": 201,"arson": 75, "grievous_hurt": 105, "dowry_deaths":65
        },
        "west bengal": {
            "murder": 230, "attempt_to_murder":125, "sexual_harassment": 125,
            "rape": 102, "theft":220, "hit_and_run": 165,"causing_death_by_negligence":182, "culpable_homicide": 100,
            "kidnapping_and_abduction": 120,"arson": 123, "grievous_hurt": 85, "dowry_deaths":90
        },
        "himachal": {
            "murder": 253, "attempt_to_murder":190, "sexual_harassment": 75,
            "rape": 126, "theft": 220, "hit_and_run":120,"causing_death_by_negligence":150, "culpable_homicide": 53,
            "kidnapping_and_abduction": 170,"arson": 63, "grievous_hurt": 152, "dowry_deaths":52
        }
    }
}
model = pickle.load(open('crime_prediction_model.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():

    year = request.form['year']
    crime = request.form['crime']
    # Extract the crime data for the selected year
    year_data = crime_data.get(year, {})
    # Prepare the data for plotting
    states = list(year_data.keys())
    crime_rates = [year_data[state].get(crime, 0) for state in states]
    plt.figure(figsize=(10, 5))
    plt.bar(states, crime_rates, color='blue')
    plt.xlabel('States')
    plt.ylabel('Crime Rate')
    plt.title(f'Crime Rate for {crime.replace("_", " ").title()} in {year}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a file
    chart_path = os.path.join('static', 'crime_chart.png')
    # plt.savefig(r"C:\Users\SAYALI\Desktop\Crime Predictions\static")
    plt.savefig(chart_path)
    
    plt.close()

    return render_template('upload.html',chart_url=url_for('static', filename='crime_chart.png'))

if __name__ == '__main__':
    app.run(debug=True)
