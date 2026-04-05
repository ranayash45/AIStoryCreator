document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("loadBtn");
    const loadingDiv = document.getElementById("loading");
    const contentArea = document.getElementById("contentArea");

    btn.addEventListener("click", async () => {
        const style = document.getElementById("style").value;
        const extraInfo = document.getElementById("extraInfo").value;

        // Show loading indicator
        loadingDiv.style.display = "block";
        contentArea.innerHTML = "";

        try {
            // Add timeout (e.g., 8 seconds)
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 160000);

            const response = await fetch(`/load_html?style=${style}&extra=${encodeURIComponent(extraInfo)}`, {
                signal: controller.signal
            });
            clearTimeout(timeoutId);

            const data = await response.json();
            contentArea.innerHTML = data.html;
        } catch (error) {
            if (error.name === "AbortError") {
                contentArea.innerHTML = "<p>Request timed out. Please try again.</p>";
            } else {
                contentArea.innerHTML = "<p>Error loading content.</p>";
            }
        } finally {
            // Hide loading indicator
            loadingDiv.style.display = "none";
        }
    });
});