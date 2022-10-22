import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = 'buen día'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DÍA') #COMPRUEBA QUE EL RESULTADO SEA EL ESPERADO, PARA ESTE CASO EN MAYUSCULAS


if __name__ == '__main__':
    unittest.main()
