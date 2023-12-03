from wpilib import DataLogManager, Timer, DriverStation, TimedRobot
from wpilib.deployinfo import getDeployData
from wpiutil.log import StringLogEntry


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
        self.log_data = self.dlm.getLog()
        self.custom_entry = StringLogEntry(self.log_data, f'messages/{self.name}')
        
    def _robot_log_setup(self):
        self.get_deploy_info()
        self.log_driverstation(True)
        self.complete('Robot logging initialized')
        
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
        DriverStation.startDataLog(self.log_data, joysticks)
        self.info('DriverStation logging started')
        if joysticks:
            self.info('Joystick logging started')
        
    def pms(self, colors: bool = True):
        
        sim_color = ''
        header_color = ''
        time_color = ''
        end_color = ''
        
        if colors:
            sim_color = BColors.TEST
            header_color = BColors.HEADER
            time_color = BColors.TIME
            end_color = BColors.ENDC
        
        mode = 'DISABLED'
        is_sim = f'{sim_color}SIMULATION{end_color}' if TimedRobot.isSimulation() else ''
        if DriverStation.isEnabled():
            mode = 'TELEOP' if DriverStation.isTeleopEnabled() else 'AUTONOMOUS'
            
        mode = f'{header_color}{mode}{end_color}'
        
        combined = mode + "  " + is_sim 
            
        time = Timer.getFPGATimestamp()
        time = f'{time:.3f}'
        if TimedRobot.isSimulation() == False:
            time = Timer.getMatchTime()
            time = f'{time:.3f}'
        
        return f'  {time}{time_color}  {combined}{end_color}'
        
    def _format(self, type):
        return f'  |  {type}  |  '
        
    def _format_std_out(self, color: BColors, type, message):
        return f'{self.pms()}{color}{type}{self.name}: {message}{BColors.ENDC}'
    
    def __log(self, message, type, color):
        print(self._format_std_out(color, type, message))
        self.custom_entry.append(f'{self.pms(False)}{type}{self.name}: {message}')
        
    def message(self, message):
        
        self.custom_entry.append(f'{self.pms()}{self.name}: {message}')
        
        
    def info(self, message):
        info = self._format('INFO')
        self.__log(message, info, BColors.OKBLUE)
        
    def debug(self, message):
        debug = self._format('DEBUG')
        self.__log(message, debug, BColors.OKCYAN)
        
    def complete(self, message):
        done = self._format('DONE')
        self.__log(message, done, BColors.OKGREEN)
        
    def warn(self, message):
        warn = self._format('WARN')
        self.__log(message, warn, BColors.WARNING)
    
    def error(self, message):
        error = self._format('ERROR')
        self.__log(message, error, BColors.FAIL)