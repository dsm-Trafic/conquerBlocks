import math
import web3
from web3.middleware import geth_poa_middleware

def connectToWeb3():
    """
    Esta función se conecta a la cadena Binance Smart Chain (BSC) utilizando la biblioteca web3 y injecta el middleware de prueba de autoridad de Geth en la pila de middlewares del objeto Web3.
    No recibe ningún parámetro.
    Devuelve un objeto Web3 inicializado con la conexión a la cadena Binance Smart Chain y el middleware Geth ya inyectado.
    """
    # Inicializa el objeto Web3 utilizando el proveedor de Binance Smart Chain (BSC)
    w3 = web3.Web3(web3.Web3.HTTPProvider("https://bsc-dataseed1.binance.org:443"))
    # Inyecta el middleware de prueba de autoridad de Geth en la pila de middlewares del objeto Web3
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    # Devuelve el objeto Web3 inicializado
    return w3


def get_abi():
    """
    Esta función importa el archivo json con la interfaz de contrato (ABI) de PancakeSwap y lo devuelve como un diccionario.
    No recibe ningún parámetro.
    Devuelve un diccionario con la ABI de PancakeSwap.
    """
    import json

    filename = open("data/abi/pancakeswap.json")
    # Carga los datos del archivo json en un diccionario
    data = json.load(filename)
    # Devuelve el diccionario con la ABI
    return data

    


def getContract(w3, address):
    """
    Esta función toma un objeto Web3 y una dirección de contrato y devuelve un objeto contrato utilizando la ABI de PancakeSwap.
    Recibe el objeto Web3 y la dirección del contrato como parámetros.
    Devuelve un objeto contrato de PancakeSwap.
    """
    # Formatea la dirección del contrato a una dirección de chequeo
    addressFormated = web3.Web3.toChecksumAddress(address)
    # Crea un objeto contrato utilizando la dirección formateada y la ABI de PancakeSwap
    contractPancake = w3.eth.contract(address = addressFormated, abi = abiCoded)

    return contractPancake


def getPrivateKey(account_id):
    """
    Esta función obtiene la clave privada de una cuenta específica utilizando una función de desencriptación y otra función para obtener la clave privada codificada de la cuenta.
    Recibe el ID de la cuenta como parámetro.
    Devuelve la clave privada de la cuenta.
    """
    from ..libs.crypt import TTK_decrypt, get_private_key
    from ..libs.function import getAccountWeb3

    # Obtiene la función para decodificar la clave privada
    private_key_decoder = get_private_key()
    # Obtiene la clave privada codificada de la cuenta específica
    account_private_key = getAccountWeb3(account_id)

    # Utiliza la función de desencriptación para obtener la clave privada
    private_key = TTK_decrypt(private_key_decoder, account_private_key)

    return private_key


def getAccount(w3, account_id):
    """
    Esta función obtiene un objeto cuenta a partir de una clave privada y un objeto Web3.
    Recibe el ID de la cuenta como parámetro.
    Devuelve un objeto cuenta de Ethereum.
    """
    #Obtiene la clave privada y la cadena de conexión a la web3
    privateKey = getPrivateKey(account_id)
    w3 = connectToWeb3()
    # Crea un objeto cuenta a partir de la clave privada y el objeto Web3
    account = w3.eth.account.privateKeyToAccount(privateKey)

    return account



def getGasPrice(w3):
    """
    Esta función obtiene el precio actual del gas y lo multiplica por 1.40.
    Recibe el objeto web3 como parámetro.
    Devuelve el precio del gas multiplicado.
    """
    # Obtiene el precio actual del gas en la cadena de Ethereum y lo multiplica por 1.40
    gasPrice = w3.eth.gasPrice * 1.40

    return gasPrice


def getNonce(w3, account_id):
    """
    Esta función obtiene el nonce de una cuenta específica utilizando un objeto Web3 y la dirección de la cuenta.
    Recibe el objeto Web3 y el ID de la cuenta como parámetros.
    Devuelve el nonce de la cuenta.
    """
    account = getAccount(w3, account_id)
    # Obtiene el nonce de la cuenta utilizando la dirección de la cuenta y el objeto Web3
    nonce = w3.eth.getTransactionCount(account.address)

    return nonce


def transaction(account_id, nonce, gasPrice, amountIn, amountOutMin, pairs, fromAddress, contractAddress):
    """
    Esta función realiza una transacción de intercambio de tokens específicos en PancakeSwap utilizando una cuenta específica, un nonce, un precio de gas, una cantidad de entrada, una cantidad de salida mínima, un par de tokens, una dirección de origen y una dirección de contrato.
    Devuelve el resultado de la transacción hasheada.
    """
    # Se conecta a la Blockchain
    w3 = connectToWeb3()

    # Obtiene los datos necesarios para la ejecucción de la transacción, cómo el contrato, la cuenta, el precio del gas, el nonce y la private_key
    contractPancake = getContract(w3, contractAddress)
    account = getAccount(w3, account_id)
    gasPrice = getGasPrice(w3)
    nonce = getNonce(w3, account_id)
    privateKey = getPrivateKey()

    import time
    # Obtiene el timestamp y le añade 10 minutos para deadline de ejecucción
    current_ts = int(time.time()) + (10*60)
    # Crea un diccionario con los parámetros de la transacción
    params = {
        'from': account.address,
        'gas':8000000,
        'gasPrice':int(gasPrice),
        'nonce':nonce,
        'chainId':56
    }

    # Crea la transacción utilizando la función swapExactTokensForETH del contrato de PancakeSwap y los parámetros especificados
    tx_has = contractPancake.functions.swapExactTokensForETH(amountIn, amountOutMin, pairs, fromAddress, current_ts).buildTransaction(params)

    # Firma la transacción con la clave privada de la cuenta
    signed_tx = w3.account.signTransaction(tx_has, privateKey)
    # Envía la transacción a la cadena de bloques
    send_transaction = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return send_transaction
    
