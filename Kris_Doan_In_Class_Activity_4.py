{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOvPpQN/h8TH5/x5pIxqasg",
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
        "<a href=\"https://colab.research.google.com/github/Niceboy1147/CSC101/blob/main/Kris_Doan_In_Class_Activity4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "In Class Activity 4"
      ],
      "metadata": {
        "id": "vbudHEoXAtPq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 1"
      ],
      "metadata": {
        "id": "D1cUOrkOAxx-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Display Info\n",
        "def display_info():\n",
        "  print (\"Title: Metro 2035\")\n",
        "  print (\"Author: Dmitry Glukhovsky\")\n",
        "  print (\"Description: Two years after the residents of the Metro’s very existence is threatened,\")\n",
        "  print (\"Artyom keeps his dream alive: to take the survivors back to the surface of the Earth, and find a new home.\")\n",
        "  print (\"Every day, he ventures out of the Metro to scan the airwaves,\")\n",
        "  print (\"taking in a new dose of radiation with every minute spent outside of the tunnels.\")\n",
        "  print (\"One day he hears of a man who found signals from other survivors.\")\n",
        "  print (\"To find him, Artyom will venture on his last journey through the tunnels and make discoveries that will turn his world upside down.\")\n",
        "\n",
        "display_info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mVDN3HCBA1Dd",
        "outputId": "f2e45a2e-daa6-4676-ccd7-2b685bad3014"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Title: Metro 2035\n",
            "Author: Dmitry Glukhovsky\n",
            "Description: Two years after the residents of the Metro’s very existence is threatened,\n",
            "Artyom keeps his dream alive: to take the survivors back to the surface of the Earth, and find a new home.\n",
            "Every day, he ventures out of the Metro to scan the airwaves,\n",
            "taking in a new dose of radiation with every minute spent outside of the tunnels.\n",
            "One day he hears of a man who found signals from other survivors.\n",
            "To find him, Artyom will venture on his last journey through the tunnels and make discoveries that will turn his world upside down.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Question 2"
      ],
      "metadata": {
        "id": "-D-LwqlJEVB-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Top Attractions\n",
        "def London():\n",
        "  print (\"Top London Attractions:\", \"1. London Tower\", \"2. London Eye\", \"3. The National Gallery\")\n",
        "\n",
        "def Paris():\n",
        "  print (\"Top Paris Attractions:\", \"1. The Eiffel Tower\", \"2. Musée du Louvre\", \"3. Notre-Dame Cathedral\")\n",
        "\n",
        "def NYC():\n",
        "  print (\"Top NYC Attractions:\", \"1. Central Park\", \"2. National September 11 Memorial and Museum\", \"3. Empire State Building\")\n",
        "\n",
        "London()\n",
        "Paris()\n",
        "NYC()"
      ],
      "metadata": {
        "id": "Qe9IthQWEXjw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "89893727-aee0-4a3b-b766-4b9d62ed823b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Top London Attractions: 1. London Tower 2. London Eye 3. The National Gallery\n",
            "Top Paris Attractions: 1. The Eiffel Tower 2. Musée du Louvre 3. Notre-Dame Cathedral\n",
            "Top NYC Attractions: 1. Central Park 2. National September 11 Memorial and Museum 3. Empire State Building\n"
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
        "id": "MNGyZfqOJ8nB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Install Turtle\n",
        "!pip3 install ColabTurtle\n",
        "from ColabTurtle.Turtle import *\n",
        "import ColabTurtle.Turtle as turtle"
      ],
      "metadata": {
        "id": "7LKGImnZMBk-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b4a68acd-8f18-47b7-e6a7-b6de76a53352"
      },
      "execution_count": 1,
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
            "  Created wheel for ColabTurtle: filename=ColabTurtle-2.1.0-py3-none-any.whl size=7642 sha256=dade6847b746f6ee2fb8d678333dd87b86a8c4c674237c2af64d4ffe3eb3066c\n",
            "  Stored in directory: /root/.cache/pip/wheels/5b/86/e8/54f5c8c853606e3a3060bb2e60363cbed632374a12e0f33ffc\n",
            "Successfully built ColabTurtle\n",
            "Installing collected packages: ColabTurtle\n",
            "Successfully installed ColabTurtle-2.1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Square Turtle\n",
        "\n",
        "initializeTurtle()\n",
        "def draw_square():\n",
        "  turtle.fd(100)\n",
        "  turtle.lt(90)\n",
        "  turtle.fd(100)\n",
        "  turtle.lt(90)\n",
        "  turtle.fd(100)\n",
        "  turtle.lt(90)\n",
        "  turtle.fd(100)\n",
        "  turtle.lt(90)\n",
        "\n",
        "turtle.up()\n",
        "turtle.goto(300, 300)\n",
        "turtle.pd()\n",
        "draw_square()\n",
        "\n",
        "turtle.up()\n",
        "turtle.goto(450, 300)\n",
        "turtle.pd()\n",
        "draw_square()\n",
        "\n",
        "turtle.up()\n",
        "turtle.goto(600, 300)\n",
        "turtle.pd()\n",
        "draw_square()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 521
        },
        "id": "_bJJwcUKJ__7",
        "outputId": "b55b1ab7-745c-4caa-d28f-0e8e31a3fcb0"
      },
      "execution_count": null,
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
              "        <line x1=\"250\" y1=\"300\" x2=\"250.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"250.0\" y1=\"200.0\" x2=\"150.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"150.0\" y1=\"200.0\" x2=\"150.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"150.0\" y1=\"300.0\" x2=\"250.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"400\" y1=\"300\" x2=\"400.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"400.0\" y1=\"200.0\" x2=\"300.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"300.0\" y1=\"200.0\" x2=\"300.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"300.0\" y1=\"300.0\" x2=\"400.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"550\" y1=\"300\" x2=\"550.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"550.0\" y1=\"200.0\" x2=\"450.0\" y2=\"200.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"450.0\" y1=\"200.0\" x2=\"450.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/><line x1=\"450.0\" y1=\"300.0\" x2=\"550.0\" y2=\"300.0\" stroke-linecap=\"round\" style=\"stroke:white;stroke-width:4\"/>\n",
              "        <g visibility=visible transform=\"rotate(360,550.0,300.0) translate(532.0, 282.0)\">\n",
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
        "Question 4"
      ],
      "metadata": {
        "id": "zAeZyqF280Vh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Even Numbers\n",
        "def find_even_numbers():\n",
        "  for x in range (1,11):\n",
        "    y = x % 2\n",
        "    if y == 0: print (x)\n",
        "\n",
        "find_even_numbers()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Aj57K14G9KND",
        "outputId": "dd5c101d-ed64-4b82-85ee-95a43ec139a3"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n"
          ]
        }
      ]
    }
  ]
}
