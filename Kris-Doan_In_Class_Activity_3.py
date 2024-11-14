{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOAAdZfpLoTm3G9C2CaNrZG",
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
        "<a href=\"https://colab.research.google.com/github/Niceboy1147/CSC101/blob/main/Kris-Doan_In_Class_assignment3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "In Class Activity 3"
      ],
      "metadata": {
        "id": "WYrtUmRivMAI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip3 install ColabTurtle\n",
        "from ColabTurtle.Turtle import *"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cPbYxi5rvr1C",
        "outputId": "9dad676a-767c-4b55-8ad6-200eb9f0f6c7"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting ColabTurtle\n",
            "  Downloading ColabTurtle-2.1.0.tar.gz (6.8 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Building wheels for collected packages: ColabTurtle\n",
            "  Building wheel for ColabTurtle (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ColabTurtle: filename=ColabTurtle-2.1.0-py3-none-any.whl size=7642 sha256=b1216dfae121c458c30000f22df007caa16ea69e2b1f727e7a6979a6be78c441\n",
            "  Stored in directory: /root/.cache/pip/wheels/5b/86/e8/54f5c8c853606e3a3060bb2e60363cbed632374a12e0f33ffc\n",
            "Successfully built ColabTurtle\n",
            "Installing collected packages: ColabTurtle\n",
            "Successfully installed ColabTurtle-2.1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 1"
      ],
      "metadata": {
        "id": "UHBpoaEKwQWR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Octagon\n",
        "initializeTurtle ()\n",
        "import ColabTurtle.Turtle as turtle\n",
        "for i in range(1, 9):\n",
        "  turtle.forward(100)\n",
        "  turtle.left(45)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 521
        },
        "id": "lPqGZdZpwYmy",
        "outputId": "1bc500d9-53d4-4fb5-f9ad-480a9a814c13"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"500\">\n",
              "        <rect width=\"100%\" height=\"100%\" fill=\"black\"/>\n",
              "        <line x1=\"400\" y1=\"250\" x2=\"400.0\" y2=\"150.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"400.0\" y1=\"150.0\" x2=\"329.289\" y2=\"79.289\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"329.289\" y1=\"79.289\" x2=\"229.289\" y2=\"79.289\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"229.289\" y1=\"79.289\" x2=\"158.578\" y2=\"150.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"158.578\" y1=\"150.0\" x2=\"158.578\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"158.578\" y1=\"250.0\" x2=\"229.289\" y2=\"320.711\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"229.289\" y1=\"320.711\" x2=\"329.289\" y2=\"320.711\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"329.289\" y1=\"320.711\" x2=\"400.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/>\n",
              "        <g visibility=visible transform=\"rotate(360,400.0,250.0) translate(382.0, 232.0)\">\n",
              "<path style=\" stroke:none;fill-rule:evenodd;fill:white;fill-opacity:1;\" d=\"M 18.214844 0.632812 C 16.109375 1.800781 15.011719 4.074219 15.074219 7.132812 L 15.085938 7.652344 L 14.785156 7.496094 C 13.476562 6.824219 11.957031 6.671875 10.40625 7.066406 C 8.46875 7.550781 6.515625 9.15625 4.394531 11.992188 C 3.0625 13.777344 2.679688 14.636719 3.042969 15.027344 L 3.15625 15.152344 L 3.519531 15.152344 C 4.238281 15.152344 4.828125 14.886719 8.1875 13.039062 C 9.386719 12.378906 10.371094 11.839844 10.378906 11.839844 C 10.386719 11.839844 10.355469 11.929688 10.304688 12.035156 C 9.832031 13.09375 9.257812 14.820312 8.96875 16.078125 C 7.914062 20.652344 8.617188 24.53125 11.070312 27.660156 C 11.351562 28.015625 11.363281 27.914062 10.972656 28.382812 C 8.925781 30.84375 7.945312 33.28125 8.238281 35.1875 C 8.289062 35.527344 8.28125 35.523438 8.917969 35.523438 C 10.941406 35.523438 13.074219 34.207031 15.136719 31.6875 C 15.359375 31.417969 15.328125 31.425781 15.5625 31.574219 C 16.292969 32.042969 18.023438 32.964844 18.175781 32.964844 C 18.335938 32.964844 19.941406 32.210938 20.828125 31.71875 C 20.996094 31.625 21.136719 31.554688 21.136719 31.558594 C 21.203125 31.664062 21.898438 32.414062 22.222656 32.730469 C 23.835938 34.300781 25.5625 35.132812 27.582031 35.300781 C 27.90625 35.328125 27.9375 35.308594 28.007812 34.984375 C 28.382812 33.242188 27.625 30.925781 25.863281 28.425781 L 25.542969 27.96875 L 25.699219 27.785156 C 28.945312 23.960938 29.132812 18.699219 26.257812 11.96875 L 26.207031 11.84375 L 27.945312 12.703125 C 31.53125 14.476562 32.316406 14.800781 33.03125 14.800781 C 33.976562 14.800781 33.78125 13.9375 32.472656 12.292969 C 28.519531 7.355469 25.394531 5.925781 21.921875 7.472656 L 21.558594 7.636719 L 21.578125 7.542969 C 21.699219 6.992188 21.761719 5.742188 21.699219 5.164062 C 21.496094 3.296875 20.664062 1.964844 19.003906 0.855469 C 18.480469 0.503906 18.457031 0.5 18.214844 0.632812\"/>\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 2"
      ],
      "metadata": {
        "id": "wXK1o2SwyAta"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Two Stars\n",
        "initializeTurtle ()\n",
        "turtle.color(\"blue\")\n",
        "turtle.left(90)\n",
        "\n",
        "for i in range(1,6):\n",
        "  turtle.forward(150)\n",
        "  turtle.left(145)\n",
        "\n",
        "initializeTurtle ()\n",
        "turtle.color(\"red\")\n",
        "turtle.up()\n",
        "turtle.goto(500,250)\n",
        "turtle.right(90)\n",
        "turtle.pd()\n",
        "\n",
        "for i in range(1, 6):\n",
        "  turtle.forward(150)\n",
        "  turtle.right(145)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "_OhQSt5wyDim",
        "outputId": "16e633fc-4e3d-4e0d-cfe3-7bad587e4de5"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"500\">\n",
              "        <rect width=\"100%\" height=\"100%\" fill=\"black\"/>\n",
              "        <line x1=\"400\" y1=\"250\" x2=\"250.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"250.0\" y1=\"250.0\" x2=\"372.873\" y2=\"336.036\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"372.873\" y1=\"336.036\" x2=\"321.57\" y2=\"195.082\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"321.57\" y1=\"195.082\" x2=\"282.747\" y2=\"339.971\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"282.747\" y1=\"339.971\" x2=\"397.654\" y2=\"243.553\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/>\n",
              "        <g visibility=visible transform=\"rotate(265,397.654,243.553) translate(379.654, 225.553)\">\n",
              "<path style=\" stroke:none;fill-rule:evenodd;fill:blue;fill-opacity:1;\" d=\"M 18.214844 0.632812 C 16.109375 1.800781 15.011719 4.074219 15.074219 7.132812 L 15.085938 7.652344 L 14.785156 7.496094 C 13.476562 6.824219 11.957031 6.671875 10.40625 7.066406 C 8.46875 7.550781 6.515625 9.15625 4.394531 11.992188 C 3.0625 13.777344 2.679688 14.636719 3.042969 15.027344 L 3.15625 15.152344 L 3.519531 15.152344 C 4.238281 15.152344 4.828125 14.886719 8.1875 13.039062 C 9.386719 12.378906 10.371094 11.839844 10.378906 11.839844 C 10.386719 11.839844 10.355469 11.929688 10.304688 12.035156 C 9.832031 13.09375 9.257812 14.820312 8.96875 16.078125 C 7.914062 20.652344 8.617188 24.53125 11.070312 27.660156 C 11.351562 28.015625 11.363281 27.914062 10.972656 28.382812 C 8.925781 30.84375 7.945312 33.28125 8.238281 35.1875 C 8.289062 35.527344 8.28125 35.523438 8.917969 35.523438 C 10.941406 35.523438 13.074219 34.207031 15.136719 31.6875 C 15.359375 31.417969 15.328125 31.425781 15.5625 31.574219 C 16.292969 32.042969 18.023438 32.964844 18.175781 32.964844 C 18.335938 32.964844 19.941406 32.210938 20.828125 31.71875 C 20.996094 31.625 21.136719 31.554688 21.136719 31.558594 C 21.203125 31.664062 21.898438 32.414062 22.222656 32.730469 C 23.835938 34.300781 25.5625 35.132812 27.582031 35.300781 C 27.90625 35.328125 27.9375 35.308594 28.007812 34.984375 C 28.382812 33.242188 27.625 30.925781 25.863281 28.425781 L 25.542969 27.96875 L 25.699219 27.785156 C 28.945312 23.960938 29.132812 18.699219 26.257812 11.96875 L 26.207031 11.84375 L 27.945312 12.703125 C 31.53125 14.476562 32.316406 14.800781 33.03125 14.800781 C 33.976562 14.800781 33.78125 13.9375 32.472656 12.292969 C 28.519531 7.355469 25.394531 5.925781 21.921875 7.472656 L 21.558594 7.636719 L 21.578125 7.542969 C 21.699219 6.992188 21.761719 5.742188 21.699219 5.164062 C 21.496094 3.296875 20.664062 1.964844 19.003906 0.855469 C 18.480469 0.503906 18.457031 0.5 18.214844 0.632812\"/>\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"500\">\n",
              "        <rect width=\"100%\" height=\"100%\" fill=\"black\"/>\n",
              "        <line x1=\"500\" y1=\"250\" x2=\"650.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"650.0\" y1=\"250.0\" x2=\"527.127\" y2=\"336.036\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"527.127\" y1=\"336.036\" x2=\"578.43\" y2=\"195.082\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"578.43\" y1=\"195.082\" x2=\"617.253\" y2=\"339.971\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"617.253\" y1=\"339.971\" x2=\"502.346\" y2=\"243.553\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/>\n",
              "        <g visibility=visible transform=\"rotate(95,502.346,243.553) translate(484.346, 225.553)\">\n",
              "<path style=\" stroke:none;fill-rule:evenodd;fill:red;fill-opacity:1;\" d=\"M 18.214844 0.632812 C 16.109375 1.800781 15.011719 4.074219 15.074219 7.132812 L 15.085938 7.652344 L 14.785156 7.496094 C 13.476562 6.824219 11.957031 6.671875 10.40625 7.066406 C 8.46875 7.550781 6.515625 9.15625 4.394531 11.992188 C 3.0625 13.777344 2.679688 14.636719 3.042969 15.027344 L 3.15625 15.152344 L 3.519531 15.152344 C 4.238281 15.152344 4.828125 14.886719 8.1875 13.039062 C 9.386719 12.378906 10.371094 11.839844 10.378906 11.839844 C 10.386719 11.839844 10.355469 11.929688 10.304688 12.035156 C 9.832031 13.09375 9.257812 14.820312 8.96875 16.078125 C 7.914062 20.652344 8.617188 24.53125 11.070312 27.660156 C 11.351562 28.015625 11.363281 27.914062 10.972656 28.382812 C 8.925781 30.84375 7.945312 33.28125 8.238281 35.1875 C 8.289062 35.527344 8.28125 35.523438 8.917969 35.523438 C 10.941406 35.523438 13.074219 34.207031 15.136719 31.6875 C 15.359375 31.417969 15.328125 31.425781 15.5625 31.574219 C 16.292969 32.042969 18.023438 32.964844 18.175781 32.964844 C 18.335938 32.964844 19.941406 32.210938 20.828125 31.71875 C 20.996094 31.625 21.136719 31.554688 21.136719 31.558594 C 21.203125 31.664062 21.898438 32.414062 22.222656 32.730469 C 23.835938 34.300781 25.5625 35.132812 27.582031 35.300781 C 27.90625 35.328125 27.9375 35.308594 28.007812 34.984375 C 28.382812 33.242188 27.625 30.925781 25.863281 28.425781 L 25.542969 27.96875 L 25.699219 27.785156 C 28.945312 23.960938 29.132812 18.699219 26.257812 11.96875 L 26.207031 11.84375 L 27.945312 12.703125 C 31.53125 14.476562 32.316406 14.800781 33.03125 14.800781 C 33.976562 14.800781 33.78125 13.9375 32.472656 12.292969 C 28.519531 7.355469 25.394531 5.925781 21.921875 7.472656 L 21.558594 7.636719 L 21.578125 7.542969 C 21.699219 6.992188 21.761719 5.742188 21.699219 5.164062 C 21.496094 3.296875 20.664062 1.964844 19.003906 0.855469 C 18.480469 0.503906 18.457031 0.5 18.214844 0.632812\"/>\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 3"
      ],
      "metadata": {
        "id": "93PaXOqX06cg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Own Design\n",
        "initializeTurtle ()\n",
        "turtle.color(\"blue\")\n",
        "turtle.up()\n",
        "turtle.goto(350,250)\n",
        "turtle.pd()\n",
        "turtle.fd(50)\n",
        "turtle.lt(90)\n",
        "turtle.fd(200)\n",
        "turtle.lt(90)\n",
        "turtle.fd(50)\n",
        "turtle.lt(90)\n",
        "turtle.fd(200)\n",
        "turtle.color(\"white\")\n",
        "turtle.fd(100)\n",
        "turtle.lt(90)\n",
        "turtle.fd(50)\n",
        "turtle.lt(90)\n",
        "turtle.fd(100)\n",
        "turtle.lt(90)\n",
        "turtle.fd(50)\n",
        "turtle.lt(90)\n",
        "turtle.fd(100)\n",
        "turtle.color(\"red\")\n",
        "turtle.fd(200)\n",
        "turtle.lt(90)\n",
        "turtle.fd(50)\n",
        "turtle.lt(90)\n",
        "turtle.fd(200)\n",
        "turtle.lt(90)\n",
        "turtle.color(\"white\")\n",
        "turtle.fd(50)\n",
        "turtle.up()\n",
        "turtle.goto(140,240)\n",
        "turtle.pd()\n",
        "turtle.rt(90)\n",
        "turtle.color(\"blue\")\n",
        "turtle.fd(25)\n",
        "turtle.up()\n",
        "turtle.goto(140,225)\n",
        "turtle.pd()\n",
        "turtle.fd(25)\n",
        "turtle.up()\n",
        "turtle.goto(140,210)\n",
        "turtle.pd()\n",
        "turtle.fd(25)\n",
        "turtle.up()\n",
        "turtle.goto(660,240)\n",
        "turtle.color(\"red\")\n",
        "turtle.pd()\n",
        "turtle.bk(25)\n",
        "turtle.up()\n",
        "turtle.goto(660,225)\n",
        "turtle.pd()\n",
        "turtle.bk(25)\n",
        "turtle.up()\n",
        "turtle.goto(660,210)\n",
        "turtle.pd()\n",
        "turtle.bk(25)\n",
        "turtle.up()\n",
        "turtle.goto(0,0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 521
        },
        "id": "PbHXv1Ps08fx",
        "outputId": "64aad314-3f5e-4411-c94a-d92c92347eef"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "      <svg width=\"800\" height=\"500\">\n",
              "        <rect width=\"100%\" height=\"100%\" fill=\"black\"/>\n",
              "        <line x1=\"350\" y1=\"250\" x2=\"350.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"350.0\" y1=\"200.0\" x2=\"150.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"150.0\" y1=\"200.0\" x2=\"150.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"150.0\" y1=\"250.0\" x2=\"350.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"350.0\" y1=\"250.0\" x2=\"450.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"450.0\" y1=\"250.0\" x2=\"450.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"450.0\" y1=\"200.0\" x2=\"350.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"350.0\" y1=\"200.0\" x2=\"350.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"350.0\" y1=\"250.0\" x2=\"450.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"450.0\" y1=\"250.0\" x2=\"650.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"650.0\" y1=\"250.0\" x2=\"650.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"650.0\" y1=\"200.0\" x2=\"450.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"450.0\" y1=\"200.0\" x2=\"450.0\" y2=\"250.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"140\" y1=\"240\" x2=\"115.0\" y2=\"240.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"140\" y1=\"225\" x2=\"115.0\" y2=\"225.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"140\" y1=\"210\" x2=\"115.0\" y2=\"210.0\" stroke-linecap=\"round\" style=\"stroke:blue;stroke-width:4\"/><line x1=\"660\" y1=\"240\" x2=\"685.0\" y2=\"240.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"660\" y1=\"225\" x2=\"685.0\" y2=\"225.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/><line x1=\"660\" y1=\"210\" x2=\"685.0\" y2=\"210.0\" stroke-linecap=\"round\" style=\"stroke:red;stroke-width:4\"/>\n",
              "        <g visibility=visible transform=\"rotate(270,0,0) translate(-18, -18)\">\n",
              "<path style=\" stroke:none;fill-rule:evenodd;fill:red;fill-opacity:1;\" d=\"M 18.214844 0.632812 C 16.109375 1.800781 15.011719 4.074219 15.074219 7.132812 L 15.085938 7.652344 L 14.785156 7.496094 C 13.476562 6.824219 11.957031 6.671875 10.40625 7.066406 C 8.46875 7.550781 6.515625 9.15625 4.394531 11.992188 C 3.0625 13.777344 2.679688 14.636719 3.042969 15.027344 L 3.15625 15.152344 L 3.519531 15.152344 C 4.238281 15.152344 4.828125 14.886719 8.1875 13.039062 C 9.386719 12.378906 10.371094 11.839844 10.378906 11.839844 C 10.386719 11.839844 10.355469 11.929688 10.304688 12.035156 C 9.832031 13.09375 9.257812 14.820312 8.96875 16.078125 C 7.914062 20.652344 8.617188 24.53125 11.070312 27.660156 C 11.351562 28.015625 11.363281 27.914062 10.972656 28.382812 C 8.925781 30.84375 7.945312 33.28125 8.238281 35.1875 C 8.289062 35.527344 8.28125 35.523438 8.917969 35.523438 C 10.941406 35.523438 13.074219 34.207031 15.136719 31.6875 C 15.359375 31.417969 15.328125 31.425781 15.5625 31.574219 C 16.292969 32.042969 18.023438 32.964844 18.175781 32.964844 C 18.335938 32.964844 19.941406 32.210938 20.828125 31.71875 C 20.996094 31.625 21.136719 31.554688 21.136719 31.558594 C 21.203125 31.664062 21.898438 32.414062 22.222656 32.730469 C 23.835938 34.300781 25.5625 35.132812 27.582031 35.300781 C 27.90625 35.328125 27.9375 35.308594 28.007812 34.984375 C 28.382812 33.242188 27.625 30.925781 25.863281 28.425781 L 25.542969 27.96875 L 25.699219 27.785156 C 28.945312 23.960938 29.132812 18.699219 26.257812 11.96875 L 26.207031 11.84375 L 27.945312 12.703125 C 31.53125 14.476562 32.316406 14.800781 33.03125 14.800781 C 33.976562 14.800781 33.78125 13.9375 32.472656 12.292969 C 28.519531 7.355469 25.394531 5.925781 21.921875 7.472656 L 21.558594 7.636719 L 21.578125 7.542969 C 21.699219 6.992188 21.761719 5.742188 21.699219 5.164062 C 21.496094 3.296875 20.664062 1.964844 19.003906 0.855469 C 18.480469 0.503906 18.457031 0.5 18.214844 0.632812\"/>\n",
              "</g>\n",
              "      </svg>\n",
              "    "
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}
