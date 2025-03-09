import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Calcolatore FNC Family - Prestazioni, Consumo, Perdite, Portata Aria e Portata Acqua")

# ------------------------------------------------------------------------------
# 1) Dati FNC Family organizzati per Versione e Modello
# I dati sono espressi in:
#   - kW per le prestazioni (Ps, Pc, Ph)
#   - W per il consumo: Pec (Cooling) e PeH (Heating)
#   - kPa per le perdite di carico: Dpc (Cooling) e Dph (Heating)
#   - m³/h per la portata d'aria ("air_flow")
#   - m³/h per la portata d'acqua: q_c (Cooling) e q_h (Heating)
#
# I vettori sono definiti ai punti misurati (alcuni modelli hanno valori differenti).
# ------------------------------------------------------------------------------
fnc_data = {
    "FNC THIN": {
        "400": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.00, 4.00, 5.70],
                "Ps":       [0.68, 2.05, 2.76],
                "Pc":       [0.83, 2.29, 2.94],
                "Pec":      [2.8, 38.9, 122],
                "Dpc":      [11.89, 11.65, 12.11],
                "air_flow": [200, 450, 680],
                "q_c":      [0.143, 0.394, 0.504]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.00, 4.00, 5.70],
                "Ph":       [0.74, 2.87, 3.62],
                "PeH":      [2.8, 42, 124.2],
                "Dph":      [11.89, 11.65, 12.11],
                "air_flow": [200, 450, 680],
                "q_h":      [0.127, 0.500, 0.630]
            }
        },
        "600": {
            "Cooling": {
                "rpm":      [500, 1200, 2200],
                "vsp":      [2.00, 4.00, 7.00],
                "Ps":       [0.59, 1.53, 2.84],
                "Pc":       [0.70, 1.74, 3.32],
                "Pec":      [2.8, 47.5, 121.5],
                "Dpc":      [12.00, 11.70, 12.50],
                "air_flow": [250, 500, 750],
                "q_c":      [0.176, 0.502, 0.616]
            },
            "Heating": {
                "rpm":      [500, 1200, 2200],
                "vsp":      [2.00, 4.00, 7.00],
                "Ph":       [0.81, 2.32, 4.10],
                "PeH":      [2.8, 47.5, 121.5],
                "Dph":      [12.00, 11.70, 12.50],
                "air_flow": [250, 500, 750],
                "q_h":      [0.155, 0.203, 0.287]
            }
        },
        "800": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.00, 4.00, 5.70],
                "Ps":       [1.08, 3.72, 4.25],
                "Pc":       [1.33, 4.45, 4.97],
                "Pec":      [4.2, 56.1, 89.6],
                "Dpc":      [7.00, 7.20, 7.50],
                "air_flow": [250, 500, 750],
                "q_c":      [0.229, 0.774, 0.865]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.00, 4.00, 5.70],
                "Ph":       [1.63, 5.27, 6.04],
                "PeH":      [4.2, 60, 90],
                "Dph":      [7.00, 7.20, 7.50],
                "air_flow": [250, 500, 750],
                "q_h":      [0.210, 0.310, 0.400]
            }
        },
        "1000": {
            "Cooling": {
                "rpm":      [500, 1200, 2150],
                "vsp":      [2.00, 4.00, 6.90],
                "Ps":       [1.45, 4.48, 5.60],
                "Pc":       [1.65, 5.04, 6.16],
                "Pec":      [7, 100, 231],
                "Dpc":      [5.77, 6.00, 6.50],
                "air_flow": [300, 550, 800],
                "q_c":      [0.279, 0.866, 1.057]
            },
            "Heating": {
                "rpm":      [500, 1200, 2150],
                "vsp":      [2.00, 4.00, 6.90],
                "Ph":       [2.43, 6.57, 7.75],
                "PeH":      [7, 103, 234],
                "Dph":      [5.77, 6.00, 6.50],
                "air_flow": [300, 550, 800],
                "q_h":      [0.424, 1.14, 1.353]
            }
        },
        "1200": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.00, 4.00, 5.70],
                "Ps":       [1.84, 6.18, 8.06],
                "Pc":       [2.14, 7.17, 8.89],
                "Pec":      [8.7, 130.8, 362.9],
                "Dpc":      [6.08, 6.20, 6.50],
                "air_flow": [350, 600, 850],
                "q_c":      [0.367, 1.24, 1.521]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.00, 4.00, 5.70],
                "Ph":       [2.89, 8.54, 10.64],
                "PeH":      [8.7, 130.8, 362.9],
                "Dph":      [6.08, 6.20, 6.50],
                "air_flow": [350, 600, 850],
                "q_h":      [0.503, 1.035, 1.140]
            }
        }
    },
    "FNC THIN MULTI": {
        "600/2": {
            "Cooling": {
                "rpm":      [500, 1200, 1950],
                "vsp":      [2.00, 4.00, 6.43],
                "Ps":       [1.11, 2.75, 3.15],
                "Pc":       [1.45, 3.32, 3.79],
                "Pec":      [2.8, 47.5, 121.5],
                "Dpc":      [5.87, 6.00, 6.30],
                "air_flow": [250, 500, 750],
                "q_c":      [0.205, 0.579, 0.724]
            },
            "Heating": {
                "rpm":      [500, 1200, 1950],
                "vsp":      [2.00, 4.00, 6.43],
                "Ph":       [1.55, 3.59, 4.14],
                "PeH":      [2.8, 47.5, 121.5],
                "Dph":      [5.87, 6.00, 6.30],
                "air_flow": [250, 500, 750],
                "q_h":      [0.180, 0.540, 0.680]
            }
        },
        "800/3": {
            "Cooling": {
                "rpm":      [500, 1200, 2050],
                "vsp":      [2.00, 4.00, 6.58],
                "Ps":       [1.53, 3.46, 4.91],
                "Pc":       [1.93, 4.17, 5.54],
                "Pec":      [4.2, 56.1, 89.6],
                "Dpc":      [6.84, 7.00, 7.20],
                "air_flow": [250, 500, 750],
                "q_c":      [0.229, 0.774, 0.865]
            },
            "Heating": {
                "rpm":      [500, 1200, 2050],
                "vsp":      [2.00, 4.00, 6.58],
                "Ph":       [2.10, 4.64, 6.94],
                "PeH":      [4.2, 60, 90],
                "Dph":      [6.84, 7.00, 7.20],
                "air_flow": [250, 500, 750],
                "q_h":      [0.220, 0.600, 0.750]
            }
        },
        "1000/4": {
            "Cooling": {
                "rpm":      [500, 1200, 1950],
                "vsp":      [2.00, 4.00, 6.30],
                "Ps":       [1.77, 4.49, 6.50],
                "Pc":       [2.06, 5.23, 7.14],
                "Pec":      [7, 100, 231],
                "Dpc":      [6.49, 6.70, 7.00],
                "air_flow": [300, 550, 800],
                "q_c":      [0.279, 0.866, 1.057]
            },
            "Heating": {
                "rpm":      [500, 1200, 1950],
                "vsp":      [2.00, 4.00, 6.30],
                "Ph":       [2.61, 6.10, 9.58],
                "PeH":      [7, 103, 234],
                "Dph":      [6.49, 6.70, 7.00],
                "air_flow": [300, 550, 800],
                "q_h":      [0.424, 1.140, 1.350]
            }
        },
        "1200/5": {
            "Cooling": {
                # Per questo modello, il punto massimo è a 2500 rpm.
                "rpm":      [500, 1200, 2500],
                "vsp":      [2.00, 4.00, 7.91],
                "Ps":       [2.19, 5.68, 5.68],
                "Pc":       [2.60, 6.72, 5.93],
                "Pec":      [8.7, 130.8, 350],
                "Dpc":      [5.78, 6.00, 6.20],
                "air_flow": [350, 600, 850],
                "q_c":      [0.367, 1.240, 1.521]
            },
            "Heating": {
                "rpm":      [500, 1200, 2500],
                "vsp":      [2.00, 4.00, 7.91],
                "Ph":       [3.27, 7.68, 8.94],
                "PeH":      [8.7, 130.8, 350],
                "Dph":      [5.78, 6.00, 6.20],
                "air_flow": [350, 600, 850],
                "q_h":      [0.503, 1.035, 1.140]
            }
        }
    },
    "FNC": {
        "400": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ps":       [0.68, 2.05, 2.76],
                "Pc":       [0.83, 2.29, 2.94],
                "Pec":      [2.8, 38.9, 122],
                "Dpc":      [11.89, 11.65, 12.11],
                "air_flow": [200, 450, 680],
                "q_c":      [0.143, 0.394, 0.504]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ph":       [0.74, 2.87, 3.62],
                "PeH":      [2.8, 42, 124.2],
                "Dph":      [11.89, 11.65, 12.11],
                "air_flow": [200, 450, 680],
                "q_h":      [0.127, 0.500, 0.630]
            }
        },
        "600": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ps":       [0.85, 2.48, 3.17],
                "Pc":       [1.02, 2.93, 3.60],
                "Pec":      [2.8, 47.5, 121.5],
                "Dpc":      [12.00, 11.70, 12.50],
                "air_flow": [250, 500, 750],
                "q_c":      [0.176, 0.502, 0.616]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ph":       [1.19, 3.34, 4.17],
                "PeH":      [2.8, 47.5, 121.5],
                "Dph":      [12.00, 11.70, 12.50],
                "air_flow": [250, 500, 750],
                "q_h":      [0.155, 0.203, 0.287]
            }
        },
        "800": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.10, 5.90],
                "Ps":       [1.08, 3.72, 4.25],
                "Pc":       [1.33, 4.45, 4.97],
                "Pec":      [4.2, 56.1, 89.6],
                "Dpc":      [7.00, 7.20, 7.50],
                "air_flow": [250, 500, 750],
                "q_c":      [0.229, 0.774, 0.865]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.10, 5.90],
                "Ph":       [1.63, 5.27, 6.04],
                "PeH":      [4.2, 60, 90],
                "Dph":      [7.00, 7.20, 7.50],
                "air_flow": [250, 500, 750],
                "q_h":      [0.210, 0.310, 0.400]
            }
        },
        "1000": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ps":       [1.45, 4.48, 5.60],
                "Pc":       [1.65, 5.04, 6.16],
                "Pec":      [7, 100, 231],
                "Dpc":      [5.57, 5.80, 6.00],
                "air_flow": [300, 550, 800],
                "q_c":      [0.279, 0.866, 1.057]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ph":       [2.43, 6.57, 7.75],
                "PeH":      [7, 103, 234],
                "Dph":      [5.57, 5.80, 6.00],
                "air_flow": [300, 550, 800],
                "q_h":      [0.424, 1.140, 1.350]
            }
        },
        "1200": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ps":       [1.84, 6.18, 8.06],
                "Pc":       [2.14, 7.17, 8.89],
                "Pec":      [8.7, 130.8, 362.9],
                "Dpc":      [10.86, 11.00, 11.20],
                "air_flow": [350, 600, 850],
                "q_c":      [0.367, 1.240, 1.521]
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 5.80, 9.00],
                "Ph":       [2.89, 8.54, 10.64],
                "PeH":      [8.7, 130.8, 362.9],
                "Dph":      [10.86, 11.00, 11.20],
                "air_flow": [350, 600, 850],
                "q_h":      [0.503, 1.035, 1.140]
            }
        }
    },
    "FNC MULTI": {
        "600/2": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 5.30],
                "Ps":       [1.11, 2.75, 3.15],
                "Pc":       [1.45, 3.32, 3.79],
                "Pec":      [2.8, 47.5, 121.5],
                "Dpc":      [10.25, 10.50, 10.75],
                "air_flow": [250, 500, 750],
                "q_c":      [0.143, 0.394, 0.504]  # ipotetico
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 5.30],
                "Ph":       [1.55, 3.59, 4.14],
                "PeH":      [2.8, 47.5, 121.5],
                "Dph":      [10.25, 10.50, 10.75],
                "air_flow": [250, 500, 750],
                "q_h":      [0.127, 0.500, 0.630]  # ipotetico
            }
        },
        "800/3": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 7.04],
                "Ps":       [1.53, 3.46, 4.91],
                "Pc":       [1.93, 4.17, 5.54],
                "Pec":      [4.2, 56.1, 89.6],
                "Dpc":      [10.88, 11.00, 11.20],
                "air_flow": [250, 500, 750],
                "q_c":      [0.176, 0.502, 0.616]  # ipotetico
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 7.04],
                "Ph":       [2.10, 4.64, 6.94],
                "PeH":      [4.2, 60, 90],
                "Dph":      [10.88, 11.00, 11.20],
                "air_flow": [250, 500, 750],
                "q_h":      [0.155, 0.203, 0.287]  # ipotetico
            }
        },
        "1000/4": {
            "Cooling": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 7.06],
                "Ps":       [1.77, 4.49, 6.50],
                "Pc":       [2.06, 5.23, 7.14],
                "Pec":      [7, 100, 231],
                "Dpc":      [7.24, 7.50, 7.80],
                "air_flow": [300, 550, 800],
                "q_c":      [0.229, 0.774, 0.865]  # ipotetico
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 7.06],
                "Ph":       [2.61, 6.10, 9.58],
                "PeH":      [7, 103, 234],
                "Dph":      [7.24, 7.50, 7.80],
                "air_flow": [300, 550, 800],
                "q_h":      [0.210, 0.310, 0.400]  # ipotetico
            }
        },
        "1200/5": {
            "Cooling": {
                # Per FNC MULTI, il vettore rpm è [500, 1200, 1800]
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 5.30],
                "Ps":       [2.19, 5.68, 6.71],
                "Pc":       [2.60, 6.72, 7.73],
                "Pec":      [8.7, 130.8, 362.9],
                "Dpc":      [6.90, 7.00, 7.10],
                "air_flow": [350, 600, 850],
                "q_c":      [0.367, 1.240, 1.521]  # ipotetico
            },
            "Heating": {
                "rpm":      [500, 1200, 1800],
                "vsp":      [2.20, 4.50, 5.30],
                "Ph":       [3.27, 7.68, 8.94],
                "PeH":      [8.7, 130.8, 362.9],
                "Dph":      [6.90, 7.00, 7.10],
                "air_flow": [350, 600, 850],
                "q_h":      [0.503, 1.035, 1.140]  # ipotetico
            }
        }
    }
}

# ------------------------------------------------------------------------------
# 2) Determinazione del numero di ventilatori in base alla Versione
# ------------------------------------------------------------------------------
def get_ventilator_count(selected_version, selected_model_number):
    if selected_version in ["FNC THIN", "FNC"]:
        if selected_model_number in ["400", "600"]:
            return 1
        elif selected_model_number in ["800", "1000"]:
            return 2
        elif selected_model_number == "1200":
            return 3
    elif selected_version in ["FNC THIN MULTI", "FNC MULTI"]:
        try:
            return int(selected_model_number.split("/")[1])
        except Exception:
            return 1
    return 1

# ------------------------------------------------------------------------------
# 3) Interfaccia di selezione: Versione e Modello
# ------------------------------------------------------------------------------
col_ver, col_mod = st.columns(2)
with col_ver:
    version_options = ["FNC THIN", "FNC THIN MULTI", "FNC", "FNC MULTI"]
    selected_version = st.selectbox("Seleziona Versione", version_options)
with col_mod:
    if selected_version in ["FNC THIN", "FNC"]:
        model_options = ["400", "600", "800", "1000", "1200"]
    else:
        model_options = ["600/2", "800/3", "1000/4", "1200/5"]
    selected_model_number = st.selectbox("Seleziona Modello", model_options)

n_fan = get_ventilator_count(selected_version, selected_model_number)
st.write(f"**Numero Ventilatori:** {n_fan}")

# ------------------------------------------------------------------------------
# 4) Metodo di inserimento: RPM oppure Vsp
# ------------------------------------------------------------------------------
method = st.radio("Metodo di inserimento:", ["Inserisci RPM", "Inserisci Vsp"])

# ------------------------------------------------------------------------------
# 5) Selezione Modalità e scelta del valore RPM/Vsp (continuo)
# ------------------------------------------------------------------------------
col_mode_sel, col_val = st.columns(2)
with col_mode_sel:
    selected_mode = st.selectbox("Modalità", ["Cooling", "Heating"])
with col_val:
    if method == "Inserisci RPM":
        rpm_arr = np.array(fnc_data[selected_version][selected_model_number][selected_mode]["rpm"], dtype=float)
        rpm_input = st.slider("Seleziona RPM", min_value=200, max_value=2600, value=1200, step=1)
    else:
        vsp_arr = np.array(fnc_data[selected_version][selected_model_number][selected_mode]["vsp"], dtype=float)
        vsp_min, vsp_max = float(vsp_arr[0]), float(vsp_arr[-1])
        vsp_input = st.slider("Seleziona Vsp", min_value=vsp_min, max_value=vsp_max, value=float(vsp_arr[1]), step=0.1)
        rpm_arr = np.array(fnc_data[selected_version][selected_model_number][selected_mode]["rpm"], dtype=float)
        poly_vsp_to_rpm = np.poly1d(np.polyfit(vsp_arr, rpm_arr, 1))
        rpm_input = poly_vsp_to_rpm(vsp_input)
        st.write(f"RPM calcolati da Vsp: {rpm_input:.0f} rpm")

# ------------------------------------------------------------------------------
# 6) Input Temperature (°C)
# ------------------------------------------------------------------------------
if selected_mode == "Cooling":
    default_t_in, default_t_out = 7.0, 12.0
else:
    default_t_in, default_t_out = 40.0, 20.0

col_T1, col_T2 = st.columns(2)
with col_T1:
    t_in = st.number_input("Temp. ingresso acqua (°C):", value=default_t_in, step=0.1)
with col_T2:
    t_out = st.number_input("Temp. uscita acqua (°C):", value=default_t_out, step=0.1)

if selected_mode == "Cooling" and t_in >= t_out:
    st.error("In Cooling, la temperatura d'ingresso deve essere inferiore a quella d'uscita.")
    st.stop()
elif selected_mode == "Heating" and t_in < t_out:
    st.error("In Heating, la temperatura d'ingresso deve essere maggiore o uguale a quella d'uscita.")
    st.stop()

# ------------------------------------------------------------------------------
# 7) Interpolazione dei dati in base all'RPM selezionato
# ------------------------------------------------------------------------------
try:
    mode_data = fnc_data[selected_version][selected_model_number][selected_mode]
except KeyError as e:
    st.error(f"Errore nella struttura dei dati: {e}")
    st.stop()

rpm_arr = np.array(mode_data["rpm"], dtype=float)
af_arr  = np.array(mode_data["air_flow"], dtype=float)
poly_af = np.poly1d(np.polyfit(rpm_arr, af_arr, 2))
af_interp = poly_af(rpm_input)

if selected_mode == "Cooling":
    ps_arr = np.array(mode_data["Ps"], dtype=float)
    pc_arr = np.array(mode_data["Pc"], dtype=float)
    pec_arr = np.array(mode_data["Pec"], dtype=float)
    dpc_arr = np.array(mode_data["Dpc"], dtype=float)
    qc_arr = np.array(mode_data["q_c"], dtype=float)
    
    poly_ps = np.poly1d(np.polyfit(rpm_arr, ps_arr, 2))
    poly_pc = np.poly1d(np.polyfit(rpm_arr, pc_arr, 2))
    poly_pec = np.poly1d(np.polyfit(rpm_arr, pec_arr, 2))
    poly_dpc = np.poly1d(np.polyfit(rpm_arr, dpc_arr, 2))
    poly_qc  = np.poly1d(np.polyfit(rpm_arr, qc_arr, 2))
    
    ps_interp = poly_ps(rpm_input)
    pc_interp = poly_pc(rpm_input)
    pec_interp = poly_pec(rpm_input)
    dpc_interp = poly_dpc(rpm_input)
    qc_interp  = poly_qc(rpm_input)
    
    if pc_interp < ps_interp:
        pc_interp = ps_interp
    lat_interp = pc_interp - ps_interp
else:
    ph_arr = np.array(mode_data["Ph"], dtype=float)
    peh_arr = np.array(mode_data["PeH"], dtype=float)
    dph_arr = np.array(mode_data["Dph"], dtype=float)
    qh_arr = np.array(mode_data["q_h"], dtype=float)
    
    poly_ph = np.poly1d(np.polyfit(rpm_arr, ph_arr, 2))
    poly_peh = np.poly1d(np.polyfit(rpm_arr, peh_arr, 2))
    poly_dph = np.poly1d(np.polyfit(rpm_arr, dph_arr, 2))
    poly_qh  = np.poly1d(np.polyfit(rpm_arr, qh_arr, 2))
    
    ph_interp = poly_ph(rpm_input)
    peh_interp = poly_peh(rpm_input)
    dph_interp = poly_dph(rpm_input)
    qh_interp  = poly_qh(rpm_input)

delta_t = abs(t_in - t_out)

# ------------------------------------------------------------------------------
# 8) Visualizzazione dei risultati numerici
# ------------------------------------------------------------------------------
st.subheader("Risultati Interpolati")
if selected_mode == "Cooling":
    st.write(f"**Resa Sensibile (Ps)**: {ps_interp:.2f} kW")
    st.write(f"**Resa Totale (Pc)**: {pc_interp:.2f} kW")
    st.write(f"**Resa Latente (Pc - Ps)**: {lat_interp:.2f} kW")
    st.write(f"**Consumo in Cooling (Pec)**: {pec_interp:.0f} W")
    st.write(f"**Perdite di Carico in Cooling (Dpc)**: {dpc_interp:.2f} kPa")
    st.write(f"**Portata Aria**: {af_interp:.1f} m³/h")
    st.write(f"**Portata Acqua in Cooling (qc)**: {qc_interp:.3f} m³/h")
else:
    st.write(f"**Resa in Heating (Ph)**: {ph_interp:.2f} kW")
    st.write(f"**Consumo in Heating (PeH)**: {peh_interp:.0f} W")
    st.write(f"**Perdite di Carico in Heating (Dph)**: {dph_interp:.2f} kPa")
    st.write(f"**Portata Aria**: {af_interp:.1f} m³/h")
    st.write(f"**Portata Acqua in Heating (qh)**: {qh_interp:.3f} m³/h")

# ------------------------------------------------------------------------------
# 9) Creazione del grafico dei parametri in funzione degli RPM
# ------------------------------------------------------------------------------
rpm_range = np.linspace(200, 2600, 200)
af_range  = poly_af(rpm_range)

if selected_mode == "Cooling":
    ps_range = poly_ps(rpm_range)
    pc_range = poly_pc(rpm_range)
    lat_range = pc_range - ps_range
    pec_range = poly_pec(rpm_range)
    dpc_range = poly_dpc(rpm_range)
    qc_range  = poly_qc(rpm_range)
else:
    ph_range = poly_ph(rpm_range)
    peh_range = poly_peh(rpm_range)
    dph_range = poly_dph(rpm_range)
    qh_range  = poly_qh(rpm_range)

fig, axs = plt.subplots(3, 2, figsize=(14, 12))
if selected_mode == "Cooling":
    # Portata Aria
    axs[0,0].plot(rpm_range, af_range, label="Portata Aria (m³/h)")
    axs[0,0].set_xlabel("RPM")
    axs[0,0].set_ylabel("Portata Aria (m³/h)")
    axs[0,0].legend()
    
    # Prestazioni
    axs[0,1].plot(rpm_range, ps_range, label="Ps (Resa Sensibile)")
    axs[0,1].plot(rpm_range, pc_range, label="Pc (Resa Totale)")
    axs[0,1].plot(rpm_range, lat_range, label="Latente (Pc-Ps)")
    axs[0,1].set_xlabel("RPM")
    axs[0,1].set_ylabel("Resa (kW)")
    axs[0,1].legend()
    
    # Perdite di Carico
    axs[1,0].plot(rpm_range, dpc_range, label="Perdite di Carico (Dpc)")
    axs[1,0].set_xlabel("RPM")
    axs[1,0].set_ylabel("Dpc (kPa)")
    axs[1,0].legend()
    
    # Consumo
    axs[1,1].plot(rpm_range, pec_range, label="Consumo (Pec)")
    axs[1,1].set_xlabel("RPM")
    axs[1,1].set_ylabel("Consumo (W)")
    axs[1,1].legend()
    
    # Portata Acqua
    axs[2,0].plot(rpm_range, qc_range, label="Portata Acqua (qc)")
    axs[2,0].set_xlabel("RPM")
    axs[2,0].set_ylabel("qc (m³/h)")
    axs[2,0].legend()
    
    # ΔT annotato nel grafico
    axs[2,1].axis('off')
    axs[2,1].text(0.1, 0.5, f"Cooling Mode\nΔT = {delta_t:.1f} °C", fontsize=14)
    
    fig.suptitle("Cooling Mode - Curve dei Parametri vs RPM")
    
else:
    # Portata Aria
    axs[0,0].plot(rpm_range, af_range, label="Portata Aria (m³/h)")
    axs[0,0].set_xlabel("RPM")
    axs[0,0].set_ylabel("Portata Aria (m³/h)")
    axs[0,0].legend()
    
    # Prestazioni
    axs[0,1].plot(rpm_range, ph_range, label="Ph (Resa Heating)")
    axs[0,1].set_xlabel("RPM")
    axs[0,1].set_ylabel("Resa (kW)")
    axs[0,1].legend()
    
    # Perdite di Carico
    axs[1,0].plot(rpm_range, dph_range, label="Perdite di Carico (Dph)")
    axs[1,0].set_xlabel("RPM")
    axs[1,0].set_ylabel("Dph (kPa)")
    axs[1,0].legend()
    
    # Consumo
    axs[1,1].plot(rpm_range, peh_range, label="Consumo (PeH)")
    axs[1,1].set_xlabel("RPM")
    axs[1,1].set_ylabel("Consumo (W)")
    axs[1,1].legend()
    
    # Portata Acqua
    axs[2,0].plot(rpm_range, qh_range, label="Portata Acqua (qh)")
    axs[2,0].set_xlabel("RPM")
    axs[2,0].set_ylabel("qh (m³/h)")
    axs[2,0].legend()
    
    # ΔT annotato nel grafico
    axs[2,1].axis('off')
    axs[2,1].text(0.1, 0.5, f"Heating Mode\nΔT = {delta_t:.1f} °C", fontsize=14)
    
    fig.suptitle("Heating Mode - Curve dei Parametri vs RPM")
    
st.pyplot(fig)

st.markdown("""
**Note:**
- I dati sono tratti dalla tabella FNC Family:
  - Prestazioni in kW (Ps, Pc, Ph)
  - Consumo in W (Pec per Cooling, PeH per Heating)
  - Perdite di Carico in kPa (Dpc per Cooling, Dph per Heating)
  - Portata Aria in m³/h
  - Portata Acqua in m³/h (qc in Cooling, qh in Heating)
- I valori sono interpolati (polinomio di 2° grado) a partire dai dati misurati per ciascun modello.
- Se si inserisce Vsp, viene effettuata una conversione lineare per stimare l'RPM.
- Lo slider per RPM va da 200 a 2600; valori fuori dal range dei dati misurati vengono ottenuti per extrapolazione.
- Il numero di ventilatori è determinato in base alla Versione e al Modello selezionato.
- È stata applicata una correzione per garantire che la resa totale (Pc) non sia inferiore a quella sensibile (Ps).
""")
