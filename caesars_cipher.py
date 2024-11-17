from __future__ import annotations

import re

import enchant

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
dictionary = enchant.Dict('en_US')


def find_key(message: str) -> int:
    for key in range(len(ALPHABET)):
        shift = -key
        source_message = CaesarsCipher.replace_symbols(message, shift)

        source_message = re.sub(r'[!?.]', '', source_message)
        source_words = source_message.split(' ')
        if 'password' in source_words:
            return key

        is_correct = all(dictionary.check(word)
                         for word in source_words if word)
        if is_correct:
            return key

    raise RuntimeError('Cannot find a encryption key')


class CaesarsCipher:
    __key: int | None = None

    @property
    def key(self) -> int | None:
        return self.__key

    @key.setter
    def key(self, key: int) -> None:
        self.__key = key

    def decrypt(self, encrypted_message: str) -> str:
        if self.key is None:
            self.key = find_key(encrypted_message)

        shift = -self.key
        source_message = self.replace_symbols(encrypted_message, shift)
        return source_message

    def encrypt(self, source_message: str) -> str:
        if self.key is None:
            raise ValueError('Encryption key is not set')

        shift = self.key
        encrypted_message = self.replace_symbols(source_message, shift)
        return encrypted_message

    @staticmethod
    def replace_symbols(message: str, shift: int) -> str:
        output_message = ''
        for symbol in message:
            old_pos_symbol = ALPHABET.index(symbol)
            new_pos_symbol = (old_pos_symbol + shift) % len(ALPHABET)
            output_message += ALPHABET[new_pos_symbol]

        return output_message


def main() -> None:
    caesars_cipher = CaesarsCipher()
    msg = caesars_cipher.decrypt('o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D')
    print(f'{caesars_cipher.key}: {msg}')


if __name__ == '__main__':
    main()
