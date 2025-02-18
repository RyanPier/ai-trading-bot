#!/bin/bash
gunicorn -w 4 -b 0.0.0.0:8000 ai_trading_bot:app
