import pytest

from caesars_cipher import CaesarsCipher


@pytest.fixture()
def caesars_cipher() -> CaesarsCipher:
    return CaesarsCipher()


def test_classic_usage(caesars_cipher: CaesarsCipher) -> None:
    caesars_cipher.key = 3

    expected_source_message = 'The vacation was a success'
    expected_encrypted_message = 'Wkh.ydfdwlrq.zdv.d.vxffhvv'

    encrypted_message = caesars_cipher.encrypt(expected_source_message)
    decrypted_message = caesars_cipher.decrypt(encrypted_message)

    assert encrypted_message == expected_encrypted_message
    assert decrypted_message == expected_source_message


def test_null_key(caesars_cipher: CaesarsCipher) -> None:
    caesars_cipher.key = 0
    expected_source_message = 'Hello world!'

    encrypted_message = caesars_cipher.encrypt(expected_source_message)
    decrypted_message = caesars_cipher.decrypt(encrypted_message)

    assert encrypted_message == expected_source_message
    assert decrypted_message == expected_source_message


if __name__ == '__main__':
    pytest.main()
