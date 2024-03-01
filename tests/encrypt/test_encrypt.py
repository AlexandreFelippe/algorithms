import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "key")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 4)

    assert encrypt_message("message", 0) == "egassem"
    assert encrypt_message("message", 10) == "egassem"

    assert encrypt_message("message", 3) == "sem_egas"

    assert encrypt_message("message", 4) == "ega_ssem"

    assert encrypt_message("example", 3) == "axe_elpm"

    assert encrypt_message("python", 2) == "noht_yp"
