async function shortenURL() {
    // 🔒 Hard-coded URL (input box ignore)
    const url = "https://www.youtube.com";
    const resultDiv = document.getElementById("result");

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
            resultDiv.innerText = data.detail;
        }
    } catch (error) {
        resultDiv.innerText = "❌ Server not reachable";
    }
}
