#!/bin/bash

sudo apt install openvpn

sudo openvpn --config vpn_config_file.ovpn --auth-user-pass credential.txt
