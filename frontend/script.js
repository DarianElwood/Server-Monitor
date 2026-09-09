const init = async () => {
    const content = document.querySelector(".main-content");

    try {
        const response = await fetch(
            "https://api.darianelwood.com/v1/api/serverQuery"
        );

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const servers = await response.json();

        for (const server of servers) {
            const row = document.createElement("div");
            row.className = "content-row";

            const values = [
                server.server_name ?? "Unavailable",
                server.status ?? "Unavailable",
                server.game ?? "Unavailable",
                server.map ?? "Unavailable",
                server.server_address ?? "Unavailable",
                server.server_port ?? "Unavailable",
                `${server.players ?? 0}/${server.max_players ?? 0}`
            ];

            const statusCell = document.createElement("div");
            statusCell.className = "content-cell";

            const statusImage = document.createElement("img");
            statusImage.className = "status-circle";
            statusImage.alt = "Server status";
            statusImage.src = server.status === "Server is up."
                ? "imgs/green-circle.svg"
                : "imgs/red-circle.svg";

            statusCell.appendChild(statusImage);
            row.appendChild(statusCell);

            for (const value of values) {
                const cell = document.createElement("div");
                cell.className = "content-cell";
                cell.textContent = value;
                row.appendChild(cell);
            }

            content.appendChild(row);
        }
    } catch (error) {
        console.error("Error fetching server data:", error);
    }
};
   

document.addEventListener('DOMContentLoaded', init);
