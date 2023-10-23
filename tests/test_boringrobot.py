from code.robots import BoringRobot

def test_speak_1():
    assert BoringRobot().speak() == "bleeep-blob"