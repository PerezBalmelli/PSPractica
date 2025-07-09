import wfdb
import numpy as np
from scipy.signal import find_peaks

# --- (Reutilizamos parte del código anterior para obtener los intervalos R-R) ---

# --- 1. Cargar la señal ECG ---
try:
    record = wfdb.rdrecord('100', pn_dir='mitdb')
    ecg_signal = record.p_signal[:, 0]  # Usar el primer canal
    fs = record.fs  # Frecuencia de muestreo
    # print(f"Señal ECG cargada: {len(ecg_signal)} muestras, Fs: {fs} Hz") # Ya mostrado antes
except Exception as e:
    print(f"Error al cargar la señal desde PhysioNet: {e}")
    exit()

# --- 2. Detectar los Picos R ---
min_peak_height = 0.5  # mV (ajustar según la señal)
min_peak_distance = int(fs * 0.25)  # Muestras

r_peaks_indices, _ = find_peaks(ecg_signal, height=min_peak_height, distance=min_peak_distance)

if len(r_peaks_indices) < 10:  # Necesitamos un número razonable de picos para un CV significativo
    print("No se detectaron suficientes picos R para un análisis de irregularidad fiable.")
    # En un caso real, podríamos querer que esto devuelva "No se puede determinar" o similar.
    # Para este ejemplo, si no hay suficientes picos, diremos que no se detecta basado en este método.
    arrhythmia_detected_heuristic = False
    reason = "Pocos picos R detectados."
else:
    # print(f"Número de picos R detectados: {len(r_peaks_indices)}") # Ya mostrado antes

    # --- 3. Calcular los Intervalos R-R en segundos ---
    rr_intervals_samples = np.diff(r_peaks_indices)
    rr_intervals_seconds = rr_intervals_samples / fs

    if len(rr_intervals_seconds) < 5:  # Necesitamos algunos intervalos para un CV significativo
        print("No hay suficientes intervalos R-R para un análisis de irregularidad fiable.")
        arrhythmia_detected_heuristic = False
        reason = "Pocos intervalos R-R."
    else:
        # --- Heurística para detección de "arritmia" basada en irregularidad R-R ---
        mean_rr = np.mean(rr_intervals_seconds)
        std_rr = np.std(rr_intervals_seconds)

        if mean_rr == 0:  # Evitar división por cero
            cv_rr = np.inf
        else:
            cv_rr = std_rr / mean_rr

        # Umbral arbitrario para el coeficiente de variación.
        # Un CV > 0.10 (10%) a veces se considera como indicativo de irregularidad significativa.
        # Este umbral NO es universal ni clínicamente validado para todas las arritmias.
        # Es solo para este ejercicio demostrativo.
        threshold_cv = 0.10

        print(f"\nAnálisis de Irregularidad R-R (Heurístico):")
        print(f"  - Media de Intervalos R-R: {mean_rr:.3f} s")
        print(f"  - Desviación Estándar de Intervalos R-R: {std_rr:.3f} s")
        print(f"  - Coeficiente de Variación (CV) de R-R: {cv_rr:.3f} ({cv_rr * 100:.1f}%)")
        print(f"  - Umbral de CV para 'arritmia' (ejemplo): {threshold_cv:.3f} ({threshold_cv * 100:.1f}%)")

        if cv_rr > threshold_cv:
            arrhythmia_detected_heuristic = True
            reason = f"Coeficiente de Variación de R-R ({cv_rr:.3f}) excede el umbral ({threshold_cv:.3f})."
        else:
            arrhythmia_detected_heuristic = False
            reason = f"Coeficiente de Variación de R-R ({cv_rr:.3f}) no excede el umbral ({threshold_cv:.3f})."

# --- Resultado de la Detección Heurística ---
print("\n--- Resultado de Detección Heurística de Arritmia ---")
if arrhythmia_detected_heuristic:
    print(">> Arritmia detectada (basado en heurística de irregularidad R-R).")
else:
    print(">> No se detectó arritmia significativa (basado en heurística de irregularidad R-R).")
print(f"   Motivo: {reason}")

print("\n**ADVERTENCIA IMPORTANTE:**")
print("Este resultado es producto de una REGLA HEURÍSTICA MUY SIMPLIFICADA y NO CONSTITUYE UN DIAGNÓSTICO MÉDICO.")
print(
    "La detección de arritmias es una tarea compleja que requiere evaluación por profesionales médicos y herramientas adecuadas.")
print(
    "El registro '100' de MIT-BIH contiene Contracciones Ventriculares Prematuras (PVCs), que son un tipo de arritmia.")
print(
    "El objetivo de este script es meramente educativo para ilustrar cómo se podría cuantificar la irregularidad del ritmo.")
print("NO UTILICE ESTE CÓDIGO NI SUS RESULTADOS PARA TOMAR DECISIONES CLÍNICAS.")