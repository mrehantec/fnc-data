import streamlit as st

# Dizionario dei dati (da aggiornare con i dati reali, ricordando di usare il punto come separatore decimale)
data = {
    "FNC THIN 400": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.0, 4.0, 5.7],
        "qc": [0.081, 0.165, 0.236],
        "Ps": [0.37, 0.77, 1.13],
        "Pc": [0.47, 0.95, 1.34],
        "Pec": [2.3, 11.2, 36.7],
        "Dpc": [9.1, 10.82, 12.71],
        "qh": [0.086, 0.195, 0.279],
        "Ph": [0.5, 1.14, 1.64],
        "Peh": [2.1, 11.3, 37.0],
        "Dph": [8.4, 10.47, 12.97],
        "Version": "F3P120-EC072",
        "NumVent": 1,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC THIN 600": {
        "RPM": [500, 1200, 2200],
        "Voltage": [2.0, 4.0, 7.0],
        "qc": [0.084, 0.181, 0.322],
        "Ps": [0.41, 0.88, 1.57],
        "Pc": [0.49, 1.05, 1.8],
        "Pec": [2.2, 12.2, 78.8],
        "Dpc": [11.31, 13.47, 14.38],
        "qh": [0.089, 0.219, 0.367],
        "Ph": [0.52, 1.27, 2.19],
        "Peh": [2.0, 12.5, 15.11],
        "Dph": [6.87, 10.65, 15.11],
        "Version": "F3P120-EC072",
        "NumVent": 1,
        "TC_Cooling": [15.4, 16.7, 16.9],
        "TC_Heating": [41.0, 41.6, 42.0]
    },
    "FNC THIN 800": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.0, 4.0, 5.7],
        "qc": [0.16, 0.403, 0.572],
        "Ps": [0.85, 2.1, 3.0],
        "Pc": [0.93, 2.33, 3.25],
        "Pec": [4.2, 25.1, 88.3],
        "Dpc": [6.74, 14.46, 23.34],
        "qh": [0.186, 0.467, 0.661],
        "Ph": [1.08, 2.71, 3.89],
        "Peh": [4.2, 26.3, 87.5],
        "Dph": [7.03, 16.35, 26.79],
        "Version": "F3P120-EC072",
        "NumVent": 2,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC THIN 1000": {
        "RPM": [500, 1200, 2150],
        "Voltage": [2.0, 4.0, 6.9],
        "qc": [0.121, 0.302, 0.592],
        "Ps": [0.59, 1.53, 2.84],
        "Pc": [0.7, 1.74, 3.32],
        "Pec": [3.7, 22.8, 129.4],
        "Dpc": [5.77, 7.94, 4.81],
        "qh": [0.139, 0.398, 0.691],
        "Ph": [0.81, 2.32, 4.1],
        "Peh": [3.8, 22.4, 128.7],
        "Dph": [5.63, 10.08, 4.86],
        "Version": "F3P120-EC072",
        "NumVent": 2,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC THIN 1200": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.0, 4.0, 5.7],
        "qc": [0.179, 0.489, 0.717],
        "Ps": [0.93, 2.48, 3.58],
        "Pc": [1.04, 2.81, 4.04],
        "Pec": [5.8, 40.0, 134.4],
        "Dpc": [6.08, 15.89, 28.71],
        "qh": [0.23, 0.635, 0.909],
        "Ph": [1.33, 3.69, 5.36],
        "Peh": [5.9, 39.5, 136.7],
        "Dph": [7.14, 22.78, 41.17],
        "Version": "F3P120-EC072",
        "NumVent": 3,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC+ THIN 600/2": {
        "RPM": [500, 1200, 1950],
        "Voltage": [2.0, 4.0, 6.43],
        "qc": [0.137, 0.375, 0.539],
        "Ps": [0.41, 0.881, 2.55],
        "Pc": [0.485, 1.048, 3.06],
        "Pec": [2.2, 12.2, 79.7],
        "Dpc": [11.31, 13.47, 36.25],
        "qh": [0.137, 0.375, 0.577],
        "Ph": [0.79, 2.17, 3.39],
        "Peh": [3.4, 17.5, 71.4],
        "Dph": [6.95, 15.95, 35.44],
        "Version": "F3P120-EC072",
        "NumVent": 2,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC+ THIN 800/3": {
        "RPM": [500, 1200, 2050],
        "Voltage": [2.0, 4.0, 6.58],
        "qc": [0.191, 0.493, 0.782],
        "Ps": [0.87, 2.28, 3.72],
        "Pc": [1.1, 2.84, 4.42],
        "Pec": [5.6, 24.6, 135.3],
        "Dpc": [6.84, 16.72, 42.66],
        "qh": [0.23, 0.524, 0.873],
        "Ph": [1.32, 3.03, 5.14],
        "Peh": [5.5, 24.3, 125.0],
        "Dph": [7.9, 16.91, 45.12],
        "Version": "F3P120-EC072",
        "NumVent": 3,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC+ THIN 1000/4": {
        "RPM": [500, 1200, 1950],
        "Voltage": [2.0, 4.0, 6.3],
        "qc": [0.219, 0.649, 0.986],
        "Ps": [1.03, 2.93, 4.57],
        "Pc": [1.27, 3.75, 5.61],
        "Pec": [7.5, 35.7, 140.4],
        "Dpc": [6.49, 22.05, 37.35],
        "qh": [0.23, 0.696, 1.081],
        "Ph": [1.33, 4.04, 6.36],
        "Peh": [6.3, 35.7, 133.1],
        "Dph": [5.6, 23.81, 41.07],
        "Version": "F3P120-EC072",
        "NumVent": 4,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC+ THIN 1200/5": {
        "RPM": [500, 1200, 2500],
        "Voltage": [2.0, 4.0, 7.91],
        "qc": [0.205, 0.551, 1.007],
        "Ps": [0.97, 2.77, 5.68],
        "Pc": [1.19, 3.18, 5.93],
        "Pec": [8.9, 42.8, 344.0],
        "Dpc": [5.78, 12.69, 23.55],
        "qh": [0.256, 0.657, 1.283],
        "Ph": [1.49, 3.82, 6.7],
        "Peh": [8.9, 41.7, 338.0],
        "Dph": [6.4, 17.49, 26.89],
        "Version": "F3P120-EC072",
        "NumVent": 5,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC 400": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.2, 5.8, 9.0],
        "qc": [0.143, 0.394, 0.504],
        "Ps": [0.68, 2.05, 2.76],
        "Pc": [0.83, 2.29, 2.94],
        "Pec": [2.8, 38.9, 122.0],
        "Dpc": [11.89, 12.0, 17.57],
        "qh": [0.127, 0.5, 0.63],
        "Ph": [0.74, 2.87, 3.62],
        "Peh": [2.0, 42.0, 124.0],
        "Dph": [4.97, 16.95, 26.04],
        "Version": "F3P146-EC072",
        "NumVent": 1,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC 600": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.2, 5.8, 9.0],
        "qc": [0.176, 0.502, 0.616],
        "Ps": [0.85, 2.48, 3.17],
        "Pc": [1.02, 2.93, 3.6],
        "Pec": [2.8, 47.5, 121.5],
        "Dpc": [7.39, 24.46, 33.11],
        "qh": [0.205, 0.579, 0.724],
        "Ph": [1.19, 3.34, 4.17],
        "Peh": [2.8, 47.5, 121.5],
        "Dph": [7.86, 26.38, 44.35],
        "Version": "F3P146-EC072",
        "NumVent": 1,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC 800": {
        "RPM": [500, 1100, 1260],
        "Voltage": [2.2, 5.1, 5.9],
        "qc": [0.229, 0.774, 0.865],
        "Ps": [1.08, 3.72, 4.25],
        "Pc": [1.33, 4.45, 4.97],
        "Pec": [4.2, 56.1, 89.6],
        "Dpc": [7.44, 36.42, 35.86],
        "qh": [0.285, 0.906, 1.035],
        "Ph": [1.63, 5.27, 6.04],
        "Peh": [4.3, 55.0, 91.9],
        "Dph": [8.19, 35.86, 47.54],
        "Version": "F3P146-EC072",
        "NumVent": 2,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC 1000": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.2, 5.8, 9.0],
        "qc": [0.279, 0.866, 1.057],
        "Ps": [1.45, 4.48, 5.6],
        "Pc": [1.65, 5.04, 6.16],
        "Pec": [6.4, 99.6, 230.9],
        "Dpc": [5.57, 12.19, 15.8],
        "qh": [0.424, 2.43, 0.0],  # valore mancante, uso 0.0 come placeholder
        "Ph": [2.43, 6.57, 7.75],
        "Peh": [6.4, 99.6, 230.9],  # placeholder
        "Dph": [5.57, 12.19, 15.8],  # placeholder
        "Version": "F3P146-EC072",
        "NumVent": 2,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC 1200": {
        "RPM": [500, 1200, 1800],
        "Voltage": [2.2, 5.8, 9.0],
        # I dati per questo modello non sono completi; uso placeholder 0 per quelli mancanti
        "qc": [0.367, 1.24, 0.0],
        "Ps": [1.84, 6.18, 0.0],
        "Pc": [2.14, 7.17, 0.0],
        "Pec": [0.0, 0.0, 0.0],
        "Dpc": [0.0, 0.0, 0.0],
        "qh": [0.0, 0.0, 0.0],
        "Ph": [0.0, 0.0, 0.0],
        "Peh": [0.0, 0.0, 0.0],
        "Dph": [0.0, 0.0, 0.0],
        "Version": "F3P146-EC072",
        "NumVent": 3,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC MULTI 600/2": {
        "RPM": [500, 1200, 1500],
        "Voltage": [2.2, 4.5, 5.3],
        "qc": [0.249, 0.568, 0.645],
        "Ps": [1.11, 2.75, 3.15],
        "Pc": [1.45, 3.32, 3.79],
        "Pec": [5.2, 38.6, 65.5],
        "Dpc": [10.25, 30.31, 36.36],
        "qh": [0.267, 0.622, 0.722],
        "Ph": [1.55, 3.59, 3.59],
        "Peh": [5.4, 38.2, 38.2],
        "Dph": [13.68, 30.8, 30.8],
        "Version": "F3P133-EC072",
        "NumVent": 2,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC MULTI 800/3": {
        "RPM": [500, 1200, 2050],
        "Voltage": [2.2, 4.5, 7.04],
        "qc": [0.331, 0.715, 0.999],
        "Ps": [1.53, 3.46, 4.91],
        "Pc": [1.93, 4.17, 5.54],
        "Pec": [7.9, 58.6, 281.2],
        "Dpc": [10.88, 32.02, 62.67],
        "qh": [0.366, 0.808, 1.163],
        "Ph": [2.1, 4.64, 6.94],
        "Peh": [8.1, 55.8, 273.1],
        "Dph": [11.13, 36.52, 74.65],
        "Version": "F3P133-EC072",
        "NumVent": 3,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC MULTI 1000/4": {
        "RPM": [500, 1200, 2050],
        "Voltage": [2.2, 4.5, 7.06],
        "qc": [0.344, 0.899, 1.281],
        "Ps": [1.77, 4.49, 6.5],
        "Pc": [2.06, 5.23, 7.14],
        "Pec": [10.5, 68.4, 345.0],
        "Dpc": [7.24, 15.16, 20.36],
        "qh": [0.455, 1.062, 4.598],
        "Ph": [2.61, 6.1, 9.58],
        "Peh": [10.5, 66.9, 357.1],
        "Dph": [6.45, 14.08, 25.97],
        "Version": "F3P133-EC072",
        "NumVent": 4,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    },
    "FNC MULTI 1200/5": {
        "RPM": [500, 1200, 1500],
        "Voltage": [2.2, 4.5, 5.3],
        "qc": [0.448, 1.144, 1.328],
        "Ps": [2.19, 5.68, 6.71],
        "Pc": [2.6, 6.72, 7.73],
        "Pec": [14.6, 97.4, 168.6],
        "Dpc": [6.9, 25.48, 32.52],
        "qh": [0.57, 1.338, 1.565],
        "Ph": [3.27, 7.68, 8.94],
        "Peh": [14.0, 95.1, 160.8],
        "Dph": [8.54, 31.53, 41.11],
        "Version": "F3P133-EC072",
        "NumVent": 5,
        "TC_Cooling": [13.0, 13.6, 14.5],
        "TC_Heating": [40.6, 39.2, 38.2]
    }
}

# Funzioni di interpolazione
def calc_factor(x, low, high):
    if x <= low:
        return 0.0
    elif x >= high:
        return 1.0
    else:
        return (x - low) / (high - low)

def interp_value(factor, low, med, high):
    if factor <= 0:
        return low
    elif factor >= 1:
        return high
    elif factor <= 0.5:
        localF = factor / 0.5
        return low + localF * (med - low)
    else:
        localF2 = (factor - 0.5) / 0.5
        return med + localF2 * (high - med)

import streamlit as st

st.title("Calcolatore Airflow Fan Coil")

# Sidebar per input
st.sidebar.header("Inserisci Parametri")
mode = st.sidebar.selectbox("Modalità", ["Cooling", "Heating"])
model = st.sidebar.selectbox("Modello", list(data.keys()))
Tin = st.sidebar.number_input("T_in Acqua (°C)", value=7.0)
Tout = st.sidebar.number_input("T_out Acqua (°C)", value=12.0)
RPM_input = st.sidebar.number_input("RPM", value=500.0)

model_data = data[model]

factor_rpm = calc_factor(RPM_input, model_data["RPM"][0], model_data["RPM"][-1])
Vdc = interp_value(factor_rpm, model_data["Voltage"][0], model_data["Voltage"][1], model_data["Voltage"][2])

if mode.lower() == "cooling":
    resa_sens = interp_value(factor_rpm, model_data["Ps"][0], model_data["Ps"][1], model_data["Ps"][2])
    resa_tot = interp_value(factor_rpm, model_data["Pc"][0], model_data["Pc"][1], model_data["Pc"][2])
    consumption = interp_value(factor_rpm, model_data["Pec"][0], model_data["Pec"][1], model_data["Pec"][2])
    dp = interp_value(factor_rpm, model_data["Dpc"][0], model_data["Dpc"][1], model_data["Dpc"][2])
    portata_acqua = interp_value(factor_rpm, model_data["qc"][0], model_data["qc"][1], model_data["qc"][2])
else:
    resa_tot = interp_value(factor_rpm, model_data["Ph"][0], model_data["Ph"][1], model_data["Ph"][2])
    consumption = interp_value(factor_rpm, model_data["Peh"][0], model_data["Peh"][1], model_data["Peh"][2])
    dp = interp_value(factor_rpm, model_data["Dph"][0], model_data["Dph"][1], model_data["Dph"][2])
    portata_acqua = interp_value(factor_rpm, model_data["qh"][0], model_data["qh"][1], model_data["qh"][2])
    resa_sens = 0

# Correzione ambientale (solo sui parametri termici)
if mode.lower() == "cooling":
    avgNom = 9.5
    avgUser = (Tin + Tout) / 2
    if avgUser < 0.1:
        avgUser = 0.1
    corr = avgNom / avgUser
    resa_sens = resa_sens * corr
    resa_tot = resa_tot * corr
else:
    avgNom = 42.5
    avgUser = (Tin + Tout) / 2
    if avgUser < 0.1:
        avgUser = 0.1
    corr = avgUser / avgNom
    resa_tot = resa_tot * corr

# Interpolazione T_calc dalla temperatura aria in uscita
if mode.lower() == "cooling":
    T_low = model_data["TC_Cooling"][0]
    T_med = model_data["TC_Cooling"][1]
    T_high = model_data["TC_Cooling"][2]
else:
    T_low = model_data["TC_Heating"][0]
    T_med = model_data["TC_Heating"][1]
    T_high = model_data["TC_Heating"][2]

if T_low == 0 and T_med == 0 and T_high == 0:
    T_calc = 0
else:
    T_calc = interp_value(factor_rpm, T_low, T_med, T_high)

# Calcolo Airflow in m³/h:
if mode.lower() == "cooling":
    T_env = 27.0
    if (T_env - T_calc) > 0:
        airflow = (resa_sens) / (1.2 * (T_env - T_calc)) * 3600
    else:
        airflow = 0
else:
    T_env = 20.0
    if (T_calc - T_env) > 0:
        airflow = (resa_tot) / (1.2 * (T_calc - T_env)) * 3600
    else:
        airflow = 0

st.header("Risultati")
st.write("Vdc:", round(Vdc, 2))
if mode.lower() == "cooling":
    st.write("Resa Sensibile (Ps):", round(resa_sens, 3))
    st.write("Resa Totale (Pc):", round(resa_tot, 3))
else:
    st.write("Resa Totale (Ph):", round(resa_tot, 3))
st.write("Portata Acqua:", round(portata_acqua, 3))
st.write("Perdita di Carico (DP):", round(dp, 3))
st.write("Airflow (m³/h):", round(airflow, 2))
st.write("Tipo Ventilatore:", model_data["Version"])
st.write("Numero di Ventilatori:", model_data["NumVent"])
st.write("Consumo Elettrico:", round(consumption, 3))
st.write("T_calc (T°C aria in uscita):", round(T_calc, 2))
