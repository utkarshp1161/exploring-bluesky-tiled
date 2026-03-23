import subprocess
subprocess.run(["tiled", "serve", "directory", "data", "--public", "--watch"], check=True)
# subprocess.run(["tiled", "serve", "directory", "data", "--public"], check=True)