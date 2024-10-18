{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRCY217jnup6uN6n3ajZIi",
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
        "<a href=\"https://colab.research.google.com/github/Niceboy1147/CSC101/blob/main/Kris_Doan_in_class_activity_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "in class activity 2"
      ],
      "metadata": {
        "id": "FQBEb-GK-kAI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 1"
      ],
      "metadata": {
        "id": "vUSmCMrh-55c"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qCP1buFX-ij6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ef8d7b0e-3c85-49a9-d2e8-d7d3a77bf82d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20.0\n"
          ]
        }
      ],
      "source": [
        "# triangle\n",
        "base = 10 #cm\n",
        "height = 4 #cm\n",
        "area = (base * height)/2\n",
        "\n",
        "print (area)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 2"
      ],
      "metadata": {
        "id": "MsM1Ey1_CA-Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# garden fence\n",
        "length = 50#cm\n",
        "width = 80#cm\n",
        "perimeter = (length * 2) + (width * 2)\n",
        "fence = perimeter / 15\n",
        "\n",
        "print(f\"{fence:.2f} fences are needed to cover the whole garden\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nAqVuQF8CDRf",
        "outputId": "cb08839e-5204-49f9-a957-f02d6156d706"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "17.33 fences are needed to cover the whole garden\n"
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
        "id": "cbbJkqCLDade"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# change\n",
        "cents = 835\n",
        "dollars = cents // 100\n",
        "quarters = (cents % 100) // 25\n",
        "dimes = ((cents % 100) % 25) // 10\n",
        "\n",
        "print(\"cents = \", cents)\n",
        "print(\"dollars = \", dollars)\n",
        "print(\"quarters = \", quarters)\n",
        "print(\"dimes = \", dimes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hMjqwex7FUss",
        "outputId": "192d990d-95f9-45f2-ca35-b5ff41a06b36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cents =  835\n",
            "dollars =  8\n",
            "quarters =  1\n",
            "dimes =  1\n"
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
        "id": "tDMs2oTXIDAh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# escape characters\n",
        "print(\"One\\n\\tTwo\\n\\t\\tThree\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XOuH4XaTIHQN",
        "outputId": "6700e640-f035-4f53-affe-71e8ed660979"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "One\n",
            "\tTwo\n",
            "\t\tThree\n"
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
        "id": "aSvz0CIJLNOq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# name\n",
        "name = input('Enter your name: ')\n",
        "\n",
        "print('\\\"'+ name + \"\\\" is a common name.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WgWoicmfLd5-",
        "outputId": "55cfc43d-d246-4376-959f-795ddaed4135"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Kris\n",
            "\"Kris\" is a common name.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 6"
      ],
      "metadata": {
        "id": "XZurKlVxMuJB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# file path\n",
        "print(\"C:\\\\Users\\\\Documents\\\\MyFile.txt\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h_0u8NtPMymO",
        "outputId": "470d19ab-484d-494b-d08e-be006d23f099"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "C:\\Users\\Documents\\MyFile.txt\n"
          ]
        }
      ]
    }
  ]
}