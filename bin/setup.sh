#!/bin/bash

echo "🚀 Setting up Stock Price Analyzer 📈"

echo "🔨 Building Docker container..."
docker-compose build

if [ $? -ne 0 ]; then
  echo "❌ Error: Docker container build failed!"
  exit 1
fi

echo "🚀 Starting Docker containers in detached mode..."
docker-compose up -d

if [ $? -ne 0 ]; then
  echo "❌ Error: Docker containers failed to start!"
  exit 1
fi

echo "🚧 Running unit tests..."
python3 -m unittest

if [ $? -ne 0 ]; then
  echo "❌ Error: Unit tests failed!"
  exit 1
fi

echo "✅ Setup completed successfully! Enjoy analyzing stock prices! 📊📉📈"