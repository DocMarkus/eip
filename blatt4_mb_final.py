import time
import numpy
import math

if __name__ == '__main__':
    from jguvc_eip import basic_io as bio
    from jguvc_eip.colors import *
    from jguvc_eip import image_objects

    print ("Aufgabe Nr.:")
    aufgabe = input()

    # Aufgabe 1 Auto
    if (aufgabe == "1"):
        print ("davor -> 'v' / dahinter -> 'h' / statisch -> 's'")
        wolang = input()
        car_x = 100
        car_y = 200

        bio.start()
        while (car_x < 700):
            if (wolang == "v"):
                bio.draw_polygon ([(400, 180), (400, 230), (500, 230), (500, 180), (450, 160)], BLUE)
            bio.draw_rectangle (car_x, car_y, 100, 30, fill_color=RED, border_color=BLACK)
            bio.draw_circle (car_x + 20, car_y + 30, 15, fill_color=BLACK, border_color=BLACK, border_thickness=1)
            bio.draw_circle (car_x + 80, car_y + 30, 15, fill_color=BLACK, border_color=BLACK, border_thickness=1)
            if (wolang == "h"):
                bio.draw_polygon ([(400, 180), (400, 230), (500, 230), (500, 180), (450, 160)], BLUE)
            elif (wolang == "s"):
                bio.draw_polygon ([(400, 180), (400, 230), (500, 230), (500, 180), (450, 160)], BLUE)
                bio.wait_close ()
                break
            car_x += 1
            time.sleep (0.016)
            bio.clear_image ()
        bio.close_and_exit()

    # Aufgabe 2 Windrad
    if (aufgabe == "2"):
        
        # Zentrum
        x_c = 320   # x Zentrum
        y_c = 140   # y Zentrum
        g= 1        # Maßstab

        def point_rot (x_0, y_0, p_angle):
            p_angle = p_angle*2*math.pi/360 
            x_1 = ((x_0 - x_c)*numpy.cos(p_angle)) - ((y_0 - y_c)*numpy.sin(p_angle)) + x_c
            y_1 = ((x_0 - x_c)*numpy.sin(p_angle)) + ((y_0 - y_c)*numpy.cos(p_angle)) + y_c
            return (int(x_1), int(y_1))
            
        def draw_rot_rectangle(x_r, y_r, angle):
            # x_r = 280, y_r = 180, Ecke links unten
            bio.draw_polygon ([point_rot(x_r, y_r, angle), point_rot(x_r+(80*g), y_r, angle), point_rot(x_r+(80*g), y_r-(80*g), angle), point_rot(x_r, y_r-(80*g), angle)], fill_color=None, border_thickness=2)

        def draw_rot_triangle(x_t, y_t, angle):
            # x_t = 320, y_t = 100, Ecke links unten
            bio.draw_polygon ([point_rot(x_t, y_t, angle), point_rot(x_t+(40*g), y_t, angle), point_rot(x_t, y_t-(80*g), angle)], fill_color=None, border_thickness=2)

        print ("statisch -> 's' / Rechteck rotieren -> 'r' / Alles rotieren -> 'a'")
        was = input()
    
        bio.start()
        if (was != "s"):
            for i in range(720):
                draw_rot_rectangle(x_c-(40*g), y_c+(40*g), i)
                if (was == "a"):
                    draw_rot_triangle(x_c, y_c-(40*g), i)
                    draw_rot_triangle(x_c, y_c-(40*g), i+90)
                    draw_rot_triangle(x_c, y_c-(40*g), i+180)
                    draw_rot_triangle(x_c, y_c-(40*g), i+270)
                time.sleep (0.016)
                bio.clear_image ()
            bio.close_and_exit ()
            
        else:
            draw_rot_rectangle(x_c-(40*g), y_c+(40*g), 0)
            draw_rot_triangle(x_c, y_c-(40*g), 0)
            draw_rot_triangle(x_c, y_c-(40*g), 90)
            draw_rot_triangle(x_c, y_c-(40*g), 180)
            draw_rot_triangle(x_c, y_c-(40*g), 270)
            bio.wait_close ()

    # Aufgabe 3 Hypnobot getrennt
    if (aufgabe == "3"):

        def draw_concentric_circle(x_c, y_c, t):
            j = int(t*(-10))
            bio.draw_circle (x_c, y_c, (j+20)%100, fill_color=None, border_color=RED, border_thickness=1)
            bio.draw_circle (x_c, y_c, (j+40)%100, fill_color=None, border_color=GREEN, border_thickness=1)
            bio.draw_circle (x_c, y_c, (j+60)%100, fill_color=None, border_color=YELLOW, border_thickness=1)
            bio.draw_circle (x_c, y_c, (j+80)%100, fill_color=None, border_color=VIOLET, border_thickness=1)
            bio.draw_circle (x_c, y_c, (j+100)%100, fill_color=None, border_color=BLUE, border_thickness=1)

        def draw_pendulum(x_B, y_B, angle):
            h = 225  # Länge des Pendels
            i = h*numpy.sin(angle)
            f = h*numpy.cos(angle)
            bio.draw_line (x_B, y_B, x_B - int(i), y_B + int(f), BLACK, thickness=1)
            bio.draw_circle (x_B - int(i), y_B + int(f), 20, BLACK)
                
        def calcangle (t):
            angle = math.pi*numpy.sin(t)/2
            return (angle)

        bio.start()
        t = 0
        while (True):
            draw_pendulum(320, 20, calcangle(t))
            draw_concentric_circle(500, 200, t)
            t += 0.05
            time.sleep (0.016)
            bio.clear_image ()
        bio.wait_close ()

    # Aufgabe 4 Hypnobot zusammen
    if (aufgabe == "4"):

        def draw_all (x_B, y_B, t):
            h = 225 # Länge des Pendels
            i = h*numpy.sin(math.pi*numpy.sin(t)/2)
            f = h*numpy.cos(math.pi*numpy.sin(t)/2)
            bio.draw_line (x_B, y_B, x_B - int(i), y_B + int(f), BLACK, thickness=1)
            bio.draw_circle (x_B - int(i), y_B + int(f), 15, BLACK)

            j = int(t*(-10))
            bio.draw_circle (x_B - int(i), y_B + int(f), (j+20)%100, fill_color=None, border_color=RED, border_thickness=1)
            bio.draw_circle (x_B - int(i), y_B + int(f), (j+40)%100, fill_color=None, border_color=GREEN, border_thickness=1)
            bio.draw_circle (x_B - int(i), y_B + int(f), (j+60)%100, fill_color=None, border_color=YELLOW, border_thickness=1)
            bio.draw_circle (x_B - int(i), y_B + int(f), (j+80)%100, fill_color=None, border_color=VIOLET, border_thickness=1)
            bio.draw_circle (x_B - int(i), y_B + int(f), (j+100)%100, fill_color=None, border_color=BLUE, border_thickness=1)
        
        bio.start()
        t = 0
        while (True):
            draw_all (320, 20, t)
            t += 0.05
            time.sleep (0.016)
            bio.clear_image ()
        bio.wait_close ()