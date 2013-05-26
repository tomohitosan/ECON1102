# Filename: run.py
# Author: Tomohito Okabe
# Date: May 24, 2013

# Import NUMPY and MATPLOTLIB libraries
import numpy as np
import matplotlib.pyplot as plt
from IS_PC_MP import ISPCMP


# Set parameters
nu, b_bar, r_bar, pi_bar = 0.1, 2, 0.03, 0.01

# Set baseline
Y_ini = 0
R_ini = r_bar
pi_ini = pi_bar
a_c_ini, a_g_ini, a_ex_ini, a_im_ini, a_i_ini = 0, 0, 0, 0, 0 
omicron_ini = 0
i_ini = R_ini + pi_ini


# Set monetary policy and shock
omicron = 0.1
a_c_new, a_g_new, a_ex_new, a_im_new, a_i_new = 0, 0, 0, 0, 0
i_MP = 5*i_ini



Q = ISPCMP(Y_ini, R_ini, pi_ini, omicron_ini, a_c_ini, a_g_ini, a_ex_ini, 
           a_im_ini, a_i_ini, i_ini, nu, b_bar, r_bar, pi_bar)

fig, ((ax_ISMP,ax_i, ax_Y), (ax_PC, ax_R, ax_pi)) = plt.subplots(2,3)
x = np.linspace(-0.99, 0.99, 1000)
ax_ISMP.axis([-1, 1, -1, 1])
ax_ISMP.set_title('IS-MP diagram')
ax_ISMP.set_xlabel(r'$\tilde{Y}$')
ax_ISMP.set_ylabel(r'$R$')
ax_ISMP.plot(0*x, x*Q.r_bar*1000, 'k--' )

ax_PC.axis([-1, 1, -1, 1])
ax_PC.set_title('PC diagram')
ax_PC.set_xlabel(r'$\tilde{Y}$')
ax_PC.set_ylabel(r'$\Delta \pi$')
x1 = np.linspace(-1, 0, 500)
ax_PC.plot(0*x1, x1, 'k--' )
ax_PC.plot(x1, 0*x1, 'k--')

ax_i.axis([0, 20, -1, 1])
ax_i.set_title('Time path $i_t$')

ax_Y.axis([0, 20, -1, 1])
ax_Y.set_title('Time path' r'$\tilde{Y}_t$')

ax_R.axis([0, 20, -1, 1])
ax_R.set_title('Time path $R_t$')

ax_pi.axis([0, 20, -1, 1])
ax_pi.set_title('Time path $\pi_t$')



pi_last = pi_ini

time = []
i_path = []
Y_path = []
R_path = []
pi_path = []

for t in range(20):
    time.append(t) 

    Q.update_para(t, a_c_new, a_g_new, a_ex_new, a_im_new, a_i_new, omicron, i_MP)
    Q.update_var(t)

    IS = -x/Q.b_bar + Q.a_bar()/Q.b_bar + Q.r_bar   
    MP = x*0 + Q.R
    PC = Q.nu*x + Q.omicron

    if t == 0:
        IS_curve, = ax_ISMP.plot(x, IS, '-r', linewidth=2, label='IS', alpha=0.6)
        MP_curve, = ax_ISMP.plot(x, MP, '-b', linewidth=2, label='MP', alpha=0.6)
        point_ISMP, = ax_ISMP.plot(Q.Y, Q.R, 'og', markersize=8)
        ax_ISMP.legend(loc='upper right', fontsize=10)

        P_curve, = ax_PC.plot(x, PC, '-m', linewidth=2, label='PC', alpha=0.6)
        point_PC, = ax_PC.plot(Q.Y, Q.pi - pi_last, 'og', markersize=8) 
        

    else:
        IS_curve.set_data(x, IS)
        MP_curve.set_data(x, MP)
        point_ISMP.set_data(Q.Y, Q.R)
      
        P_curve.set_data(x, PC)
        point_PC.set_data(Q.Y,  -pi_last + Q.pi)

    i_path.append(Q.i)
    ax_i.plot(time, i_path, 'oc', linewidth=2)
    
    Y_path.append(Q.Y)
    ax_Y.plot(time, Y_path, 'oc', linewidth=2)    
    
    R_path.append(Q.R)
    ax_R.plot(time, R_path, 'oc', linewidth=2)    

    pi_path.append(Q.pi)
    ax_pi.plot(time, pi_path, 'oc', linewidth=2)    

    pi_last = Q.pi
    plt.pause(0.5)
    fig.show()
