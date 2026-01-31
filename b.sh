#!/bin/bash
echo "🚀 Memulai siklus download/hapus..."
while true
do
    npm install raproxy
    echo "✅ Downloaded. Now deleting..."
    rm -rf node_modules
done
