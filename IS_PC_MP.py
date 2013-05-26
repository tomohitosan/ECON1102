# Filename: IS_PC_MP.py
# Author: Tomohito Okabe
# Date: May 24, 2013

class ISPCMP:
    
    def __init__(self, Y, R, pi, omicron, a_c, a_g, a_ex, a_im, a_i, i, nu, 
                b_bar, r_bar, pi_bar):
        self.Y, self.R, self.pi = Y, R, pi
        self.omicron, self.a_c, self.a_g, self.a_ex, self.a_im, self.a_i, \
        self.i = omicron, a_c, a_g, a_ex, a_im, a_i, i
        self.nu, self.b_bar, self.r_bar, self.pi_bar = nu, b_bar, r_bar, pi_bar 

    
    def a_bar(self):
        a_bar = self.a_c + self.a_g + self.a_ex - self.a_im + self.a_i 
        return a_bar
    
    def update_para(self, t, a_c_new, a_g_new, a_ex_new, a_im_new, a_i_new, 
                    omicron, i_MP):
                        
        # Price Shock (i.e. omicron) takes a postive/ negative value just at
        # t=1, and becomes zero on/after t=2.
        # Demand shock (i.e. a_c/a_g/a_ex/ a_im/a_i) keep values between t=1  
        # and t=4, and become zero on/ after t=5.
        # MP is set between t=1 and t=4, and reset to passive policy
        # (i.e. i = r_bar - pi_bar).
                
        if t == 1: 
            self.omicron = omicron
            self.a_c = a_c_new
            self.a_g = a_g_new
            self.a_ex = a_ex_new
            self.a_im = a_im_new
            self.a_i = a_i_new
            self.i = i_MP
            
        if t == 2:
            self.omicron = 0

        if t == 5:
            self.a_c = 0
            self.a_g = 0
            self.a_ex = 0
            self.a_im = 0
            self.a_i = 0
            self.i = self.r_bar + self.pi_bar
            

    def update_var(self, t):
        if t >= 1:
            self.R = self.i - self.pi
            self.Y = self.a_bar() - self.b_bar*(self.R - self.r_bar)
            delta_pi = self.nu*self.Y + self.omicron
            self.pi = delta_pi + self.pi

        