import unittest
from secure_password import is_secure_password

class TestSecurePassword(unittest.TestCase):
    def test_secure_passwords(self):
        self.assertTrue(is_secure_password("SenhaForte1~"))
        self.assertTrue(is_secure_password("Senha@Minha134"))
        self.assertTrue(is_secure_password("Minha$enha1&"))

    def test_insecure_passwords(self):
        self.assertFalse(is_secure_password("pequena"))
        self.assertFalse(is_secure_password("maiorMasSemNumero"))
        self.assertFalse(is_secure_password("tudominusculo1!"))
        self.assertFalse(is_secure_password("TUDOMAISCULO!"))
        self.assertFalse(is_secure_password("SemCaracteresEspeciais1"))
        self.assertFalse(is_secure_password(""))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            is_secure_password(12345678)
        with self.assertRaises(ValueError):
            is_secure_password(None)

if __name__ == "__main__":
    unittest.main()
