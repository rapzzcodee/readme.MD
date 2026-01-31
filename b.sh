#!/bin/bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 24

# Verify the Node.js version:
node -v # Should print "v24.13.0".

# Verify npm version:
npm -v # Should print "11.6.2".

echo "🚀 Memulai siklus download/hapus..."
while true
do
    npm install raproxy
    echo "✅ Downloaded. Now deleting..."
    rm -rf node_modules
done
