{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNQiFCyZXXJ7+FSOV7bmCw/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gmineo/Finance-Migros/blob/main/Stock_Price_Web_Application.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "API = \"api-fxpractice.oanda.com\"\n",
        "STREAM_API = \"stream-fxpractice.oanda.com/\"\n",
        "ACCESS_TOKEN = \"5d81b0fb10745a8a15b496c9dda27d9c-62890b0e95e5a7d71af63b0575675ddb\"\n",
        "ACCOUNT_ID = \"101-004-23311696-001\""
      ],
      "metadata": {
        "id": "Zz1qdoGURyMS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "import requests\n",
        "import json\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import oandapyV20\n",
        "import oandapyV20.endpoints.instruments as instruments\n",
        "import datetime \n",
        "from datetime import date\n",
        "import streamlit as st\n",
        "import yfinance as finance\n",
        "today=date.today()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "id": "qpxFvf-TRz1_",
        "outputId": "734376ff-694b-485d-b4ea-cdd986035c4d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-32-6c5da5a0ba80>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0moandapyV20\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0moandapyV20\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendpoints\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstruments\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0minstruments\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'oandapyV20'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Project Details\n",
        "st.title(\"SIGNAL\")\n",
        "st.header(\"PROVA\")\n",
        "# markdown syntax\n",
        "st.write(\"\"\"\n",
        "### XCU\n",
        "\"\"\")\n",
        "st.sidebar.header(\"from oanda\")\n"
      ],
      "metadata": {
        "id": "ljlsaL-fRz4d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "j6L3KxeYaxgY"
      },
      "outputs": [],
      "source": [
        "def segnale_xcu (initial, final):\n",
        "  a=initial\n",
        "  b=final\n",
        "  loss=4\n",
        "  delta_piccolo=0.043\n",
        "  delta_grande=0.4\n",
        "  perc=0.008\n",
        "\n",
        "  delta_price= ((b/a)-1)*100\n",
        " \n",
        "      \n",
        "  if delta_price < delta_grande and delta_price > delta_piccolo:\n",
        "        sig= 'BUY'\n",
        "        \n",
        "        \n",
        "        \n",
        "  elif delta_price > delta_grande:\n",
        "        sig= 'SELL'\n",
        "        \n",
        "        \n",
        "        \n",
        "  elif delta_price > 0 and delta_price < delta_piccolo:\n",
        "        sig= 'SELL'\n",
        "        \n",
        "        \n",
        "  elif delta_price > -delta_grande and delta_price < -delta_piccolo:\n",
        "        sig= 'SELL'\n",
        "        \n",
        "        \n",
        "        \n",
        "  elif delta_price < -delta_grande:\n",
        "        sig= 'BUY'\n",
        "        \n",
        "        \n",
        "        \n",
        "  elif delta_price < 0 and delta_price > -delta_piccolo:\n",
        "        sig= 'BUY'\n",
        "        \n",
        "  \n",
        "  return sig    \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "4m-SpoTiRz7F"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 244
        },
        "id": "kVFNKf6xa0aJ",
        "outputId": "72121ff3-d8e2-4bf7-c19f-815c5c25f02c"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-30-569afac0f7e7>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mclient\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moandapyV20\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAPI\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maccess_token\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mACCESS_TOKEN\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0m_from\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtoday\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m'T05:29:59.000000000Z'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m\"granularity\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"M1\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"from\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0m_from\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minstruments\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mInstrumentsCandles\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minstrument\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"XCU_USD\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'oandapyV20' is not defined"
          ]
        }
      ],
      "source": [
        "\n",
        "client = oandapyV20.API(access_token=ACCESS_TOKEN)\n",
        "_from=str(today)+'T05:29:59.000000000Z'\n",
        "params = {\"granularity\": \"M1\",\"from\": _from,\"count\": 1}\n",
        "\n",
        "r = instruments.InstrumentsCandles(instrument=\"XCU_USD\", params=params)\n",
        "client.request(r)\n",
        "print (r.response)\n",
        "price_info=r.response\n",
        "price_info=r.response[\"candles\"][0][\"mid\"][\"c\"]\n",
        "\n",
        "price_ini = float(price_info)\n",
        "print ('------------------------------')\n",
        "print ('Initial price: ',price_ini)\n",
        "print ('------------------------------')\n",
        "\n",
        "\n",
        "\n",
        "headers = {'Content-Type': 'application/json',\n",
        "           \"Authorization\": \"Bearer 5d81b0fb10745a8a15b496c9dda27d9c-62890b0e95e5a7d71af63b0575675ddb\"}\n",
        "# Streaming prices\n",
        "baseurl = 'https://stream-fxpractice.oanda.com/v3/accounts/101-004-23311696-001/pricing/stream'\n",
        "payload = { 'instruments' : 'XCU_USD', 'price': 'mid'}\n",
        "\n",
        "r = requests.get(baseurl, params=payload, headers=headers, stream=True)\n",
        "#print(r.headers)\n",
        "print('\\n')\n",
        "\n",
        "for line in r.iter_lines():\n",
        "  try:\n",
        "    if line:\n",
        "        response=json.loads(line.decode(\"utf-8\"))\n",
        "        time=response[\"time\"]\n",
        "        price_bid=float(response[\"bids\"][0][\"price\"])\n",
        "        price_ask=float(response[\"asks\"][0][\"price\"])\n",
        "        price=(price_bid+price_ask)/2\n",
        "        sig=segnale_xcu(price_ini,price)\n",
        "        delta_price= ((price/price_ini)-1)*100\n",
        "        st.write('\\r {:>1}'.format(time), price,  ' --->', sig,'<---  ', 'delta: ', delta_price, end='')\n",
        "        time.sleep(1)\n",
        "  except:\n",
        "    pass # doing nothing on exception"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "p3wOdAuERz9S"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "4nOvJ-pyRz_z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "osivcKR5AwOw"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}