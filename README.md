# trading-bot-binance
Overview = This is a simple Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

Setup
 Clone the repository:
git clone https://github.com/your-username/trading-bot-binance.git
cd trading-bot-binance
Create virtual environment:
python -m venv venv
venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Add API keys in .env:
API_KEY=your_api_key
API_SECRET=your_secret_key

How to Run
MARKET Order
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
LIMIT Order
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

Assumptions
Binance Futures Testnet account is already created
API keys are valid
Python 3.x is installed

Requirements
python-binance
python-dotenv

Logs
Log file (bot.log) contains:
MARKET order execution
LIMIT order execution
API responses and errors
