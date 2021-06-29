import time
from pathlib import Path
from SMWinservice import SMWinservice
from lucrum_sync import main

class PythonCornerExample(SMWinservice):
    _svc_name_ = "LucrumBiometricPushService"
    _svc_display_name_ = "Lucrum Biometric Push Service"
    _svc_description_ = "Service to push biometric data from device to Lucrum"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            main()
            time.sleep(15)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()