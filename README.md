# Arma Server Monitor

A small server status page for an Arma server. The backend queries the server through the A2S protocol and returns its current status, map, player count, and connection details. The frontend is a plain HTML/CSS/JavaScript page that displays the response.

## Running it

The easiest way to run the backend is with Docker Compose:

```sh
docker compose up --build
```

The API will be available at `http://127.0.0.1:8000`.

To run it without Docker:

```sh
python -m venv .venv
```

Activate the virtual environment, then install the dependencies:

```sh
pip install -r requirements.txt
waitress-serve --listen=127.0.0.1:8000 backend.backend:app
```

The frontend files can be served by any static web server. Opening `frontend/index.html` directly is also enough for a quick look, although the page currently fetches data from the deployed API at `https://api.darianelwood.com/v1/api/serverQuery`.

## API

`GET /v1/api/serverQuery` returns an array containing one object per configured server. A server that cannot be reached is returned with a `Server unreachable` status instead of failing the whole request.

Example response:

```json
[
	{
		"status": "Server is up.",
		"server_name": "Example server",
		"game": "Arma 3",
		"map": "Altis",
		"server_address": "example.com",
		"server_port": 2303,
		"players": 4,
		"max_players": 64
	}
]
```

## Adding a server

The monitored addresses are defined in `backend/backend.py`. Add another `Address(host, port)` entry to the list passed to `Monitor`.

## License

This project is licensed under the GNU General Public License v3. See `LICENSE` for the full text.
