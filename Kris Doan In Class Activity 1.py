{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "\n",
        "##Instructions for In Class Activity 1\n",
        "\n",
        "You must find all errors in your scripts. But because you are communicating with a machine, not a person, you have to be exact: the computer cannot understand you at all if there are errors, bugs, in your code. Or the computer may do exactly what you wrote, but not what you meant to do.\n",
        "\n",
        "Add a comment to the file that describes what you did.\n",
        "\n",
        "Change the file name to \"your name In Class Activity 1\" and hand in these corrected Python scripts!\n",
        "\n"
      ],
      "metadata": {
        "id": "4VrSYGZZmO7v"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 1"
      ],
      "metadata": {
        "id": "pitapNW7ScyM"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "collapsed": true,
        "id": "DTmAjv3VSTtN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eb2e5a1a-08b3-4e47-fafe-73e2100fa26a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.0\n"
          ]
        }
      ],
      "source": [
        "x = 15\n",
        "y = 5\n",
        "z = 3\n",
        "# removed y=0\n",
        "k = x / y\n",
        "print(k)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 2"
      ],
      "metadata": {
        "id": "rNOElr3mSwDm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = 10\n",
        "y = 20\n",
        "z = 30\n",
        "print(x, y, z) # removed indent"
      ],
      "metadata": {
        "id": "yIuX2GwTSyEy",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d590b1d5-ff27-4064-bc00-fe4a3ba3eaa9"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 20 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 3"
      ],
      "metadata": {
        "id": "d0-zG7VsS7KZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# This program converts miles to km\n",
        "\n",
        "miles = 10\n",
        "multiplier = 1.609344\n",
        "km = miles * multiplier # changed \"multplier\" to \"multiplier\"\n",
        "print(km)"
      ],
      "metadata": {
        "id": "2cznlPZPS8V7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4d6aff67-69f7-4a25-97e4-b68b5ec1e1cd"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "16.09344\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 4"
      ],
      "metadata": {
        "id": "qrVE3Ww1UeWR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1\n",
        "y = 10\n",
        "z = 2\n",
        "t = 15\n",
        "print((x * t) / (y / z)) # added additional \")\"\n",
        "print('Done')"
      ],
      "metadata": {
        "id": "tg2EcgYoUfpI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fa07fa2a-90d1-4109-b3be-e9b445b5dde6"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.0\n",
            "Done\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 5"
      ],
      "metadata": {
        "id": "reMlWZmYU5Xr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "fruit = \"kiwi\"\n",
        "print(fruit, fruit, fruit) # corrected \"frut\" to \"fruit\""
      ],
      "metadata": {
        "id": "d12bxUkVU7j6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fd4266e8-a815-4ec6-a655-b8bf395ef29b"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "kiwi kiwi kiwi\n"
          ]
        }
      ]
    }
  ]
}