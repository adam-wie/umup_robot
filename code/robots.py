from typing import Protocol

class Robot(Protocol):
    def speak(self) -> str :
        pass


class BoringRobot() :
    def speak(self) :
        return "bleeep-blob"