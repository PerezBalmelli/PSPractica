import wfdb
import numpy as np

# Cargar señal del paciente 100 desde PhysioNet
record = wfdb.rdrecord('100', pn_dir='mitdb')  # Descarga automática

# Extraer una sola señal (canal 0) y convertir a array
ecg = record.p_signal[:, 0]  # Canal 0 (puede cambiar según el caso)
fs = record.fs  # Frecuencia de muestreo

from scipy.io.wavfile import write

# Normalizar la señal ECG para convertirla a int16 (formato estándar en WAV)
ecg_normalized = ecg / np.max(np.abs(ecg))  # entre -1 y 1
ecg_int16 = np.int16(ecg_normalized * 32767)

# Guardar como archivo .wav
write('ecg.wav', int(fs), ecg_int16)
print("Archivo ECG guardado como ecg.wav")


