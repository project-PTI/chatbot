<py-script>
        from pyscript import Element # Mengimpor Element dari PyScript untuk manipulasi DOM

        def respond(event): # Fungsi untuk menangani respons chatbot
            user_input = Element('userInput').element.value.lower() # Mengambil input pengguna dan mengubahnya menjadi huruf kecil
            if "hello" in user_input: # Menanggapi jika input mengandung "halo"
                response = "Hello, how can I assist you?"
            elif "hai" in user_input: # Menanggapi jika input mengandung "hai"
                response = "Hi, how can I help you?"
            elif "how are you?" in user_input: # Menanggapi jika input mengandung "apa kabar"
                response = "I'm doing well, thank you!"
            elif "recommendation" in user_input: # Menanggapi jika input mengandung "rekomendasi"
                response = "What kind of pet do you have?"
            elif "cat" in user_input:
                response = """
                Here are some name recommendations for your cat:
                <div style='display: flex; justify-content: space-between;'>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Milo</li>
                            <li>Neko</li>
                            <li>Kiki</li>
                            <li>Loki</li>
                            <li>Tara</li>
                        </ul>
                    </div>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Whiskers</li>
                            <li>Oliver</li>
                            <li>Leo</li>
                            <li>Ginger</li>
                            <li>Shadow</li>
                        </ul>
                    </div>
                </div>""" #Membuat respons dengan 2 kolom nama
            
            elif "dog" in user_input:
                response = """
                Here are some name recommendations for your dog:
                <div style='display: flex; justify-content: space-between;'>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Chiko</li>
                            <li>Belo</li>
                            <li>Snowy</li>
                            <li>Midnight</li>
                            <li>Simba</li>
                        </ul>
                    </div>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Buddy</li>
                            <li>Daisy</li>
                            <li>Rocky</li>
                            <li>Max</li>
                            <li>Charlie</li>
                        </ul>
                    </div>
                </div>"""
            
            elif "bird" in user_input: # Menanggapi jika input mengandung "burung"
                response = """
                Here are some name recommendations for your bird:
                <div style='display: flex; justify-content: space-between;'>
                    <div style ='width: 50%;'>
                        <ul>
                            <li>Sky</li>
                            <li>Sunny</li>
                            <li>Lola</li>
                            <li>Kiwi</li>
                            <li>Pepper</li>
                        </ul>
                    </div> 
                    <div style='width: 50%;'>
                        <ul>
                            <li>Pixel</li>
                            <li>Echo</li>
                            <li>Nox</li>
                            <li>Vega</li>
                            <li>Zara</li>
                        </ul>
                    </div> 
                </div>"""
            elif "fish" in user_input: # Menanggapi jika input mengandung "ikan"
                response = """
                Here are some name recommendations for your fish:
                <div style='display: flex; justify-content: space-between;'>
                    <div style='width: 50%;'>
                        <ul>
                            <li>Lucky</li>
                            <li>Nemo</li>
                            <li>Bubbles</li>
                            <li>Suki</li>
                            <li>Yoda</li>
                        </ul>
                     </div>
                    <div style='width: 50%;'>
                        <ul>
                            <li>coco</li>
                            <li>jett</li>
                            <li>Zylo</li>
                            <li>Riptide</li>
                            <li>Aqua</li>
                        </ul>
                    </div>
                </div>"""
            elif "quote" in user_input:
                response="Work for a cause, not for applause. Live life to express, not to impress. - J.R.R. Tolkien"
            elif "more" in user_input: # Menanggapi jika input mengandung "kata"
                response = "Do not depend on others, let alone hanging on a tree while eating bananas."
            elif "next" in user_input: # Menanggapi jika input mengandung "lagi dong"
                response = "Failure is not something to fear, but something to learn from."
            else: # Menanggapi jika input tidak dikenali
                response = "Sorry, I don't understand."

        
                # Update chat output with user and bot messages alongside profiles
            Element('chatOutput').element.innerHTML += f"""
                <div class='message user-message'>
                    <div class='profile'>
                        <img src='http://bit.ly/3ASBRH0' alt='User Profile' class='profile-pic'>
                        <span>USER</span>
                    </div>
                    <span>{user_input}</span> <!-- Display user message text -->
                </div>
            """
            Element('chatOutput').element.innerHTML += f"""
                <div class='message bot-message'>
                    <div class='profile'>
                        <img src='https://files.oaiusercontent.com/file-V66QJl1i7pC7S2uv2mi1jzdy?se=2024-11-14T06%3A08%3A03Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dd8b0d4f8-87cb-4b32-b572-2fa70e5bb577.webp&sig=FfJCOR8jLLB%2BlmCwgIf6IHnxpCe6vKkXnMzcNZFSdE0%3D' alt='Bot Profile' class='profile-pic'>
                        <span>BOT   </span>
                    </div>
                    <span>{response}</span> <!-- Display bot message text -->
                </div>
            """
            Element('userInput').element.value = ""
          

        Element('sendBtn').element.onclick = respond
           
    </py-script>
