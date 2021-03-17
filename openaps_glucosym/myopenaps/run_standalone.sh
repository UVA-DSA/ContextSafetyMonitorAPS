#apt-get update && apt-get install -y build-essential clang vim screen wget bzip2 git libglib2.0-0 python-pip capnproto libcapnp-dev libzmq5-dev libffi-dev libusb-1.0-0
#pip2 install numpy==1.11.2 scipy==0.18.1 matplotlib
#pip2 install -r requirements_openpilot.txt

export PYTHONPATH="$PWD":$PYTHONPATH
python initialize.py 200
python updated_ct_script_iob_based.py
# /bin/sh -c './updated_ct_script_iob_based.py'
