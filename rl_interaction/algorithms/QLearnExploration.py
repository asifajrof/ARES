from algorithms.ExplorationAlgorithm import ExplorationAlgorithm
from utils.utils import Timer
from utils.q import Q


class QLearnAlgorithm(ExplorationAlgorithm):

    @staticmethod
    def explore(app, emulator, appium, timesteps, timer, eps=0.8, **kwargs):
        try:
            t = Timer(timer)
            q_l = Q(app, t, eps=eps)
            q_l.learn(timesteps)
            return True
        except Exception as e:
            appium.restart_appium()
            if emulator is not None:
                emulator.restart_emulator()
            return False
