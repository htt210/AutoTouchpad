import time 
import subprocess
import threading

def main():
    subprocess.call('gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true', shell=True)
    # replace 17 with the id of your keyboard as shown in output of `xinput list`
    p = subprocess.Popen('xinput test 17', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    clickTime = [0]
    def checkTime():
        keys = [37, 50, 62, 64, 105, 108, 133]
        while True:
            out = p.stdout.readline()
            
            if len(out) < 1:
                break
            key = int(out.split()[-1])
            if key not in keys:
                clickTime[0] = time.time()
    
    t = threading.Thread(target=checkTime)
    t.start()
    
    touchpad = True
    while True:
        inactive = time.time() - clickTime[0]
        # print ('inactive for', inactive)
        if inactive > 1:            # replace 1 with `x` to disable the touchpad for `x` seconds
            if not touchpad:
                print ('Enable touchpad')
                subprocess.call('gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true', shell=True)
            touchpad = True
        else:
            if touchpad:
                print ('Disable touchpad')
                subprocess.call('gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click false', shell=True)
            touchpad = False
        time.sleep(0.5)

    retval = p.wait()

if __name__ == '__main__':
    main()
