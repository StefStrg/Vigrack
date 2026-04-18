SCRIPT_PATH="$(pwd)/vigrack.py"

chmod +x "$SCRIPT_PATH"
sudo ln -sf "$SCRIPT_PATH" /usr/local/bin/vigrack
echo "Success! You can now use 'vigrack' from any directory."
