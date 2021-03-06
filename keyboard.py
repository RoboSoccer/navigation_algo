
import socket
import sys
import pygame as pg
import time


def client_program():
    print('Started server')
    pg.init()
    #host = socket.gethostname()  # as both code is running on same pc
    host = '192.168.43.31'
    port = 5031  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print('connected to the server')

    done = False
    pg.joystick.init()
    if(pg.joystick.get_count()!=0):
        joystick = pg.joystick.Joystick(0)
        print(joystick)
        joystick.init()
        while not done:
            time.sleep(.4)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
            axis1 = joystick.get_axis( 1 ) #for forward movement
            axis0 = joystick.get_axis( 0 ) #for left and right movement
            axis2 = joystick.get_axis( 2 )
            A = joystick.get_button( 0 )
            B = joystick.get_button( 1 )
            Y = joystick.get_button( 3 )
            X = joystick.get_button( 2 )
            keys = pg.key.get_pressed()
            if A == 1:
                pressed.append(1)
            if B == 1:
                pressed.append(2)
            if Y == 1:
                pressed.append(3)
            if X == 1:
                pressed.append(0)
            if pressed[-1] == 0:
                speed = ",190"
            if pressed[-1] == 1:
                speed = ",100"
            if pressed[-1] == 2:
                speed = ",120"
            if pressed[-1] == 3:
                speed = ",150"
            message = "0,0"+speed+speed
            if keys[pg.K_a] or axis0 <= -0.85:  #to move left
                message = "3,3"+speed+speed
            if keys[pg.K_d]or axis0 >= 0.85: #to move right
                message = "4,4"+speed+speed
            if keys[pg.K_w]or axis1 <= -0.85:  #to move up
                message = "1,1"+speed+speed

            if keys[pg.K_s]or axis1 >= 0.85: #to move down
                message = "2,2"+speed+speed
            if axis2 <= -0.85: 
                message = "2,1"+speed+speed
            if axis2 >= 0.85:
                message = "1,2"+speed+speed
            print(message)

        #message = input(" -> ")  # take input
        #key = input()
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            print('Received from server: ' + data)  # show in terminal

            # message = input(" -> ")  # again take input
            #key = input()

        client_socket.close()  # close the connection
    else:
        while not done:
            time.sleep(.4)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
            keys = pg.key.get_pressed()
            message = "0,0,0,0"
            if keys[pg.K_a]:  #to move left
                message = "3,3,255,255"
            elif keys[pg.K_d]: #to move right
                message = "4,4,255,255"
            elif keys[pg.K_w]:  #to move up
                message = "1,1,255,255"

            elif keys[pg.K_s]: #to move down
                message = "2,2,255,255"
            elif keys[pg.K_q]: 
                message = "2,1,255,255"
            elif keys[pg.K_e]:
                message = "1,2,255,255"
            print(message)

        #message = input(" -> ")  # take input
        #key = input()
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            print('Received from server: ' + data)  # show in terminal

            # message = input(" -> ")  # again take input
            #key = input()

        client_socket.close()  # close the connection



if __name__ == '__main__':
    global pressed
    pressed=[0]
    client_program()
    pg.quit()
    sys.exit()