async function shortenURL() {
    const input = document.getElementById("urlInput");
    const resultDiv = document.getElementById("result");
    const url = input.value;

    if (!url) {
        resultDiv.innerText = "❌ Please enter a URL";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/shorten", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        if (response.ok) {
            const shortUrl = `http://127.0.0.1:8000/${data.short_code}`;
            resultDiv.innerHTML = `
                ✅ Short URL:<br>
                <a href="${shortUrl}" target="_blank">${shortUrl}</a>
            `;
        } else {
            resultDiv.innerText = data.detail || "Error occurred";
        }
    } catch (error) {
        resultDiv.innerText = "❌ Backend server not running";
    }
}
