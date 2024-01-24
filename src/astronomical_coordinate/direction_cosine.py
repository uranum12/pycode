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

sin_alpha = np.sin(alpha)
cos_alpha = np.cos(alpha)
sin_delta = np.sin(delta)
cos_delta = np.cos(delta)
sin_phi = np.sin(phi)
cos_phi = np.cos(phi)
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)

m1 = np.matrix(
    [
        [cos_delta * cos_alpha],
        [cos_delta * sin_alpha],
        [sin_delta],
    ],
)

m2 = np.matrix(
    [
        [cos_theta, sin_theta, 0],
        [-sin_theta, cos_theta, 0],
        [0, 0, 1],
    ],
)

m3 = np.dot(m2, m1)

m4 = np.matrix(
    [
        [sin_phi, 0, -cos_phi],
        [0, 1, 0],
        [cos_phi, 0, sin_phi],
    ],
)

m5 = np.dot(m4, m3)

tan_la = m5[1, 0] / -m5[0, 0]

la_prime = np.arctan(tan_la)

if -m5[0, 0] < 0:  # 第2、第3象限
    la = la_prime + np.radians(180)
elif m5[1, 0] < 0:  # 第4象限
    la = la_prime + np.radians(360)
else:  # 第1象限
    la = la_prime

h = np.arcsin(m5[2, 0])

azimuth = np.rad2deg(la)
altitude = np.rad2deg(h)

print(f"天体の赤経         : {right_ascension} [°]")
print(f"天体の赤緯         : {declination} [°]")
print(f"観測地の緯度       : {latitude} [°]")
print(f"観測時の地方恒星時 : {sidereal_time} [°]")

print(f"alpha              : {alpha} [rad]")
print(f"delta              : {delta} [rad]")
print(f"phi                : {phi} [rad]")
print(f"theta              : {theta} [rad]")

print(f"sin alpha          : {sin_alpha} [rad]")
print(f"cos alpha          : {cos_alpha} [rad]")
print(f"sin delta          : {sin_delta} [rad]")
print(f"cos delta          : {cos_delta} [rad]")
print(f"sin phi            : {sin_phi} [rad]")
print(f"cos phi            : {cos_phi} [rad]")
print(f"sin theta          : {sin_theta} [rad]")
print(f"cos theta          : {cos_theta} [rad]")

print(f"m1 :\n{m1}")
print(f"m2 :\n{m2}")
print(f"m3 :\n{m3}")
print(f"m4 :\n{m4}")
print(f"m5 :\n{m5}")

print(f"tan A              : {tan_la} [rad]")
print(f"A prime            : {la_prime} [rad]")
print(f"A                  : {la} [rad]")

print(f"h                  : {h} [rad]")

print(f"天体の方位角       : {azimuth} [°]")
print(f"天体の高度         : {altitude} [°]")
