import unittest
from produto import Produto
from produto import create

class teste(unittest.TestCase):
    def testeproduto(self):
        prod = Produto(1,"a",1,1,"a")
        self.assertIsNotNone(prod)
        self.assertEqual(prod.id, 1)
        self.assertEqual(prod.nome, "a")
        self.assertEqual(prod.quantidade, 1)
        self.assertEqual(prod.preco, 1)
        self.assertEqual(prod.fornecedor, "a")
    def testecreateiderro(self):
        prod = create(-1,"a",1,1,"a")
        self.assertEqual(prod.id,-255)
        self.assertEqual(prod.nome, "Erro de ID")
        self.assertEqual(prod.fornecedor, "Erro")
    def testecreateprecoerro(self):
        prod = create(1,"a",1,-1,"a")
        self.assertEqual(prod.preco,-800)
        self.assertEqual(prod.nome, "Erro de Preço")
        self.assertEqual(prod.fornecedor, "Erro")
    def testecreateduploerro(self):
        prod = create(10,"a",1,0,"a")
        self.assertEqual(prod.id,-999)
        self.assertEqual(prod.nome, "Erro Múltiplo")
        self.assertEqual(prod.fornecedor, "Erro")
    def testecreatequantidadezero(self):
        prod = create(1,"a",-5,1,"a")
        self.assertEqual(prod.quantidade, 0)

if __name__ == '__main__':
    unittest.main()