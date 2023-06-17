{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/jmasonlee/efficiently_testing_etl_pipelines/blob/main/diamonds.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Efficiencies of Right Sizing Tests\n"
      ],
      "metadata": {
        "id": "Bhc_PE_4BrpG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "This exercise is meant to give you a practical example on how the number of inputs to a test affect the number of tests you need to write and maintain in order to fully cover your system."
      ],
      "metadata": {
        "id": "qljkG08NDynH"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Install Dependencies\n",
        "\n",
        "For the exercise, we will need some special dependencies to allow us to run tests with lots of combinations"
      ],
      "metadata": {
        "id": "_h199h_XEAwT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install ipytest\n",
        "!pip install pyspark\n",
        "!pip install approvaltests"
      ],
      "metadata": {
        "id": "7v0kaWulDXi-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0_BcRiFvBeLs"
      },
      "outputs": [],
      "source": [
        "import pytest\n",
        "import ipytest\n",
        "ipytest.autoconfig()\n",
        "from diamonds import replace_null_prices_with_floating_averages\n",
        "from pyspark import SparkConf\n",
        "\n",
        "from pyspark.sql import SparkSession\n",
        "from verification_helpers import verify_will_replace_null_values_with_floating_averages\n",
        "from _pytest.fixtures import FixtureRequest\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "@pytest.fixture(scope=\"session\")\n",
        "def spark(request: FixtureRequest):\n",
        "    conf = (SparkConf()\n",
        "        .setMaster(\"local\")\n",
        "        .setAppName(\"sample_pyspark_testing_starter\"))\n",
        "\n",
        "    spark = SparkSession \\\n",
        "        .builder \\\n",
        "        .config(conf=conf) \\\n",
        "        .getOrCreate()\n",
        "\n",
        "    request.addfinalizer(lambda: spark.stop())\n",
        "    return spark"
      ],
      "metadata": {
        "id": "V6XwgiHHJrYr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%ipytest -qq\n",
        "def test_will_replace_null_prices_with_floating_averages(spark: SparkSession) -> None:\n",
        "    price = [327, None]\n",
        "\n",
        "    verify_will_replace_null_values_with_floating_averages(spark, price)"
      ],
      "metadata": {
        "id": "lfANxIAgIFEz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section\n"
      ],
      "metadata": {
        "id": "TATb7BjoCXP6"
      }
    }
  ]
}