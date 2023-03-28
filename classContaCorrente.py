class ContaCorrente:

    def __init__(self):
        self._saldo = None

    def depositar(self, valor):
        self._saldo += valor

    def consultar_saldo(self):
        return self._saldo


# conta = ContaCorrente()  # cria um objeto da classe ContaCorrente
# conta.depositar(100)  # deposita R$ 100 na conta
# saldo = conta.consultar_saldo()
# print("Saldo da conta corrente:", saldo)  # imprime o saldo na tela
