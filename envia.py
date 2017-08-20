import os
import sys
noti = sys.argv[1]



f = open('/home/estokeate/notificaciones.txt', 'a')
f.write('p256dh.....'+str(noti)+'\n')

os.system('node /home/estokeate/push.js '+str(sys.argv[1])+' '+sys.argv[2]+' '+sys.argv[3]+' '+str(sys.argv[4])+' '+str(sys.argv[5]))