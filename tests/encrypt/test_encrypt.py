from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('12345', 3) == '321_54'
    assert encrypt_message('12345', 4) == '5_4321'
    assert encrypt_message('54321', 2) == '123_45'
    assert encrypt_message('12345', 9) == '54321'
    with pytest.raises(TypeError):
        encrypt_message('12345', '12345')
    with pytest.raises(TypeError):
        encrypt_message(12345, 12345)
