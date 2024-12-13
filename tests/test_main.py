from main import greet
def test_greet(caps ys):
   greet("Alice")
   captured=caps ys.readouterr()
   assert captured.out="Bonjour, Alice !\n"
