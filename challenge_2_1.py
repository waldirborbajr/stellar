from inspect import signature

import base64
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, ManageData

SERVER_URL_MAIN = "https://horizon.stellar.org"

server = Server(SERVER_URL_MAIN)

secret_key = "SUA_CHAVE_SECRETA"
keypair = Keypair.from_secret(secret_key)
public_key = keypair.public_key

text = "DEV30K"
text_byte = text.encode()
signature = keypair.sign(base64.b64encode(text_byte))
print(f"Assinatura de '{text}' em base64: {signature}")
try:
    account = server.load_account(public_key)

    manage_data_op = ManageData(data_name="desafio", data_value=signature)

    transaction = (
        TransactionBuilder(
            source_account=account,
            network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
            base_fee=100,
        )
        .add_text_memo(text)
        .append_operation(manage_data_op)
        .set_timeout(30)
        .build()
    )

    # Assina a transação com a chave secreta
    transaction.sign(keypair)

    # Envia a transação para a rede Mainnet da Stellar
    result = server.submit_transaction(transaction)

    print("Transação enviada com sucesso! Hash da transação:", result["hash"])
except Exception as error:
    print("Erro ao enviar a transação:", error)
