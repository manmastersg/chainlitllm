#!/bin/bash

# Define paths
BASE_DIR="/home/rdp/myproject/chainlitsrc"
BACKEND_DIR="$BASE_DIR/backend"
FRONTEND_DIR="$BASE_DIR/frontend"

echo "--- Starting Application Services ---"

# 1. Cleanup existing processes on ports 8001 and 3001
echo "[1/4] Cleaning up existing processes on ports 8001 and 3001..."
fuser -k 8001/tcp 2>/dev/null
fuser -k 3001/tcp 2>/dev/null
sleep 2

# 2. Build Frontend Assets
echo "[2/4] Building Frontend assets..."
cd "$FRONTEND_DIR"
pnpm build
cd "$BASE_DIR"

# 3. Start Backend (Chainlit)
echo "[3/4] Starting Backend (Chainlit) on port 8001..."
cd "$BACKEND_DIR"
# Using uv run to manage the environment automatically
uv run chainlit run auth_test.py --port 8001 --host 0.0.0.0 --root-path /chats > "$BACKEND_DIR/chainlit_exec.log" 2>&1 &
BACKEND_PID=$!

# 4. Start Frontend (Vite Dev Server)
echo "[4/4] Starting Frontend Dev Server on port 3001..."
cd "$FRONTEND_DIR"
# pnpm dev is configured for port 3001 in package.json
pnpm dev --host 0.0.0.0 > "$FRONTEND_DIR/frontend_exec.log" 2>&1 &
FRONTEND_PID=$!

echo "---------------------------------------"
echo "Services started successfully!"
echo "Backend PID: $BACKEND_PID (Log: $BACKEND_DIR/chainlit_exec.log)"
echo "Frontend PID: $FRONTEND_PID (Log: $FRONTEND_DIR/frontend_exec.log)"
echo ""
echo "App is accessible at:"
echo "- Direct Frontend: http://$(hostname -I | awk '{print $1}'):3001"
echo "- via Nginx: https://istart.hopto.org/chats"
echo "---------------------------------------"
