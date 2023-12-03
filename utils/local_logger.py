from wpilib import DataLogManager, Timer, DriverStation, TimedRobot
from wpilib.deployinfo import getDeployData



class BColors:
    TEST = '\u001b[41;1m'
    TIME = '\u001b[35;1m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class LocalLogger():
    
    def __init__(self, name):
        self.name = name
        self.dlm = DataLogManager
        self.dlm.start('logs/')
        self.log_custom = self.dlm.getLog()
        
    def _robot_log_setup(self):
        self.get_deploy_info()
        self.log_driverstation(True)
        
    def get_deploy_info(self):
        
        data = getDeployData()
        
        if data is None:
            if TimedRobot.isSimulation():
                self.warn('Running in simulation')
                return
            self.warn('Deploy info not found')
            return
        
        branch = data['git']['branch']
        
        date = data['deploy']['date']
        
        by = data['deply']['user']
        
        string = f'Deploy Info\n Branch: {branch}\n Deployment Date: {date}\n Deployed By: {by}'
        
        if branch != 'master' and branch != 'main':
            self.warn(string)
        else:
            self.complete(string)
        
    def log_driverstation(self, joysticks: bool):
        DriverStation.startDataLog(self.log_custom, joysticks)
        
    def pms(self):
        
        mode = 'DISABLED'
        is_sim = f'{BColors.TEST}SIMULATION{BColors.ENDC}' if TimedRobot.isSimulation() else ''
        if DriverStation.isEnabled():
            mode = 'TELEOP' if DriverStation.isTeleopEnabled() else 'AUTONOMOUS'
            
        mode = f'{BColors.HEADER}{mode}{BColors.ENDC}'
        
        combined = mode + "  " + is_sim 
            
        time = Timer.getFPGATimestamp()
        time = f'{time:.3f}'
        if TimedRobot.isSimulation() == False:
            time = Timer.getMatchTime()
            time = f'{time:.3f}'
        
        return f'  {BColors.TIME}{time}  {combined}{BColors.ENDC}'
        
    def message(self, message):
        self.dlm.log(f'{self.pms()}{self.name}: {message}')
        
    def _format(self, type):
        return f'  |  {type}  |  '
        
    def info(self, message):
        info = self._format('INFO')
        self.dlm.log(f'{self.pms()}{BColors.OKBLUE}{info}{self.name}: {message}{BColors.ENDC}')
        
    def debug(self, message):
        debug = self._format('DEBUG')
        self.dlm.log(f'{self.pms()}{BColors.OKCYAN}{debug}{self.name}: {message}{BColors.ENDC}')
        
    def complete(self, message):
        done = self._format('DONE')
        self.dlm.log(f'{self.pms()}{BColors.OKGREEN}{done}{self.name}: {message}{BColors.ENDC}')
        
    def warn(self, message):
        warn = self._format('WARN')
        self.dlm.log(f'{self.pms()}{BColors.WARNING}{warn}{self.name}: {message}{BColors.ENDC}')
    
    def error(self, message):
        error = self._format('ERROR')
        self.dlm.log(f'{self.pms()}{BColors.FAIL}{error}{self.name}: {message}{BColors.ENDC}')