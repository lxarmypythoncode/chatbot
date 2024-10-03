import cohere

# Menginisialisasi API Cohere dengan API token Anda
cohere_client = cohere.Client('API_KEY_DARI_AI')

# Fungsi untuk mengirim prompt ke Cohere dan mendapatkan respons
def chat_with_cohere(prompt):
    try:
        response = cohere_client.generate(
            model='command-xlarge-nightly',  # Model yang digunakan
            prompt=prompt,
            max_tokens=150,  # Batasan panjang respons
            temperature=0.7,  # Kreativitas atau variasi jawaban
            k=0,  # Tidak ada top-k sampling
            p=0.75,  # Top-p sampling untuk mengontrol keseragaman jawaban
            stop_sequences=["--"]
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Fungsi utama untuk memulai percakapan
def main():
    print("Selamat datang di Chatbot Cohere sederhana! Ketik 'keluar' untuk berhenti.")
    
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == "keluar":
            print("Terima kasih sudah menggunakan Chatbot Cohere!")
            break
        
        response = chat_with_cohere(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
