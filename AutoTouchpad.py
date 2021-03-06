import time 
import subprocess
import threading

def main():
    listResult = subprocess.Popen('xinput list', shell=True, stdout=subprocess.PIPE)
    for line in listResult.stdout:
        if line.find('AT Translated Set 2 keyboard') >= 0:
            start = line.find('id=') + 3
            keyboardId = int(line[start:start+2])
    subprocess.call('gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true', shell=True)
    p = subprocess.Popen('xinput test ' + str(keyboardId), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    clickTime = [0, 0]
    def checkTime():
        keys = [37, 50, 62, 64, 108, 105, 133]
        while True:
            out = p.stdout.readline()
            if len(out) < 1:
                break
            key = int(out.split()[-1])
            if key not in keys:
                clickTime[0] = time.time()
    
    t = threading.Thread(target=checkTime)
    t.start()
    
    counter = 0
    touchpad = True
    while True:
        inactive = time.time() - clickTime[0]
        # print ('inactive for', inactive)
        if inactive > 2:            
            if not touchpad:
                print ('Enable touchpad', counter)
                counter += 1
                subprocess.call('gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true', shell=True)
                # subprocess.call('notify-send "tap-to-click enabled"', shell=True)
            touchpad = True
        else:
            if touchpad:
                print ('Disable touchpad', counter)
                counter += 1
                subprocess.call('gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click false', shell=True)
                # subprocess.call('notify-send "tap-to-click disabled"', shell=True)
            touchpad = False
        time.sleep(0.1)

    retval = p.wait()

if __name__ == '__main__':
    main()
