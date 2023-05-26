from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis()

def calcular_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        # Verificar se o resultado está em cache
        cache_key = f"fatorial:{numero}"
        resultado = cache.get(cache_key)
        if resultado: 
            return int(resultado)

        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i

        # Armazenar o resultado em cache
        cache.set(cache_key, str(fatorial))
        return fatorial

def calcular_super_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        # Verificar se o resultado está em cache
        cache_key = f"super_fatorial:{numero}"
        resultado = cache.get(cache_key)
        if resultado:
            return int(resultado)

        super_fatorial = 1
        for i in range(1, numero + 1):
            super_fatorial *= calcular_fatorial(i)

        # Armazenar o resultado em cache
        cache.set(cache_key, str(super_fatorial))
        return super_fatorial

@app.route('/super_fatorial/<int:numero>', methods=['GET'])
def obter_super_fatorial(numero):
    resultado = calcular_super_fatorial(numero)
    return jsonify({'numero': numero, 'super_fatorial': resultado})

if __name__ == '__main__':
    app.run(debug=True)