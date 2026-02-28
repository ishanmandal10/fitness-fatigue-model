
# Fatigue Modeling During Endurance Running

## What This Project Does

This project simulates a 60-minute steady endurance run and models how fatigue develops over time.

It:

- Generates a simulated heart rate signal  
- Adds noise and slight drift to mimic wearable measurements  
- Uses a simple manually implemented 1D Kalman filter to estimate the underlying heart rate  
- Computes heart rate variability (HRV) using a rolling window  
- Detects fatigue onset based on sustained HRV decline  

A simple regression model is also used to observe the overall HRV trend, but the main focus of the project is signal estimation using a Kalman filter.

In this simulation, fatigue onset was detected at around 30 minutes into the run.

---

## Why I Built This

I run/walk around 10 km, 4–5 days a week. Over time, I became curious about how fatigue builds up during longer steady efforts.

My fitness band shows heart rate and other metrics, but I started wondering, instead of just looking at raw heart rate numbers, I wanted to explore how filtering and structured modeling could help estimate the true physiological state behind noisy measurements.

This project is a small exploration of that idea.

---

## Modeling Assumptions

Since this is a simulation, I chose reasonable values for heart rate, variability, and noise.

The model includes:

- A moderate baseline heart rate (steady 10 km effort)
- A gradual increase over time to represent fatigue
- A slow drop in HRV during sustained effort
- Random Gaussian noise to mimic motion artifacts
- A small drift term to simulate wearable sensor shift

The overall pattern felt directionally similar to what I usually see on my wrist fitness band during longer runs — not accurate, but close enough to make the modeling meaningful.

The goal wasn’t to perfectly match real-world data, but to explore how signal estimation behaves under realistic endurance dynamics.

## Results

The heart rate graph showed a gradual upward trend over the 60-minute run, representing increasing fatigue. The raw measured signal was noisy, but after applying the Kalman filter, the estimated heart rate became much smoother while still preserving the overall upward progression.

The HRV graph showed a gradual decline over time, which aligns with how variability typically reduces during prolonged effort. After smoothing the HRV signal, a sustained drop was observed around the 30-minute mark, which was marked as fatigue onset in this simulation.

The regression line captured the overall downward trend in HRV (R² ≈ 0.6), indicating a clear fatigue-driven pattern while still preserving short-term fluctuations.

---

## What I Learned

- Raw wearable signals can be misleading without filtering.
- State estimation is more appropriate than simple smoothing for noisy data.
- HRV decline can act as a reasonable fatigue proxy.
- Even simple models can capture meaningful physiological trends.

---

## Future Improvements

- Add multi-sensor simulation (e.g., accelerometer)
- Compare Kalman filter with moving average
- Try nonlinear state modeling
- Test against real workout data
