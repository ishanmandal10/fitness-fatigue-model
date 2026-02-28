
"""
Fatigue Modeling During Endurance Running
Author: Ishan Mandal

Simulates a 60-minute run, applies Kalman filtering to estimate
true heart rate from noisy measurements, computes HRV,
and detects fatigue onset.
"""
import numpy as np
import matplotlib.pyplot as plt

# Total duration = 60 minutes
total_time = 3600

# 2000 time samples
time = np.linspace(0, total_time, 2000)
# Heart rate slowly increases due to fatigue
fatigue_increase = 0.01 * time

# Variability reduces over time 
hr_variation = 6 - 0.0015 * time

# True heart rate signal
true_heart_rate = 135 + fatigue_increase + hr_variation * np.sin(0.02 * time)
# Random motion noise
noise = np.random.normal(0, 5, len(time))

# Sensor drift
drift = 0.0005 * time

# Measured heart rate (what wearable sees)
measured_heart_rate = true_heart_rate + noise + drift

plt.figure()
plt.plot(time/60, measured_heart_rate)
plt.xlabel("Time (minutes)")
plt.ylabel("Heart Rate (BPM)")
plt.title("Measured Heart Rate (Noisy)")
plt.show()

# Calculate HRV (rolling standard deviation)


window_size = 100
hrv_values = []

for i in range(len(estimated_heart_rate) - window_size):

    segment = estimated_heart_rate[i : i + window_size]

    std_value = np.std(segment)

    hrv_values.append(std_value)

hrv_values = np.array(hrv_values)

print("HRV calculated. Length:", len(hrv_values))

plt.figure()
plt.plot(time[:len(hrv_values)]/60, hrv_values)
plt.xlabel("Time (minutes)")
plt.ylabel("HRV (Std Dev)")
plt.title("Heart Rate Variability Over Time")
plt.show()

# Smooth HRV before detection


smoothed_hrv = []

smooth_window = 50

for i in range(len(hrv_values) - smooth_window):
    segment = hrv_values[i : i + smooth_window]
    smoothed_hrv.append(np.mean(segment))

smoothed_hrv = np.array(smoothed_hrv)


# Detect fatigue onset


threshold = np.percentile(smoothed_hrv, 30)

fatigue_index = 0

for i in range(len(smoothed_hrv)):
    if smoothed_hrv[i] < threshold:
        fatigue_index = i
        break

fatigue_time = time[fatigue_index] / 60

print("Estimated Fatigue Onset (minutes):", round(fatigue_time, 2))

from sklearn.linear_model import LinearRegression

time_feature = time[:len(smoothed_hrv)].reshape(-1,1)

target = smoothed_hrv

model = LinearRegression()
model.fit(time_feature, target)

predicted_hrv = model.predict(time_feature)

plt.figure()
plt.plot(time_feature/60, smoothed_hrv, label="Actual HRV")
plt.plot(time_feature/60, predicted_hrv, label="Regression Fit")
plt.xlabel("Time (minutes)")
plt.ylabel("HRV")
plt.legend()
plt.title("HRV Trend Modeling")
plt.show()

print("Regression R^2 score:", model.score(time_feature, target))

