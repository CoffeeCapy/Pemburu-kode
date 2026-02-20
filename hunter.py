import secrets
import base58
from solana.keypair import Keypair
from solana.rpc.api import Client

# Menggunakan koneksi resmi Solana
client = Client("https://api.mainnet-beta.solana.com")

def hunt():
    print("--- Memulai Pencarian CoffeeCapy ---")
    # Cek 100 dompet setiap kali mesin ini menyala
    for i in range(100):
        seed = secrets.token_bytes(32)
        keypair = Keypair.from_seed(seed)
        address = str(keypair.public_key)
        priv = base58.b58encode(seed).decode('ascii')
        
        try:
            # Cek saldo langsung ke blockchain
            res = client.get_balance(keypair.public_key)
            bal = res['result']['value'] / 1000000000
            
            print(f"[{i+1}] {address} | Saldo: {bal} SOL")
            
            # Jika ditemukan dompet yang ada isinya:
            if bal > 0:
                print(f"!!! JACKPOT DITEMUKAN !!!")
                with open("jackpot.txt", "a") as f:
                    f.write(f"Address: {address} | PrivateKey: {priv} | Balance: {bal}\n")
        except:
            continue

if __name__ == "__main__":
    hunt()
