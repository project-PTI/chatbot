<script>
        function openChat() {
            // Hide the tab container and show the chat container
            document.getElementById('tabContainer').style.display = 'none';
            document.getElementById('chatContainer').style.display = 'flex';
    
        }

        function endChat() {
            // Hide the chat container and show the tab container
            document.getElementById('chatContainer').style.display = 'none';
            document.getElementById('tabContainer').style.display = 'flex';
        }

        function resetChat() {
            document.getElementById('chatOutput').innerHTML = "";
            document.getElementById('userInput').value = "";
            
            const welcomeMessage = document.createElement('div');
            welcomeMessage.classList.add('message', 'bot-message');
            welcomeMessage.innerHTML = `
                <div class='profile'>
                    <img src='https://files.oaiusercontent.com/file-V66QJl1i7pC7S2uv2mi1jzdy?se=2024-11-14T06%3A08%3A03Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dd8b0d4f8-87cb-4b32-b572-2fa70e5bb577.webp&sig=FfJCOR8jLLB%2BlmCwgIf6IHnxpCe6vKkXnMzcNZFSdE0%3D' alt='Bot Profile' class='profile-pic'>
                    <span>BOT</span>
                </div>
                <span>Welcome to Pet's Name Chatbot! I'm here to help with anything you need...</span>
            `;
            document.getElementById('chatOutput').appendChild(welcomeMessage);
        }

        document.getElementById("startChatButton").addEventListener("click", function() {
            document.getElementById("welcomeMessage").style.display = "none"; // Hide welcome message
            document.getElementById("chatbotBox").classList.remove("hidden"); // Show chatbot box

        });

        
    </script>
