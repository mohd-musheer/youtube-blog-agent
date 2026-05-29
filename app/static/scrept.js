document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('blog-form');
    const urlInput = document.getElementById('youtube-url');
    const generateBtn = document.getElementById('generate-btn');
    const btnText = document.querySelector('.btn-text');
    const spinner = document.getElementById('loading-spinner');
    
    const resultContainer = document.getElementById('result-container');
    const blogTitle = document.getElementById('blog-title');
    const blogContent = document.getElementById('blog-content');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const url = urlInput.value.trim();
        if (!url) return;

        // Reset UI States
        errorMessage.classList.add('hidden');
        resultContainer.classList.add('hidden');
        
        // Set Loading State
        generateBtn.disabled = true;
        btnText.classList.add('hidden');
        spinner.classList.remove('hidden');

        try {
            // Call the FastAPI backend
            const response = await fetch('/generate-blog', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ youtube_url: url })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();

            // Populate Data
            blogTitle.textContent = data.title;
            
            // Parse Markdown content to HTML using Marked.js
            blogContent.innerHTML = marked.parse(data.content);

            // Show Result
            resultContainer.classList.remove('hidden');

        } catch (error) {
            errorMessage.textContent = "Failed to generate blog. Please check the URL and try again.";
            errorMessage.classList.remove('hidden');
            console.error("Error:", error);
        } finally {
            // Remove Loading State
            generateBtn.disabled = false;
            btnText.classList.remove('hidden');
            spinner.classList.add('hidden');
        }
    });
});