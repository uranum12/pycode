import numpy as np

# 天体の赤経 [°]
right_ascension = 316.166396

# 天体の赤緯 [°]
declination = 38.499750

# 観測地の緯度 [°]
latitude = 35.788889

# 観測時の地方恒星時 [°]
sidereal_time = 223.032708

alpha = np.deg2rad(right_ascension)
delta = np.deg2rad(declination)
phi = np.deg2rad(latitude)
theta = np.deg2rad(sidereal_time)

H = theta - alpha

sin_delta = np.sin(delta)
cos_delta = np.cos(delta)
sin_phi = np.sin(phi)
cos_phi = np.cos(phi)
sin_H = np.sin(H)
cos_H = np.cos(H)

cos_h_sin_A = -cos_delta * sin_H
cos_h_cos_A = sin_delta * cos_phi - cos_delta * sin_phi * cos_H
tan_A = cos_h_sin_A / cos_h_cos_A

A_prime = np.arctan(tan_A)

if cos_h_cos_A < 0:  # 第2、第3象限
    A = A_prime + np.deg2rad(180)
elif cos_h_sin_A < 0:  # 第4象限
    A = A_prime + np.deg2rad(360)
else:  # 第1象限
    A = A_prime

sin_h = sin_delta * sin_phi + cos_delta * cos_phi * cos_H

h = np.arcsin(sin_h)

azimuth = np.rad2deg(A)
altitude = np.rad2deg(h)

print(f"天体の赤経         : {right_ascension} [°]")
print(f"天体の赤緯         : {declination} [°]")
print(f"観測地の緯度       : {latitude} [°]")
print(f"観測時の地方恒星時 : {sidereal_time} [°]")

print(f"alpha              : {alpha} [rad]")
print(f"delta              : {delta} [rad]")
print(f"phi                : {phi} [rad]")
print(f"theta              : {theta} [rad]")

print(f"H                  : {H} [rad]")

print(f"sin delta          : {sin_delta} [rad]")
print(f"cos delta          : {cos_delta} [rad]")
print(f"sin phi            : {sin_phi} [rad]")
print(f"cos phi            : {cos_phi} [rad]")
print(f"sin H              : {sin_H} [rad]")
print(f"cos H              : {cos_H} [rad]")

print(f"cos h sin A        : {cos_h_sin_A} [rad]")
print(f"cos h cos A        : {cos_h_cos_A} [rad]")
print(f"tan A              : {tan_A} [rad]")
print(f"A prime            : {A_prime} [rad]")
print(f"A                  : {A} [rad]")

print(f"sin h              : {sin_h} [rad]")
print(f"h                  : {h} [rad]")

print(f"天体の方位角       : {azimuth} [°]")
print(f"天体の高度         : {altitude} [°]")
