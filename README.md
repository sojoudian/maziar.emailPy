# Python HTTP Server

This repository contains a simple HTTP server using Python’s built-in `http.server` module. It serves static files from the `templates/` directory without requiring external dependencies like Flask.

## Features
- Uses Python’s standard library (`http.server` and `socketserver`).
- Serves files dynamically from the `templates/` directory.
- Graceful handling of errors, including port conflicts and keyboard interrupts.
- Runs on `0.0.0.0:8002` by default for network accessibility.

## Installation & Usage

### 1. Clone the Repository
```sh
git clone https://github.com/mazair/maziar.emailPy.git
cd python-http-server
```

### 2. Run the Server
Ensure Python (3.x) is installed, then start the server:
```sh
python server.py
```

### 3. Access the Server
Open a browser and navigate to:
```
http://localhost:8002/
```
The server serves files from the `templates/` directory.

## Configuration
- **Change the Port:** Modify the `PORT` variable in `server.py`.
- **Change the Directory:** Set the `DIRECTORY` variable to a different folder.

## Stopping the Server
To stop the server, press `CTRL + C` in the terminal.

## License
This project is open-source and available under the MIT License.

---

**Author:** Maziar Sojoudian
**GitHub:** [sojoudian](https://github.com/sojoudian)

