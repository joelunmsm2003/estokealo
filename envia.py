import os
import sys
noti = sys.argv[1]

print sys.argv[2]

f = open('/home/estokeate/notificaciones.txt', 'a')
f.write('p256dh.....'+str(sys.argv[4])+'\n')

os.system('node /home/estokeate/push.js '+str(sys.argv[1])+' '+sys.argv[2]+' '+sys.argv[3]+' "'+str(sys.argv[4])+'" "'+str(sys.argv[5])+'" "'+str(sys.argv[6])+'" "'+str(sys.argv[7])+'"')