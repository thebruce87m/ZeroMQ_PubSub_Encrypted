# Installation
 - Clone the repo

 - (Optional) Create Virtual Environment
```bash
python3 -m venv env
```
 - Activate env
      - Linux/mac
     ```bash
     source env/bin/activate
     ```
      - Windows
     ```bash
     env/Scripts/activate
     ```

 - Install requirements
```bash
pip3 install -r requirements.txt
```

# Usage

## Generate keys

```bash
python3 generate_certificates.py
```

## Run the server ( Terminal 1 )

```bash
python3 example-server.py
```

# Run the client ( Terminal 2 )

```bash
python3 example-client.py
```