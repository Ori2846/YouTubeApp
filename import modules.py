import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("tk")
install("Pillow")
install("urllib3")
install("yt-dlp")