import secrets
import base58
from solders.keypair import Keypair # Ini perubahan utamanya
from solana.rpc.api import Client

client = Client("https://api.mainnet-beta.solana.com")

def hunt():
    print("--- Hunting Started ---")
    for i in range(100):
        # Membuat keypair baru
        kp = Keypair() 
        address = str(kp.pubkey())
        # Private key dalam format Base58
        priv = base58.b58encode(bytes(kp)).decode('utf-8')
        
        try:
            res = client.get_balance(kp.pubkey())
            bal = res.value / 1000000000 # Format terbaru pake .value
            print(f"[{i+1}] {address} | Bal: {bal} SOL")
            
            if bal > 0:
                with open("jackpot.txt", "a") as f:
                    f.write(f"Addr: {address} | Priv: {priv} | Bal: {bal}\n")
        except:
            continue

if __name__ == "__main__":
    hunt()
