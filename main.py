import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def get_salary_data():
    filename = "./datasets/salary_data.csv"

    df = pd.read_csv(filename)
    df = df.sort_values("YearsExperience")

    service = df["YearsExperience"].to_numpy()
    salaries = df["Salary"].to_numpy()
    
    five_years = df[df["YearsExperience"] > 5]["Salary"].to_numpy()

    mean_salary = np.median(salaries)
    mean_service = np.median(service)
    five_mean = np.median(five_years)
    
    colors = cm.viridis(np.linspace(0, 1, len(salaries)))
    plt.figure(figsize=(10, 6))
    plt.bar(service, salaries, color=colors, width=0.2)
    plt.title("Salaries based on the years")

    plt.xlabel("Years")
    plt.ylabel("Salary")

    plt.grid()

    plt.subplots_adjust(bottom=0.25) 

    plt.figtext(0.1, 0.02, f"Mean Salary: ${mean_salary:.2f}", fontsize=10)
    plt.figtext(0.1, 0.05, f"Mean Salary (5+ years): ${five_mean:.2f}", fontsize=10)
    plt.figtext(0.1, 0.08, f"Mean Years of Experience: {mean_service:.2f} years", fontsize=10)

    plt.show()


def get_salary_aumento():
    filename = "./datasets/salary_data.csv"

    df = pd.read_csv(filename)
    df = df.sort_values("YearsExperience")

    service = df["YearsExperience"].to_numpy()
    salaries = df["Salary"].to_numpy() * 1.1
    

    five_years = df[df["YearsExperience"] > 5]["Salary"].to_numpy()

    mean_salary = np.median(salaries)
    mean_service = np.median(service)
    five_mean = np.median(five_years)
    
    colors = cm.viridis(np.linspace(0, 1, len(salaries)))
    plt.figure(figsize=(10, 6))
    plt.bar(service, salaries, color=colors, width=0.2)
    plt.title("Salaries based on the years (aumento 10%)")

    plt.xlabel("Years")
    plt.ylabel("Salary")

    plt.grid()

    plt.subplots_adjust(bottom=0.25)

    plt.figtext(0.1, 0.02, f"Mean Salary: ${mean_salary:.2f}", fontsize=10)
    plt.figtext(0.1, 0.05, f"Mean Salary (5+ years): ${five_mean:.2f}", fontsize=10)
    plt.figtext(0.1, 0.08, f"Mean Years of Experience: {mean_service:.2f} years", fontsize=10)

    plt.show()


    
    

get_salary_data()
get_salary_aumento()

