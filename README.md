{\rtf1\ansi\ansicpg936\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\
A CLI chatbot that lets you chat with SpongeBob SquarePants using the ai.sooners.us API.\
\
## Requirements\
\
- Python 3.8 or higher\
- API key from ai.sooners.us\
\
## Setup Instructions\
\
1. **Get your API key:**\
   - Visit https://ai.sooners.us\
   - Sign up with your OU email\
   - Go to Settings \uc0\u8594  Account \u8594  API Keys\
   - Create a new API key and copy it\
2. **Create environment file:**\
   \
   Create a file at `~/.soonerai.env` with:\
\
   SOONERAI_API_KEY=your_key_here\
   SOONERAI_BASE_URL=https://ai.sooners.us\
   SOONERAI_MODEL=gemma3:4b\
   \
   Replace `your_key_here` with your actual API key.\
\
## How to Run\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 pip install -r requirements.txt\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 python spongebob_cli.py\
\
Type your messages and press Enter. Type 'quit', 'exit', or 'bye' to end the conversation.\
\
\
## Project Structure\
\
- `spongebob_cli.py` - Main chatbot script\
- `requirements.txt` - Python dependencies\
- `README.md` - This file\
- `.gitignore` - Excludes env files from Git\
\
}