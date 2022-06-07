{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Streamlit Image Classification Web App",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lawliaet/dc/blob/main/score.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "j5C8c_IfYHfH",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 697
        },
        "outputId": "c6779135-ac81-4669-940e-04143c457b79"
      },
      "source": [
        "!pip install -U ipykernel==5.3.4"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting ipykernel==5.3.4\n",
            "  Downloading ipykernel-5.3.4-py3-none-any.whl (120 kB)\n",
            "\u001b[K     |████████████████████████████████| 120 kB 5.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: tornado>=4.2 in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.1.1)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.3.5)\n",
            "Requirement already satisfied: ipython>=5.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.5.0)\n",
            "Requirement already satisfied: traitlets>=4.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel==5.3.4) (5.1.1)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (0.7.5)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (4.4.2)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (57.4.0)\n",
            "Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (0.8.1)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (2.6.1)\n",
            "Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (1.0.18)\n",
            "Requirement already satisfied: pexpect in /usr/local/lib/python3.7/dist-packages (from ipython>=5.0.0->ipykernel==5.3.4) (4.8.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython>=5.0.0->ipykernel==5.3.4) (0.2.5)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython>=5.0.0->ipykernel==5.3.4) (1.15.0)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel==5.3.4) (4.10.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel==5.3.4) (2.8.2)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel==5.3.4) (23.0.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect->ipython>=5.0.0->ipykernel==5.3.4) (0.7.0)\n",
            "Installing collected packages: ipykernel\n",
            "  Attempting uninstall: ipykernel\n",
            "    Found existing installation: ipykernel 4.10.1\n",
            "    Uninstalling ipykernel-4.10.1:\n",
            "      Successfully uninstalled ipykernel-4.10.1\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires ipykernel~=4.10, but you have ipykernel 5.3.4 which is incompatible.\u001b[0m\n",
            "Successfully installed ipykernel-5.3.4\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "ipykernel"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rrVDYLxxMzxz"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uxclE-m8LZa6"
      },
      "source": [
        "!pip install -q streamlit"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j-qizgiOFEkc",
        "outputId": "3c9d0261-9b53-4788-b7ae-5a2daaaf9c32"
      },
      "source": [
        "!wget https://bin.equinox.io/c/4VmDzA7iaHb/-stablngroke-linux-amd64.zip"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-06-07 10:53:03--  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip\n",
            "Resolving bin.equinox.io (bin.equinox.io)... 54.237.133.81, 18.205.222.128, 52.202.168.65, ...\n",
            "Connecting to bin.equinox.io (bin.equinox.io)|54.237.133.81|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 13832437 (13M) [application/octet-stream]\n",
            "Saving to: ‘ngrok-stable-linux-amd64.zip.1’\n",
            "\n",
            "ngrok-stable-linux- 100%[===================>]  13.19M  8.48MB/s    in 1.6s    \n",
            "\n",
            "2022-06-07 10:53:04 (8.48 MB/s) - ‘ngrok-stable-linux-amd64.zip.1’ saved [13832437/13832437]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MrUFFcWtFIC_",
        "outputId": "f7a9b352-de8e-4855-8899-c1dcf5e9ebc0"
      },
      "source": [
        "!unzip ngrok-stable-linux-amd64.zip"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  ngrok-stable-linux-amd64.zip\n",
            "replace ngrok? [y]es, [n]o, [A]ll, [N]one, [r]ename: A\n",
            "  inflating: ngrok                   \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DEpqpO_1FNWJ",
        "outputId": "1c5d359e-a631-4e55-af1b-b3ef790b9e62"
      },
      "source": [
        "!ls"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ngrok\t\t\t      ngrok-stable-linux-amd64.zip.1\n",
            "ngrok-stable-linux-amd64.zip  sample_data\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hVZv2sH3FRzo",
        "outputId": "1411a811-cf63-4b0d-9609-1c88cf3cb33f"
      },
      "source": [
        "!./ngrok "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NAME:\n",
            "   ngrok - tunnel local ports to public URLs and inspect traffic\n",
            "\n",
            "DESCRIPTION:\n",
            "    ngrok exposes local networked services behinds NATs and firewalls to the\n",
            "    public internet over a secure tunnel. Share local websites, build/test\n",
            "    webhook consumers and self-host personal services.\n",
            "    Detailed help for each command is available with 'ngrok help <command>'.\n",
            "    Open http://localhost:4040 for ngrok's web interface to inspect traffic.\n",
            "\n",
            "EXAMPLES:\n",
            "    ngrok http 80                    # secure public URL for port 80 web server\n",
            "    ngrok http -subdomain=baz 8080   # port 8080 available at baz.ngrok.io\n",
            "    ngrok http foo.dev:80            # tunnel to host:port instead of localhost\n",
            "    ngrok http https://localhost     # expose a local https server\n",
            "    ngrok tcp 22                     # tunnel arbitrary TCP traffic to port 22\n",
            "    ngrok tls -hostname=foo.com 443  # TLS traffic for foo.com to port 443\n",
            "    ngrok start foo bar baz          # start tunnels from the configuration file\n",
            "\n",
            "VERSION:\n",
            "   2.3.40\n",
            "\n",
            "AUTHOR:\n",
            "  inconshreveable - <alan@ngrok.com>\n",
            "\n",
            "COMMANDS:\n",
            "   authtoken\tsave authtoken to configuration file\n",
            "   credits\tprints author and licensing information\n",
            "   http\t\tstart an HTTP tunnel\n",
            "   start\tstart tunnels by name from the configuration file\n",
            "   tcp\t\tstart a TCP tunnel\n",
            "   tls\t\tstart a TLS tunnel\n",
            "   update\tupdate ngrok to the latest version\n",
            "   version\tprint the version string\n",
            "   help\t\tShows a list of commands or help for one command\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a3gBR5EsiIa7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f38b6130-cda4-4dfc-cf2a-7a765ae4e95f"
      },
      "source": [
        "!pip install pyngrok==4.1.8"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: pyngrok==4.1.8 in /usr/local/lib/python3.7/dist-packages (4.1.8)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.7/dist-packages (from pyngrok==4.1.8) (0.16.0)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.7/dist-packages (from pyngrok==4.1.8) (3.13)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xEjZmh1V078P"
      },
      "source": [
        "https://ngrok.com/\n",
        "\n",
        "⚠️⚠️Update the token below from creating an account in ngrok website⚠️⚠️\n",
        "\n",
        "You can ignore Ngrok step completely if you are not looking to expose your app to internet\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YjoAEsIEh-oZ",
        "cellView": "both",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2fc9f1d4-38f5-4ec0-f80c-40065c4ccfea"
      },
      "source": [
        "!./ngrok authtoken 21j68CC03JWN6TY2Vh9sqDABXib_2JYYHuEduf95MSPoDYz6z"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.ngrok2/ngrok.yml\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hvmlfY16Yg9O",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d188b3a7-16a0-4625-b21a-2ff311e2def7"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RuNpGDdZY3WW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4e844031-c215-42e0-fd0d-82feec229e09"
      },
      "source": [
        "%%writefile score.py\n",
        "\n",
        "import tensorflow as tf\n",
        "import numpy as np\n",
        "import streamlit as st\n",
        "from PIL import Image\n",
        "import requests\n",
        "from io import BytesIO\n",
        "\n",
        "st.set_option('deprecation.showfileUploaderEncoding', False)\n",
        "st.title(\"Image Classifier\")\n",
        "st.text(\"Provide URL of flower Image for image classification\")\n",
        "\n",
        "@st.cache(allow_output_mutation=True)\n",
        "def load_model():\n",
        "  model = tf.keras.models.load_model('/content/drive/MyDrive/protomodel/chessmodel')\n",
        "  return model\n",
        "\n",
        "with st.spinner('Loading Model Into Memory....'):\n",
        "  model = load_model()\n",
        "\n",
        "classes=['Bishop', 'King', 'Knight', 'Pawn', 'Queen', 'Rook']\n",
        "\n",
        "\n",
        "def scale(image):\n",
        "  image = tf.cast(image, tf.float32)\n",
        "  image /= 255.0 # external data norm while training\n",
        "  # in our case norm is part of sequential model\n",
        "\n",
        "  return tf.image.resize(image,[224,224])\n",
        "\n",
        "def decode_img(image):\n",
        "  img = tf.image.decode_jpeg(image, channels=3)\n",
        "  img = scale(img)\n",
        "  return np.expand_dims(img, axis=0)\n",
        "\n",
        "path = st.text_input('Enter Image URL to Classify.. ','https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg')\n",
        "image_file = st.file_uploader(\"Upload Images\", type=[\"png\",\"jpg\",\"jpeg\"])\n",
        "if path is not None:\n",
        "    content = requests.get(path).content\n",
        "\n",
        "    st.write(\"Predicted Class :\")\n",
        "    with st.spinner('classifying.....'):\n",
        "      label =np.argmax(model.predict(decode_img(content)),axis=1)\n",
        "      st.write(np.array(classes))\n",
        "      st.write(model.predict(decode_img(content)))\n",
        "      st.write(classes[label[0]])    \n",
        "    st.write(\"\")\n",
        "    image = Image.open(BytesIO(content))\n",
        "    st.image(image, caption='Classifying Bean Image', use_column_width=True)    \n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting score.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zhFjAjHFP62u"
      },
      "source": [
        "# import tensorflow as tf\n",
        "# model = tf.keras.models.load_model('/content/drive/MyDrive/Colab Notebooks/models/flower/models')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZeUbOXBNhVmq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "effc2ecb-0484-4e3a-e37a-91ce2363234e"
      },
      "source": [
        "!nohup streamlit run score.py >/dev/null &"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "nohup: redirecting stderr to stdout\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run score.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DIZfUBEmzmQf",
        "outputId": "e18433af-fe42-426e-9669-84fb0bb7bc1d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2022-06-07 11:20:18.299 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n",
            "\u001b[K\u001b[?25hnpx: installed 22 in 2.117s\n",
            "your url is: https://warm-hats-remain-34-73-109-20.loca.lt\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.2:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.73.109.20:8501\u001b[0m\n",
            "\u001b[0m\n",
            "2022-06-07 11:20:48.934774: W tensorflow/core/common_runtime/gpu/gpu_bfc_allocator.cc:39] Overriding allow_growth setting because the TF_FORCE_GPU_ALLOW_GROWTH environment variable is set. Original config value was 0.\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YB0kwgXqhdeo",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "0ad56514-72a3-4273-beaa-3926d177ee68"
      },
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "url = ngrok.connect(port=8503)\n",
        "url"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'http://b34b-34-73-109-20.ngrok.io'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "71SR5W0rkrsw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d7d5a570-f3ed-4877-ff79-1ffc25471604"
      },
      "source": [
        "!cat nohup.out"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cat: nohup.out: No such file or directory\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mvmVgcgCODxD"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}