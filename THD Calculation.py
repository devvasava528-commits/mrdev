import numpy as np
import matplotlib.pyplot as plt

Vm = 325
f = 50
t = np.linspace(0,1,10000)

V_f = Vm*np.sin(2*np.pi*f*t)
V_d = Vm*np.sin(2*np.pi*f*t) + 1/6*Vm*np.sin(2*2*np.pi*f*t - np.pi) + 1/8*Vm*np.sin(4*2*np.pi*f*t - np.pi/3)
V_f_fd = np.fft.fft(V_f)
V_d_fd = np.fft.fft(V_d)
V_p_fd_pol = np.sqrt(np.real(V_f_fd)**2 + np.imag(V_f_fd)**2)
V_d_fd_pol = np.sqrt(np.real(V_d_fd)**2 + np.imag(V_d_fd)**2)

V_f_RMS = np.sqrt(np.mean(V_f**2))
V_d_RMS = np.sqrt(np.mean(V_d**2))

THD = (np.sqrt(np.mean((V_f - V_d)**2)))/np.sqrt(np.mean(V_f**2))
THD_pr = THD*100

print("Vf_RMS:",np.round(V_f_RMS,1),"V")
print("Vd_RMS:",np.round(V_d_RMS,1),"V")
print("THD:",np.round(THD,3))
print("THD%:",np.round(THD_pr,3),"%")

plt.subplot(2,1,1)
plt.title('Fundamental sinewave')
plt.ylabel('Amplitude')
plt.xlabel('Time(s)')
plt.plot(t,V_f, color='b', label='THD:0%')
plt.xlim(0,0.06)
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.title('Distorted sinewave')
plt.ylabel('Amplitude')
plt.xlabel('Time(s)')
plt.plot(t,V_d, color='b', label= f'THD:{np.round(THD_pr,2)}%')
plt.xlim(0,0.06)
plt.legend()
plt.grid()

plt.legend()
plt.tight_layout()
plt.show()

plt.subplot(2,1,1)
plt.title('Frequency Domain')
plt.ylabel('Amplitude')
plt.xlabel('Frequency(Hz)')
plt.plot(V_p_fd_pol, color='r')
plt.xlim(0,250)
plt.grid()

plt.subplot(2,1,2)
plt.ylabel('Amplitude')
plt.xlabel('Frequency(Hz)')
plt.plot(V_d_fd_pol, color='r')
plt.xlim(0,250)
plt.grid()

plt.tight_layout()
plt.show()
